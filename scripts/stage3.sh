#!/bin/bash

if [ -d $(pwd)/output/lr_pred ]; then
	rm -rf $(pwd)/output/lr_pred
fi

if [ -d $(pwd)/output/fm_pred ]; then
	rm -rf $(pwd)/output/fm_pred
fi


spark-submit --jars /usr/hdp/current/hive-client/lib/hive-metastore-1.2.1000.2.6.5.0-292.jar,/usr/hdp/current/hive-client/lib/hive-exec-1.2.1000.2.6.5.0-292.jar --packages org.apache.spark:spark-avro_2.12:3.0.3 $(pwd)/scripts/models.py

cat $(pwd)/output/lr_pred/*.csv > $(pwd)/output/lr_pred.csv

cat $(pwd)/output/fm_pred/*.csv > $(pwd)/output/fm_pred.csv




