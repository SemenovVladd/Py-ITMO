from jinja2 import Environment, PackageLoader, select_autoescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from controllers.databasecontroller import CurrencyRatesCRUD
from controllers.Users_controller import UsersCRUD
from Models import Author
from Models import User
from Models import User_cur
from Models import cur
from utils import get_currencies

from controllers import databasecontroller
from controllers import Users_controller

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)



main_author = Author('Vlad', 'P3124')

template = env.get_template("index.html")
template1 = env.get_template("users.html")
template2 = env.get_template("Userss.html")
template3 = env.get_template("currencies.html")
template4 = env.get_template("for_users.html")
User1 = User('Vlad', 'USD', 'yandex', '5555555555')
User2 = User('Peter', 'USD,EUR', 'goggle', '66666666666')
User3 = User('Ivan', 'USD,AUD', 'mail', '77777777777')

class CurrencyRatesMockU():
    def __init__(self):
        self.__values = [('Vlad', 'USD', 'yandex', '5555555555'),
                         ('Peter', 'USD,EUR', 'goggle', '66666666666'),
                         ('Ivan', 'USD,AUD', 'mail', '77777777777')]

    @property
    def values(self):
        return self.__values

users = CurrencyRatesMockU()

controlleru = Users_controller.UsersCRUD(users)
controlleru._createu()




class CurrencyRatesMock():
    def __init__(self):
        self.__values = cur()

    @property
    def values(self):
        return self.__values


c_r = CurrencyRatesMock()

c_r_controller = databasecontroller.CurrencyRatesCRUD(c_r)
c_r_controller._create()





class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global template
        global template1
        global template2
        global template3

        global c_r_controller
        global controlleru





        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        print(self.path)
        url_query_dict = parse_qs(self.path.rpartition('?')[-1])
        if self.path == '/':




            result = template.render(myapp="CurrenciesListApp",
                                     navigation=[
                                         {'caption': 'Валюты', 'href': '/currencies'},
                                         {'caption': 'Список пользователей', 'href': '/users'}
                                     ],
                                     author_name=main_author.name,
                                     author_group=main_author.group,
                                     currencies=(controlleru._readu())
                                     )

        if self.path == '/now_users':
            print(controlleru._readu())


            # root url

            result = template4.render(myapp="CurrenciesListApp",
                                     navigation=[
                                         {'caption': 'Валюты', 'href': '/currencies'},
                                         {'caption': 'Список пользователей', 'href': '/users'}
                                     ],
                                     author_name=main_author.name,
                                     author_group=main_author.group,
                                     currencies=controlleru._readu()
                                     )




#################
        if self.path == '/users':

            result = template2.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'основная страница', 'href': '/'},
                                                  {'caption': 'пользователь №1', 'href': '/user?id=1'},
                                                  {'caption': 'пользователь №2', 'href': '/user?id=2'},
                                                  {'caption': 'пользователь №3', 'href': '/user?id=3'}
                                                  ],
                                      )



        if 'user?' in self.path:
            User=controlleru.get_row_by_id(self.path.rpartition('?')[-1][-1])
            k = []
            for i in User_cur(User[2], get_currencies()):
                c_r_controller.get_row_by_id(i[0])
                k.append(c_r_controller.get_row_by_id(i[0]))

            result = template1.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      user_name=User[1],
                                      group=User[2],
                                      mail=User[3],
                                      phone=User[4],
                                      currencies=k
                                      )


        if self.path == '/currencies':
            result = template3.render(myapp="CurrenciesListApp",
                                      navigation=[{'caption': 'Основная страница',
                                                   'href': "/"},
                                                  ],
                                      author_name=main_author.name,
                                      author_group=main_author.group,
                                      currencies=c_r_controller._read()
                                      )

        if 'currency/delete' in self.path:
            print(self.path.rpartition('?')[-1])
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
      #  print(3, controlleru._readu()[1])


httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print('server is running')
httpd.serve_forever()

