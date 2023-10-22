import pathlib


def debug_print(data, debug_mode=True):
    if debug_mode:
        print(f"Debugging: {data}")


def file_exists(file):
    return pathlib.Path(file).exists()