USE project;

INSERT OVERWRITE LOCAL DIRECTORY './output/insight_4'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT count(*), round((expire_unix - q_unix_time) / 60 / 60 / 24) as lifetime_days FROM tesla_option_chain_opt GROUP BY round((expire_unix - q_unix_time) / 60 / 60 / 24);

