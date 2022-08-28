import subprocess
def edit_video(joined_src_path, joined_dst_path, start, end):
    args = [
        'ffmpeg', '-y',
        '-i', joined_src_path,
        '-sseof' if start.startswith('-1') else '-ss', start,
    ]
    if not end is None:
        args += ['-to', end]
    args.append(joined_dst_path)
    subprocess.run(args, check=True)

