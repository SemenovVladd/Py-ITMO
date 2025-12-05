import logging

import requests

import sys


def logger(func=None, *, handle=sys.stdout):
    if isinstance(handle,logging.Logger):
        info= handle.info
#        error= handle.error
    else:
        info= handle.write

    def iner():
        info("Вызаваем функцию")
        try:
            return func()
        except Exception as e:
            info(str(e))
            raise e
        finally:
            info("Завершение вызова")
    return iner

@logger
def get_currencies(url='https://www.cbr-xml-daily.ru/daily_json.js'):
    try:
        if url!='https://www.cbr-xml-daily.ru/daily_jsn.js':
            raise ValueError
        response=requests.get(url)
        a=response.json()
        d={}
        for i in a['Valute']:
            d[i]=a['Valute'][i]['Value']
        return d
    except KeyError as e:
        raise e
def cur():
    curses1=[]
    d=get_currencies()
    for i in d:
        curses1.append((i,str(d[i])))
    return curses1
print(get_currencies())
print(100)