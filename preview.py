"""Local static preview with byte-range support for the video timeline."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import re


class PreviewHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        self.byte_range = None
        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            return super().send_head()
        stream = open(path, 'rb')
        size = os.fstat(stream.fileno()).st_size
        requested = self.headers.get('Range')
        if requested:
            match = re.fullmatch(r'bytes=(\d*)-(\d*)', requested)
            if not match or not any(match.groups()):
                stream.close()
                self.send_error(416)
                return None
            left, right = match.groups()
            start = int(left) if left else max(0, size - int(right))
            end = min(int(right), size - 1) if left and right else size - 1
            if start >= size or start > end:
                stream.close()
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{size}')
                self.end_headers()
                return None
            self.byte_range = (start, end)
            stream.seek(start)
            self.send_response(206)
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
            length = end - start + 1
        else:
            self.send_response(200)
            length = size
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(length))
        self.end_headers()
        return stream

    def copyfile(self, source, outputfile):
        if self.byte_range is None:
            return super().copyfile(source, outputfile)
        remaining = self.byte_range[1] - self.byte_range[0] + 1
        while remaining:
            chunk = source.read(min(65536, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    server = ThreadingHTTPServer(('127.0.0.1', 8766), partial(PreviewHandler, directory=str(root)))
    print('EmbodiSafety preview: http://127.0.0.1:8766/', flush=True)
    server.serve_forever()
