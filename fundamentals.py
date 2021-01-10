from polygon import RESTClient


def run():
    key = "AKIJL74XBP2M5WEQBZ2L"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects

    list_of_cash_flows = []
    with RESTClient(key) as client:
        resp = client.reference_stock_financials("PYPL", limit=20, type="YA", sort="-reportPeriod")
        #print(resp.results)
        
        for result in resp.results:
            free_cash_flow = result['freeCashFlow']
            list_of_cash_flows.append(free_cash_flow)
            print(result['reportPeriod'] + ":", f"${free_cash_flow:,}")
        
    


run()


