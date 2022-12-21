import datetime
from statistics.monte_carlo import monte_carlo

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=12&page=1&sparkline=false"


def test_monte_carlo():
    assert 1 == 1
    mc = monte_carlo(url)
    assert len(mc["extreme"]) > 0
    assert type(mc["extreme"]) is list
    assert type(mc["start"]) is datetime.datetime
    assert type(mc["end"]) is datetime.datetime
    assert type(mc["next"]) is datetime.datetime
