import os
import sys

import config as cfg

import constants.file_structure as fst

import helpers.check_and_exit_if as check_and_exit_if
import helpers.files as files
import helpers.util as util

def run_checks():
    check_and_exit_if.bad_args(sys.argv)
    check_and_exit_if.no_source_folder()
    if os.path.exists(fst.REMAINING):
        check_and_exit_if.files_remaining()


def main():
    run_checks()

    new_files = files.ls(cfg.SOURCE)
    util.write_to_json(new_files, fst.REMAINING)

if __name__ == '__main__':
    main()
