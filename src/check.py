#!/usr/bin/env python3

import difflib
import glob
import os
import pathlib
import re
import sys

import solve

# Make paths relative to the folder containing the script so that it can be called from anywhere
src_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = pathlib.Path(src_dir / '../data/')
input_filename_pattern = 'input*.txt'
result_filename_pattern = 'result{}.out'
output_filename_pattern = 'output{}.txt'

# Iterate over files in zip
for filepath in sorted(glob.glob(os.path.join(data_dir, input_filename_pattern))):
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    print('Solving with input file {}'.format(base_filename))
    file_number = re.search(r'\d+', base_filename).group()
    # Solve input<n>.txt and write result to result<n>.out
    with open(filepath, 'r') as input_stream, \
            open(os.path.join(data_dir, result_filename_pattern.format(file_number)), 'w') as result_stream:
        solve.solve(input_stream, result_stream)
    print('Diff:')
    # Compare produced result<n>.out with expected data from output<n>.txt
    with open(os.path.join(data_dir, output_filename_pattern.format(file_number)), 'r') as output_stream, \
            open(os.path.join(data_dir, result_filename_pattern.format(file_number)), 'r') as result_stream:
        diff = difflib.context_diff(result_stream.readlines(), output_stream.readlines())
        sys.stderr.writelines(diff)
