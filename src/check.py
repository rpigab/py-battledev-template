#!/usr/bin/env python3

import glob
import os
import re
import solve

data_folder = './data/'
input_filename_pattern = 'input*.txt'
output_filename_pattern = 'result{}.out'

for filepath in sorted(glob.glob(os.path.join(data_folder, input_filename_pattern))):
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    file_number = re.search(r'\d+', base_filename).group()
    with open(filepath, 'r') as input_stream, \
            open(os.path.join(data_folder, output_filename_pattern.format(file_number)), 'w') as output_stream:
        solve.solve(input_stream, output_stream)
