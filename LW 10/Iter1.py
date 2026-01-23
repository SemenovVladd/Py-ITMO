import math
import unittest
import timeit


#итерация 1
#Функция вычисляет интегралл заданнй функции в заданном диапазоне


def integrate(f, a, b, *, n_iter=10000):
#  f - функция для которой вычисляем интегралл
#  a, b - диапазон интегрирования
#  n_inter - количество интеграций
    acc=0
    #  счетчик, к которому мы будем прибавлять значения интегралов
    step=(b-a) / n_iter
    #  переменная stp отвечает за ширину прямоугольникам интегрирования
    for i in range(n_iter):
    #  проходимся по всем прямоугольникам интегрирования
        acc += f(a + i*step)*step
    #  высчитывем их площадь и прибовляем к счетчику
    return acc
#  возвращаем сумму

class Tests(unittest.TestCase):
    def test_1(self):
        result=integrate(math.cos, 0, 100)
        self.assertAlmostEqual(result,-0.51, places=2)
    def test_2(self):
        result=integrate(math.sin, 0, 100)
        self.assertAlmostEqual(result,0.14, places=2)
if __name__ == "__main__":
    unittest.main()
#Тесты для проверки работоспособности функции (все работает)
