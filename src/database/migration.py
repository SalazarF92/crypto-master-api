uuid = """
 CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
"""

user = """
CREATE TABLE IF NOT EXISTS users (
id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL)"""

crypto = """
CREATE TABLE IF NOT EXISTS cryptos (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    market_cap VARCHAR(255) NOT NULL,
    volume_24h VARCHAR(255) NOT NULL,
    percent_change_1h VARCHAR(255) NOT NULL,
    percent_change_24h VARCHAR(255) NOT NULL,
    percent_change_7d VARCHAR(255) NOT NULL,
    last_updated VARCHAR(255) NOT NULL,
    user_id UUID REFERENCES users(id)
);
"""


def command_tables(conn):
    create_tables = [uuid, user]
    for create_table in create_tables:
        conn.cursor().execute(create_table)
        conn.commit()
