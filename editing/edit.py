import subprocess
def edit_video(joined_src_path, joined_dst_path, start, end=None):
    args = ['ffmpeg', '-y']
    source = ['-i', joined_src_path]
    args += ['-sseof', start, *source] if start.startswith('-') else [*source, '-ss', start]

    if not end is None:
        args += ['-to', end]
        
    args.append(joined_dst_path)
    subprocess.run(args, check=True)
    return args

