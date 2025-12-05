import requests
def get_currencies(d={}):
    response=requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    a=response.json()
    d={}
    for i in a['Valute']:
        d[i]=a['Valute'][i]['Value']
    return d