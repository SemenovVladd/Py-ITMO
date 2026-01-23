import math
import unittest
import timeit
#from Iter23 import integrate2
from Iter5 import integrate5
import Cython
import Iterc
#итерация 1
#Функция вычисляет интегралл заданнй функции в заданном диапазоне


def integrate(f=math.sin, a=5 ,b=4, *, n_iter=10000):
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
#def sum(a=1,b=2):
 #   return a+b
#print(timeit.timeit(sum),1)


print(min(timeit.repeat(integrate, number=100, repeat=5)))
print(min(timeit.repeat(integrate2, number=100, repeat=5)))
print(min(timeit.repeat(iterc, number=100, repeat=5)))
print(min(timeit.repeat(integrate5, number=100, repeat=5)))
# замеряем время выполнения функции с заданными параметрами





#0.28742579999379814
#0.29652280011214316
#
#0.04730423508324927
#0.24608319997787476