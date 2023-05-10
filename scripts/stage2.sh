#!/bin/bash

hdfs dfs -test -d /project/avsc/ && hdfs dfs -rm -r /project/avsc/
hdfs dfs -mkdir	 /project/avsc
hdfs dfs -put ./avsc/*.avsc /project/avsc/

hive -f ./sql/db.hql > hive_results.txt
