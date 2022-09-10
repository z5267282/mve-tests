import subprocess, sys
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
    return result.stdout

    # return int(
    #     round(
    #         float(result.stdout), 0
    #     )
    # )

print(get_duration(sys.argv[1]))
