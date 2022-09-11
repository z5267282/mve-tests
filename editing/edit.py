import subprocess
import moviepy.editor as mvp
import config as cfg
import video_editing as vde

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
    args = ['ffmpeg', '-y']
    source = ['-i', joined_src_path]

    if not start is None:
        args += ['-sseof', start, *source] if start.startswith('-') else [*source, '-ss', start]

    if not end is None:
        args += ['-to', end]
        
    args.append(joined_dst_path)
    subprocess.run(args, check=True)

