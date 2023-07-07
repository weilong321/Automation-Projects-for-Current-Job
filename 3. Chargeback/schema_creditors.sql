DROP TABLE IF EXISTS creditors;

CREATE TABLE creditors (
    supplier VARCHAR(255),
    supplier_name VARCHAR(255),
    tran_date DATE,
    item VARCHAR(255),
    reference VARCHAR(255),
    apply VARCHAR(255),
    tran_type VARCHAR(255),
    due_date DATE,
    currency VARCHAR(255),
    value FLOAT,
    rate VARCHAR(255),
    base_value FLOAT,
    tran_period VARCHAR(255),
    age_period VARCHAR(255),
    posting_period VARCHAR(255)
);

CREATE INDEX IF NOT EXISTS creditorsItemIdx
ON creditors (item);