import subprocess, re
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
    return round_float(result.stdout)

def round_float(float_string):
    match = re.match(r'([(0-9)]+)\.([0-9])', float_string)
    whole_number, tenths = int(match.group(1)), int(match.group(2))
    return whole_number + (tenths >= 5)

def get_seconds(time):
    if time.startswith('-'):
        return int(time[1:])

    if ':' in time:
        return get_timestamp_seconds(time)

    return int(time)

def get_timestamp_seconds(timestamp):
    return sum(
        int(t) * (60 ** i)
            for i, t in enumerate(
                reversed(
                    timestamp.split(':')
                )
            )
    )
