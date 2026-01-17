import requests
import pandas as pd
from datetime import datetime
def test_api_brl_rate():
    url='https://v6.exchangerate-api.com/v6/73c592037bf219f44e3ee7bf/latest/USD'
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert 'BRL' in data['conversion_rates']
    assert 'time_last_update_utc' in data
    assert 'time_next_update_unix' in data
    brazil_rate=data['conversion_rates']['BRL']
    assert isinstance(brazil_rate, float)
    assert brazil_rate > 0
    last_update=data['time_last_update_utc']
    next_update=datetime.fromtimestamp(data['time_next_update_unix'])
    df = pd.DataFrame({'Currency':'BRL','Rate':[brazil_rate],'Last Update':[last_update],'Next Update':[next_update]},index=['Brazil'])
    print(df)
    now=datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name=f'exchange_rates_report_{now}.xlsx'
    df.to_excel(file_name, index=False)
    print(df)
    print(f'Your file name is {file_name}')