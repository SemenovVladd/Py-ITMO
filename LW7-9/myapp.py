from jinja2 import Environment, PackageLoader, select_autoescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from controllers.databasecontroller import CurrencyRatesCRUD
from Models import Author
from Models import User
from Models import User_cur
from Models import cur
from utils import get_currencies

from controllers import databasecontroller

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)


class CurrencyRatesMock():
    def __init__(self):
        self.__values = [("USD", "90"),
                         ("EUR", "91"),
                         ("GBP", '100'),
                         ("AUD", '52.8501')]

    @property
    def values(self):
        return self.__values


c_r = CurrencyRatesMock()

c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
c_r_controller._create()
# print(c_r.values)

# main_author = author.Author('Nikolai', 'P2345')
main_author = Author('Vlad', 'P3124')

template = env.get_template("index.html")
template1 = env.get_template("users.html")
template2 = env.get_template("userss.html")
template3 = env.get_template("currencies.html")
User1 = User('Vlad', 'USD', 'yandex', '5555555555')
User2 = User('Peter', 'USD,EUR', 'goggle', '66666666666')
User3 = User('Ivan', 'USD,AUD', 'mail', '77777777777')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # global template
        global c_r_controller

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        print(self.path)
        url_query_dict = parse_qs(self.path.rpartition('?')[-1])
        if self.path == '/':
            global template

            # root url

            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = cur()

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()

            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()

            result = template.render(myapp="CurrenciesListApp",
                                     navigation=[
                                         {'caption': 'Валюты', 'href': '/currencies'},
                                         {'caption': 'Список пользователей', 'href': '/users'}
                                     ],
                                     author_name=main_author.name,
                                     author_group=main_author.group,
                                     currencies=c_r_controller._read()
                                     )
        if self.path == '/users':
            # root url
            global template2

            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = User_cur(User1.group, get_currencies())

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()
            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()
            result = template2.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'основная страница', 'href': '/'},
                                                  {'caption': 'пользователь №1', 'href': '/user1'},
                                                  {'caption': 'пользователь №2', 'href': '/user2'},
                                                  {'caption': 'пользователь №3', 'href': '/user3'}
                                                  ],
                                      # currencies= c_r_controller._read()
                                      )
        if self.path == '/user1':
            # root url
            global template1

            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = User_cur(User1.group, get_currencies())

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()
            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()
            result = template1.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      user_name=User1.name,
                                      group=User1.group,
                                      mail=User1.mail,
                                      phone=User1.phone,
                                      currencies=c_r_controller._read()
                                      )
        if self.path == '/user2':
            # root url
            # global template1
            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = User_cur(User2.group, get_currencies())

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()
            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()
            result = template1.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      user_name=User2.name,
                                      group=User2.group,
                                      mail=User2.mail,
                                      phone=User2.phone,
                                      currencies=c_r_controller._read()
                                      )
        if self.path == '/user3':
            # root url
            #  global template1
            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = User_cur(User3.group, get_currencies())

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()
            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()
            result = template1.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      user_name=User3.name,
                                      group=User3.group,
                                      mail=User3.mail,
                                      phone=User3.phone,
                                      currencies=c_r_controller._read()
                                      )
        if self.path == '/currencies':
            # root url
            global template3

            class CurrencyRatesMock():
                def __init__(self):
                    self.__values = cur()

                @property
                def values(self):
                    return self.__values

            c_r = CurrencyRatesMock()

            c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
            c_r_controller._create()
            result = template3.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      author_name=main_author.name,
                                      author_group=main_author.group,
                                      currencies=c_r_controller._read()
                                      )

        if 'currency/delete' in self.path:
            # print(self.path.rpartition('?')[-1])
            c_r_controller._delete(url_query_dict['id'][0])
            # print(user_params_dict['id'][0])

            # c_r_controller._delete(user_id = )

        if 'currency/show' in self.path:
            print(c_r_controller._read())

        if 'currency/update' in self.path:
            # localhost:8080?usd=100000.100
            if 'usd' or 'USD' in url_query_dict:
                c_r_controller._update({'USD': url_query_dict['usd'][0]})
                result = template.render(result=f'обновление {url_query_dict} завершено')

        self.end_headers()
        # result = "<html><h1>Hello, world!</h1></html>"
        self.wfile.write(bytes(result, "utf-8"))


httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print('server is running')
httpd.serve_forever()
