"""Generate the tiny 240 px / 8 fps preview loops used by the dataset mosaic.

The mosaic autoplays one clip per tile, so the page must not pull the full
640x360 masters (6.9 MB for 32 clips). Each tile plays a silent H.264 loop at
240 px wide, 8 fps (about 19 KB, 0.58 MB for all 32); clicking a tile still
opens the full-size master in the lightbox.

Requires ffmpeg on PATH. Idempotent: existing previews are kept unless --force.

    python tools/make_previews.py [--force]
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'assets/demos/manifest.json'
preview_dir = root / 'assets/demos/previews'
preview_dir.mkdir(parents=True, exist_ok=True)
force = '--force' in sys.argv

if not shutil.which('ffmpeg'):
    sys.exit('ffmpeg not found on PATH')

demos = json.loads(manifest_path.read_text(encoding='utf-8'))
for demo in demos:
    source = root / demo['src']
    preview = preview_dir / f"{demo['id']}.mp4"
    if force or not preview.exists():
        subprocess.run([
            'ffmpeg', '-v', 'error', '-y', '-i', str(source),
            '-vf', 'fps=8,scale=240:-2',
            '-c:v', 'libx264', '-crf', '34', '-preset', 'veryslow',
            '-an', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
            str(preview),
        ], check=True)
    demo['preview'] = preview.relative_to(root).as_posix()

total = sum((root / d['preview']).stat().st_size for d in demos)
ordered = []
for demo in demos:
    entry = {}
    for key, value in demo.items():
        if key != 'preview':
            entry[key] = value
        if key == 'poster':
            entry['preview'] = demo['preview']
    ordered.append(entry)
manifest_path.write_text(json.dumps(ordered, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'{len(ordered)} previews, {total / 1024:.0f} KB total')
