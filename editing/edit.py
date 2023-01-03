import subprocess
import moviepy.editor as mvp
import config as cfg
import video_editing as vde
import time_handlers

def edit_video(joined_src_path, joined_dst_path, start, end):
    if cfg.USE_MOVIEPY:
        edit_moviepy(joined_src_path, joined_dst_path, start, end)
    else:
        edit_ffmpeg(joined_src_path, joined_dst_path, start, end)

def edit_moviepy(joined_src_path, joined_dst_path, start, end):
    with mvp.VideoFileClip(joined_src_path) as file:
        clip = file.subclip(t_start=start, t_end=end)
        clip.write_videofile(
            joined_dst_path,
            threads=cfg.NUM_THREADS,
            fps=vde.FRAMES,
            codec=vde.VCODEC,
            preset=vde.COMPRESSION,
            audio_codec=vde.ACODEC
        )

def edit_ffmpeg(joined_src_path, joined_dst_path, start, end):
    source = ['-accurate_seek', '-i', joined_src_path]
    args = ['ffmpeg', '-y', *generate_ffmpeg_args(source, start, end), '-c', 'copy', joined_dst_path]
    print(args)
    subprocess.run(args, check=True)

def generate_ffmpeg_args(source, start, end):
    if start is None and end is None:
        return source

    if start is None:
        return [*source, '-to', end]

    if end is None:
        return ['-sseof' if start.startswith('-') else '-ss', start, *source]

    relative_time = str(
        time_handlers.get_seconds(end) - time_handlers.get_seconds(start)
    )
    return ['-ss', start, *source, '-to', relative_time]

