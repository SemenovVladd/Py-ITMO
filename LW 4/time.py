import timeit
import matplotlib.pyplot as plt
from fact_rec import fact_rec
from fact_not_rec import fact_not_rec
def time_func(func, n, repeats=5):
    #функиця для измерения времени выполнения другой функции
    """"
    :param func: сама функция, которую будем тестировать
    :param n: значение, которое принимает функция func
    :param repeats: количество повторений
    """

    timer = timeit.Timer(lambda: func(n))
    # объект таймера, который принимает функцию с числом внутри нее(для этого использовал lambda, иначе не работало)
    times = timer.repeat(repeat=repeats, number=1000)
    #измеряем время
    return (times[repeats//2+1])
    # возвращаем среднее время среди 5 (в данном случае) больших повторений


max_n = 200
#до какого числа будем измерять факториал
t_fact_rec = []
#массив для время функции через рекурсию
t_fact_not_rec = []
#массив для время функции без рекурсии

for n in range(max_n):
    #проходимся по значениям от 1 до 200
    t = time_func(fact_rec, n)
    t_fact_rec.append(t)
    #вычисляем время и записываем в массив

    t = time_func(fact_not_rec, n)
    t_fact_not_rec.append(t)
    #вычисляем время и записываем в массив


# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(t_fact_rec, label="fact_rec")
plt.plot(t_fact_not_rec, label="fact_not_rec")
#строим сами графики
plt.xlabel("n")
plt.ylabel("Время выполнения функции")
#подписываем их
plt.title("Сравнение времени вычисления факториала")
#называем сам плот
plt.legend()
#добавляем легенду
plt.grid(True)
#сетка для наглядности
plt.tight_layout()
plt.show()

print(time_func(fact_rec, 150))
#пример для конкретного значения (0.0003863000001729233)
print(time_func(fact_not_rec, 150))
#пример для конкретного значения (0.016563700000006065)