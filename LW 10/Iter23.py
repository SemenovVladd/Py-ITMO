#итерация 2
#Функция вычисляет интегралл заданнй функции в заданном диапазоне
import concurrent.futures as ftres
from functools import partial
import math
from Iter1 import integrate
from typing import Callable
import timeit
def integrate2(f=math.sin, a=5, b=4,
               *, n_jobs=2, n_iter=10000):
#  f - функция для которой вычисляем интегралл
#  a, b - диапазон интегрирования
#  n_jobs - количество потоков, !надо поэкспеременитровать с потоками!
#  n_inter - количество интеграций

    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)



    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)             ###################

    step=(b - a) / n_jobs
    #  переменная stp отвечает за ширину работы каждого потока

 #   for i in range(n_jobs):
    #  проходимся по всем потокам интегрирования
       # print(f"Работник {i}, границы {a + i * step}, {a + (i + 1) * step}")

    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]


    return sum(list(f.result() for f in ftres.as_completed(fs)))
#  возвращаем сумму

print(timeit.timeit(integrate2, number=100))
#итерация 3
#Функция вычисляет интегралл заданнй функции в заданном диапазоне

def integrate3(f, a, b,
               *, n_jobs=4, n_iter=10000):
#  f - функция для которой вычисляем интегралл
#  a, b - диапазон интегрирования
#  n_jobs - количество потоков, !надо поэкспеременитровать с процесами!
#  n_inter - количество интеграций

    executor = ftres.ProcessPoolExecutor(max_workers=n_jobs)

    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)      ###########################



    step=(b - a) / n_jobs
    #  переменная stp отвечает за ширину работы каждого потока

    for i in range(n_jobs):
    #  проходимся по всем потокам интегрирования
        print(f"Работник {i}, границы {a + i * step}, {a + (i + 1) * step}")

    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
   # print(fs,12324355254253245245245)


    return sum(list(f.result() for f in ftres.as_completed(fs)))
#  возвращаем сумму

#print(integrate3(math.cos, 0, math.pi))



































def testF(x: float) -> float:
    """
    Simple linear test function for
    benchmarking integration.

    Args:
        x (float): Input value

    Returns:
        float: x + 1
    """
    return x + 1

def integrate33(func: Callable[[float], float],
                          start: float,
                          end: float,
                          *,
                          steps: int = 1000,
                          jobs: int = 2) -> float:







    with ftres.ProcessPoolExecutor(max_workers=jobs) as executor:
        threadStart = partial(executor.submit, integrate, func, steps=steps)

        step = (end - start) / jobs
        results = [threadStart(start + i * step, start + (i + 1) * step)
                   for i in range(jobs)]
        return sum([i.result() for i in ftres.as_completed(results)])


print(timeit.repeat(lambda: integrate33(testF, 1.0, 100.0),
                            number=1000, repeat=5))








