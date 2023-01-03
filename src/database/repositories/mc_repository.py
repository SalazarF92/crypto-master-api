import json
from src.statistics.monte_carlo import monte_carlo


class MCRepository:

    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def monte_carlo_values(self):
        psql = """INSERT into monte_carlo(crypto_exchange, start_date, end_date, next_date, min_variation, max_variation) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id"""
        mc = monte_carlo()
        for x in range(len(mc['extreme'])):
            self.cursor.execute(psql, (str(mc['extreme'][x][0]), mc['start'],  mc['end'], mc['next'],
                                float(mc['extreme'][x][1]), float(mc['extreme'][x][2])))
            self.conn.commit()

    def get_interval(self, days):
        rowarray_list = []
        # "SELECT * FROM monte_carlo WHERE created_at >= NOW() - INTERVAL '60 days';"
        psql = """SELECT crypto_exchange, min_variation, max_variation FROM monte_carlo WHERE created_at >= NOW() - INTERVAL 'VALUES(%s) days';"""
        self.cursor.execute(psql, days)
        scrap = self.cursor.fetchall()
        print(scrap)
        for row in scrap:
          t = ({'crypto_exchange': row[0], 'min_variation': float(row[1]), 'max_variation': float(row[2])})
          rowarray_list.append(t)
          
        return json.dumps(rowarray_list)