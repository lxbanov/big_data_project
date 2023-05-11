USE project;
INSERT OVERWRITE LOCAL DIRECTORY './output/insight_3'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT strike,underlying_last,expire_unix,dte,c_volume,c_last,c_size,c_bid,c_ask,p_volume,p_last,p_size,p_bid,p_ask FROM tesla_option_chain_opt;

