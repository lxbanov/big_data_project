#!/bin/bash

echo "Installing pip..."
if [ ! -f "get-pip.py" ]; then 
	wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
	python3.6 get-pip.py
fi

echo "Installed pip"

pip3 install pandas

if [ ! -f "postgresql-42.6.0.jar" ]; then
	wget https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --no-check-certificate
	cp  postgresql-42.6.0.jar /usr/hdp/current/sqoop-client/lib/
fi

echo "Installed pandas"

rm -f /var/lib/pgsql/data/pg_hba.conf
cp ./config/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
sudo systemctl restart postgresql
echo "Configured postgresql"

if [ ! -f "./data/tsla_2019_2022.csv" ]; then
	wget -O ./data/tsla_2019_2022.csv https://storage.yandexcloud.net/alobanov-innopolis-0/tsla_2019_2022.csv
fi 

echo "Data is ready to be preprocessed"

python3.6 /root/big_data_project/scripts/preprocess.py -i "./data/tsla_2019_2022.csv" -o "./data"
echo "Data is processed"
