import argparse
import os
import sys
import pandas as pd
from tools import *
from down_software import *


def parameter_input():
    parser = argparse.ArgumentParser(description='pha_downstream (Phage_downstream pipeline)')
    parser.add_argument('-contigs', help='Path to the contigs file')
    parser.add_argument('-o', '--output', help='Path to output directory', default=f'{os.getcwd()}/result')
    parser.add_argument('-t', '--threads', type=int, help='Threads used to run this pipeline (default:1)', default=1)
    parser.add_argument('-k', '--keep_log', action='store_true',
                        help='This parameter allows you to continue a killed run, but please make sure you have not changed any files in the output directory.',
                        default=False)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    db = "/cpfs01/projects-HDD/cfff-47998b01bebd_HDD/rj_24212030018/db"  # please adjust db here
    args = parameter_input()
    threads = args.threads
    output = args.output
    sample = args.contigs

    # check if the user is using "keep_log"
    if args.keep_log is False:
        with open(f"{output}/log2.txt", "w") as f:
            f.write("0\n")

    # get log info
    with open(f"{output}/log.txt", "r") as f:
        log = int(f.readline()[0: -1])
    # assess quality of sequencing with fastqc
    if log < 1:
        run_phabox2(sample, output, threads, db)
        log = 1
        with open(f"{output}/log2.txt", "w") as f:
            f.write(f"{log}\n")

