import subprocess
SRC = '../videos/03.mp4'
DUR = 75
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

def check_timestamp(timestamp, duration):
    return sum(
        int(t) * (60 ** i)
            for t, i in enumerate(reversed(timestamp.split(':')), start=1)
    ) <= duration

def check_good_time(joined_src_path, time):
    duration = get_duration(joined_src_path)

    if time.startswith('-'):
        return int(time[1:]) <= duration 

    if ':' in time:
        return check_timestamp(time)

    return int(time) <= duration

