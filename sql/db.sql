START TRANSACTION;

CREATE TABLE tesla_option_chain (
	transaction_id integer NOT NULL PRIMARY KEY,
	q_unix_time text,
	q_read_time text,
	q_date date,
	q_time_h real,
	underlying_last real,
	expire_date date,
	expire_unix VARCHAR(50),
	dte real,
	c_delta real,
	c_gamma real,
	c_vega real,
	c_theta real,
	c_rho real,
	c_iv real,
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
	p_delta real,
	p_gamma real,
	p_vega real,
	p_theta real,
	p_rho real,
	p_iv real,
	p_volume real,
	strike_distance real,
	strike_distance_pct real
);

\COPY tesla_option_chain FROM './data/data.csv' DELIMITER ',' CSV HEADER NULL '';

COMMIT;

-- SELECT * FROM tesla_option_chain LIMIT(10);
