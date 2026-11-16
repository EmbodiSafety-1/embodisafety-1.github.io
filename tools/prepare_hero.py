from pathlib import Path
import json,subprocess

root=Path(__file__).resolve().parents[1]
selected=[('refuse-pharmacy-theft',90),('constrain-wet-tray',50),('passport-disposal',65)]
chapters=[];start=0;lines=[]
for slug,focus in selected:
    src=f'assets/videos/{slug}.mp4'
    path=(root/src).resolve()
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=nb_frames','-of','json',str(path)],text=True))['streams'][0]
    duration=int(probe['nb_frames'])/24
    chapters.append({'src':src,'poster':f'assets/posters/{slug}.webp','focus':focus,'start':round(start,6),'duration':round(duration,6),'end':round(start+duration,6)})
    start+=duration
    lines.append("file '"+path.as_posix()+"'")
concat=Path(__file__).parent/'hero-concat.txt'
concat.write_text('\n'.join(lines),encoding='utf-8')
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(root/'assets/videos/hero-examples.mp4')],check=True)
(root/'assets/hero-chapters.json').write_text(json.dumps(chapters,indent=2),encoding='utf-8')
print('Hero:',len(chapters),'examples;',round(start,3),'seconds;', (root/'assets/videos/hero-examples.mp4').stat().st_size,'bytes')
