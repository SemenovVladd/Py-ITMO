import matplotlib as plt
from gen_bin_tree1 import gen_bin_tree1
from gen_bin_tree2 import gen_bin_tree2
import timeit
def time_func(func, n, repeats=5):
    #функиця для измерения времени выполнения другой функции
    """"
    :param func: сама функция, которую будем тестировать
    :param n: значение, которое принимает функция func
    :param repeats: количество повторений
    """
    if func == gen_bin_tree2:
        timer = timeit.Timer(lambda: func(n, 18, lambda x: (x - 8) * 3, lambda x: (x + 8) * 2))
    if func == gen_bin_tree1:
        timer = timeit.Timer(lambda: func(18, n, lambda x: (x - 8) * 3, lambda x: (x + 8) * 2))
    #объект таймера, который принимает функцию с числом внутри нее(для этого использовал lambda, иначе не работало)
    #тут 2 разных объекта, т.к. изначально перепутал высоту и корень у первой функции
    times = timer.repeat(repeat=repeats, number=10)
    #измеряем время
    return (times[repeats//2+1])
    # возвращаем среднее время среди 5 (в данном случае) больших повторений





max_n = 10
#до какой высоты будем строить дерево
t_tree_rec = []
#массив для время функции через рекурсию
t_tree_not_rec = []
#массив для время функции без рекурсии

for n in range(1,max_n):
    #проходимся по значениям от 1 до 10
    t = time_func(gen_bin_tree1, n)
    t_tree_rec.append(t)
    #вычисляем время и записываем в массив

    t = time_func(gen_bin_tree2, n)
    t_tree_not_rec.append(t)
    #вычисляем время и записываем в массив


#построение графика
plt.figure(figsize=(8, 6))
plt.plot(t_tree_rec, label="fact_rec")
plt.plot(t_tree_not_rec, label="fact_not_rec")
#строим сами графики
plt.xlabel("высота дерева")
plt.ylabel("Время выполнения функции")
#подписываем их
plt.title("Сравнение времени построения деревьев")
#называем сам плот
plt.legend()
#добавляем легенду
plt.grid(True)
#сетка для наглядности
plt.tight_layout()
plt.show()