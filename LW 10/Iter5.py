#интерация 5
#Функция вычисляет интегралл заданнй функции в заданном диапазоне
import concurrent.futures as ftres
from functools import partial
import math
from Iter1 import integrate
import Cython
import timeit
#@Cython.nogil
def integrate5(f=math.sin, a=5 ,b=4, *, n_jobs=2, n_iter=10000):
#  f - функция для которой вычисляем интегралл
#  a, b - диапазон интегрирования
#  n_jobs - количество потоков, !надо поэкспеременитровать с потоками!
#  n_inter - количество интеграций

    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)

    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)



    step=(b - a) / n_jobs
    #  переменная stp отвечает за ширину работы каждого потока

  #  for i in range(n_jobs):
    #  проходимся по всем потокам интегрирования
      #  print(f"Работник {i}, границы {a + i * step}, {a + (i + 1) * step}")

    @Cython.nogil
    def f():
        pass
    #отключаем блокирувку многопоточности
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]


    return sum(list(f.result() for f in ftres.as_completed(fs)))

#print(timeit.timeit(integrate5, number=100))

#from Cython.Build import cythonize
#from setuptools import setup
#from Cython.Build import cythonize
#from setuptools.extension import Extension

#setup(
 #   name="iterc",
  #  ext_modules=cythonize("iterc.pyx", annotate=True,
  #                        compiler_directives={"language_level": 3}),
#)