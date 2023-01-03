import subprocess

args = ['ffmpeg', '-y', '-ss', '1', '-accurate_seek', '-i', '../videos/01.mp4', '-to', '1', '-c', 'copy', 'outputs/middle command.mp4']
subprocess.run(args, check=True)
