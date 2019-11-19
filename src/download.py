#!/usr/bin/env python3

import io
import os
import pathlib
import sys
from zipfile import ZipFile

import requests

DEFAULT_URL = 'https://questionsacm.isograd.com/codecontest/sample_input_output/sample-lJdOuPUVRty107MkPy5Em4OWCFIWHYf6rV_gf6jAgU4.zip'

# Make paths relative to the folder containing the script so that it can be called from anywhere
src_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = pathlib.Path(src_dir / '../data/')
zip_filepath = data_dir / 'data.zip'
url = sys.argv[1] if len(sys.argv) >= 2 else DEFAULT_URL

# Get zip from url
response = requests.get(url)
if not response:
    exit('Invalid response, got status code {}'.format(response.status_code))
zip_file = ZipFile(io.BytesIO(requests.get(url).content))

# Delete existing txt files from data folder
txt_files = os.listdir(data_dir)
for file in txt_files:
    if file.endswith('.txt'):
        os.remove(data_dir / file)

# Extract .txt files to data folder
for fileName in zip_file.namelist():
    if fileName.endswith('.txt'):
        with open(data_dir / pathlib.PurePath(fileName).name, 'wb') as f_out:
            f_out.write(zip_file.read(fileName))
