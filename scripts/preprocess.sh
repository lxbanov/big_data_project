#!/bin/bash

wget    -O  "./data/tesla.zip" http://download.alobanov.space/Introduction-to-Big-Data/tesla.zip 
unzip   -d  ./data/ ./data/tesla.zip 
python3 ./scripts/preprocess.py -i "./data/tsla_2019_2022.csv" -o "./data"
rm      -f  ./data/tsla_2019_2022.csv
rm      -f  ./data/tesla.zip