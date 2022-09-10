import subprocess, sys, re
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
    match = re.match(r'([(0-9)]+)\.([0-9])', result.stdout)
    whole_number, tenths = int(match.group(1)), int(match.group(2))
    return whole_number + (tenths >= 5)

print(get_duration(sys.argv[1]))
