#!/bin/bash

psql -U postgres -c 'DROP DATABASE IF EXISTS project;'

psql -U postgres -c 'CREATE DATABASE project;'

psql -U postgres -d project -f "$(pwd)/sql/db.sql"

hdfs dfs -rm -r /project
# hdfs dfs -mkdir /project
# rm -rf ./avsc
if [ -d "$(pwd)/avsc" ]; then
	rm -rf $(pwd)/avsc
fi

sqoop import-all-tables \
    -Dmapreduce.job.user.classpath.first=true \
    -Dmapreduce.map.memory.mb=2048 \
    --connect jdbc:postgresql://localhost/project \
    --username postgres \
    --warehouse-dir /project \
    --as-avrodatafile \
    --compression-codec=snappy \
    --outdir ./avsc \
    --m 1
