-- A script that creates a table
CREATE TABLE IF NOT EXISTS unique_id(
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
