DROP DATABASE IF EXISTS project CASCADE;
CREATE DATABASE project;
USE project;
SET mapreduce.map.output.compress = true;
SET mapreduce.map.output.compress.codec = org.apache.hadoop.io.compress.SnappyCodec;
SET hive.enforce.bucketing = true;
--SET hive.exec.dynamic.partition = true;
--SET hive.exec.dynamic.partition.mode = nonstrict;
set hive.tez.container.size=1024;
set hive.tez.java.opts=-Xmx4096m;
set tez.runtime.io.sort.mb=512;
set tez.task.resource.memory.mb=1024;
set tez.am.resource.memory.mb=1024;
set tez.am.launch.cmd-opts=-Xmx4096m;
-- SET hive.exec.max.dynamic.partitions=100000;
--SET hive.exec.max.dynamic.partitions.pernode=4000;

CREATE EXTERNAL TABLE tesla_option_chain 
STORED AS AVRO LOCATION '/project/tesla_option_chain'
TBLPROPERTIES ('avro.schema.url'='/project/avsc/tesla_option_chain.avsc');

SELECT * FROM tesla_option_chain LIMIT 15;

DROP TABLE IF EXISTS tesla_option_chain_opt PURGE;

CREATE EXTERNAL TABLE tesla_option_chain_opt (
	transaction_id int,
	q_unix_time bigint,
	q_time_h float,
	underlying_last float,
	expire_unix bigint,
	dte float,
	c_volume float,
	c_last float,
	c_size VARCHAR(50),
	c_bid float,
	c_ask float,
	strike float,
	p_bid float,
	p_ask float,
	p_size VARCHAR(50),
	p_last float,
	p_volume float
)
CLUSTERED BY (transaction_id) INTO 16 BUCKETS
STORED AS AVRO LOCATION '/project/tesla_option_chain_opt' 
TBLPROPERTIES ('avro.compress'='snappy');

INSERT INTO tesla_option_chain_opt SELECT * FROM tesla_option_chain;
