START TRANSACTION;

CREATE TABLE tesla_option_chain (
	transaction_id integer NOT NULL PRIMARY KEY,
	q_unix_time text,
	q_time_h real,
	underlying_last real,
	expire_unix real,
	dte real,
	c_volume real,
	c_last real,
	c_size VARCHAR(50),
	c_bid real,
	c_ask real,
	strike real,
	p_bid real,
	p_ask real,
	p_size VARCHAR(50),
	p_last real,
	p_volume real
);

\COPY tesla_option_chain FROM './data/data.csv' DELIMITER ',' CSV HEADER NULL '';

COMMIT;

-- SELECT * FROM tesla_option_chain LIMIT(10);
