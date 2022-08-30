import subprocess
def get_duration(joined_src_path):
    args = [
        'ffprobe',
        '-i',
        joined_src_path,
        '-v',
        'quiet',
        '-show_entries',
        'format=duration',
        '-hide_banner',
        '-of',
        'default=noprint_wrappers=1:nokey=1'
    ]
    result = subprocess.run(args, capture_output=True, text=True)

    return int(float(result.stdout))

def get_timestamp_seconds(timestamp):
    return sum(
        int(t) * (60 ** i)
            for i, t in enumerate(reversed(timestamp.split(':')))
    )

def in_duration_bounds(joined_src_path, time):
    duration = get_duration(joined_src_path)

    seconds = None
    if time.startswith('-'):
        seconds = int(time[1:]) 
    elif ':' in time:
        seconds = get_timestamp_seconds(time)
    else:
        seconds = int(time)

    return seconds >= 0 and seconds <= duration

