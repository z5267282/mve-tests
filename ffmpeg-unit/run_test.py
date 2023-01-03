import subprocess
import time_handlers
def edit_ffmpeg(joined_src_path, joined_dst_path, start, end):
    source = ['-accurate_seek', '-i', joined_src_path]
    args = ['ffmpeg', '-y', *generate_ffmpeg_args(source, start, end), '-c', 'copy', joined_dst_path]
    subprocess.run(args, check=True)

def generate_ffmpeg_args(source, start, end):
    if start is None and end is None:
        return source
    
    if start is None:
        return [*source, '-to', end]
    
    if end is None:
        return ['-sseof' if start.startswith('-') else '-ss', start, *source]
    
    return ['-ss', start, *source, '-to', time_handlers.get_seconds(end) - time_handlers.get_seconds(start)]

edit_ffmpeg("../videos/01.mp4", "out.mp4", "-5", None)
