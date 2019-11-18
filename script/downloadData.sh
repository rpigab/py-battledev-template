#!/usr/bin/env bash

set -ex

DATA_FOLDER=./data
TMP_ZIP_FILE=/tmp/temp.zip
ZIP_URL_DEFAULT=https://questionsacm.isograd.com/codecontest/sample_input_output/sample-lJdOuPUVRty107MkPy5Em4OWCFIWHYf6rV_gf6jAgU4.zip
ZIP_URL_ARG=$1

rm -f "${DATA_FOLDER}"/*.out ${DATA_FOLDER}/*.txt
wget --no-check-certificate "${ZIP_URL_ARG:-$ZIP_URL_DEFAULT}" -O "${TMP_ZIP_FILE}"
unzip -j "${TMP_ZIP_FILE}" "*.txt" -d "${DATA_FOLDER}/"
rm "${TMP_ZIP_FILE}"
