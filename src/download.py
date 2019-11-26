#!/usr/bin/env python3

import io
import os
import pathlib
import sys
from zipfile import ZipFile

import requests

DEFAULT_URL = 'https://questionsacm.isograd.com/codecontest/sample_input_output/sample-5xx4zqIdCTdKJ1pNSqibpMYIWyYe6Ndhvu-HMspT_aw.zip'

# Make paths relative to the folder containing the script so that it can be called from anywhere
src_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = pathlib.Path(src_dir / '../data/')
zip_filepath = data_dir / 'data.zip'
url = sys.argv[1] if len(sys.argv) >= 2 else DEFAULT_URL

# Get zip from url
print('Downloading zip file from {}'.format(url))
response = requests.get(url)
if not response:
    exit('Invalid response, got status code {}'.format(response.status_code))
zip_file = ZipFile(io.BytesIO(requests.get(url).content))

# Delete existing txt files from data folder
print('Deleting .txt and .out files from data folder')
txt_files = os.listdir(data_dir)
for file in txt_files:
    if file.endswith('.txt') or file.endswith('.out'):
        os.remove(data_dir / file)

# Extract .txt files to data folder
print('Extracting individual text files to data folder')
for file_name in zip_file.namelist():
    if file_name.endswith('.txt'):
        base_name = pathlib.PurePath(file_name).name
        print('Extracting file from archive as {}'.format(base_name))
        with open(data_dir / base_name, 'wb') as f_out:
            f_out.write(zip_file.read(file_name))
    else:
        print('Ignoring non txt file {}'.format(file_name))
