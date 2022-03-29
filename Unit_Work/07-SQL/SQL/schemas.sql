CREATE TABLE card_holder (
	id_card_holder INT PRIMARY KEY,
	card_holder_name VARCHAR(100)
);
CREATE TABLE credit_card (
	card_number VARCHAR(20) PRIMARY KEY,
	id_card_holder INT
);
CREATE TABLE merchant_category (
	id_merchant_category INT PRIMARY KEY,
	merchant_category_name VARCHAR(30)
);
CREATE TABLE merchant (
	id_merchant INT PRIMARY KEY,
	merchant_name VARCHAR(60),
	id_merchant_category int
);
CREATE TABLE transaction (
	id_transaction INT PRIMARY KEY,
	date TIMESTAMP,
	amount NUMERIC(20,2),
	card_number VARCHAR(20),
	id_merchant int
);