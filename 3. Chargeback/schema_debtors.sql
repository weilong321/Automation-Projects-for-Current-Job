DROP TABLE IF EXISTS debtors;

CREATE TABLE debtors (
	agent VARCHAR(20),
	agent_name VARCHAR(500),
	tran_date DATE,
	item VARCHAR(500),
	reference INT,
	apply INT,
	tran_type VARCHAR(500),
	currency VARCHAR(500),
	value FLOAT,
	rate INT,
	base_value FLOAT,
	tran_period VARCHAR(500),
	age_period VARCHAR(500),
	posting_period VARCHAR(500)
);

CREATE INDEX IF NOT EXISTS debtorsItemIdx
ON debtors (item);