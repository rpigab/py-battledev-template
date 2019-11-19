#!/usr/bin/env python3

import glob
import os
import pathlib
import re

import solve

# Make paths relative to the folder containing the script so that it can be called from anywhere
src_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = pathlib.Path(src_dir / '../data/')
input_filename_pattern = 'input*.txt'
result_filename_pattern = 'result{}.out'
output_filename_pattern = 'output{}.txt'

for filepath in sorted(glob.glob(os.path.join(data_dir, input_filename_pattern))):
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    file_number = re.search(r'\d+', base_filename).group()
    with open(filepath, 'r') as input_stream, \
            open(os.path.join(data_dir, result_filename_pattern.format(file_number)), 'w') as output_stream:
        solve.solve(input_stream, output_stream)
