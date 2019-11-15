#!/usr/bin/env bash

set -eux

DATA_FOLDER=./data
TMP_ZIP_FILE=/tmp/temp.zip

rm -f "${DATA_FOLDER}"/*.out ${DATA_FOLDER}/*.txt
wget --no-check-certificate $1 -O "${TMP_ZIP_FILE}"
unzip -j "${TMP_ZIP_FILE}" "*.txt" -d "${DATA_FOLDER}/"
rm "${TMP_ZIP_FILE}"
