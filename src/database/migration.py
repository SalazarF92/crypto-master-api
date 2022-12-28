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
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
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

monte_carlo = """
CREATE TABLE IF NOT EXISTS monte_carlo (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    crypto_exchange VARCHAR(30),
    start_date timestamp,
    end_date timestamp,
    next_date timestamp,
    min_variation float,
    max_variation float,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """


sentiments_reddit = """
                DROP TABLE IF EXISTS sentiments_reddit;
                CREATE TABLE sentiments_reddit(
                    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
                    coin_name VARCHAR(30),
                    coin_symbol VARCHAR(30),
                    sentiment_value float,
                    sentiment_pos int,
                    sentiment_neg int,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )

        """


def command_tables(conn):
    create_tables = [uuid, user, monte_carlo]
    for create_table in create_tables:
        conn.cursor().execute(create_table)
        conn.commit()
