import requests
import pathlib
from zipfile import ZipFile

data_folder = pathlib.Path('../data/')
zip_filepath = data_folder / 'data.zip'
url = 'https://questionsacm.isograd.com/codecontest/sample_input_output/sample-lJdOuPUVRty107MkPy5Em4OWCFIWHYf6rV_gf6jAgU4.zip'

r = requests.get(url)

with open(zip_filepath, 'wb') as f:
    f.write(r.content)

# Create a ZipFile Object and load sample.zip in it
with ZipFile(zip_filepath, 'r') as zipObj:
    # Get a list of all archived file names from the zip
    listOfFileNames = zipObj.namelist()
    # Iterate over the file names
    for fileName in listOfFileNames:
        # Check filename endswith csv
        if fileName.endswith('.txt'):
            # Extract a single file from zip
            zipObj.extract(fileName, path=data_folder)
            with open(data_folder / pathlib.PurePath(fileName).name, 'wb') as f_out:
                f_out.write(zipObj.read(fileName))
