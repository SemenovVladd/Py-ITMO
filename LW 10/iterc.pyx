import cython
cpdef double Iterc(object f ,double a=0 ,double b=100, int n_iter=10000):
#   f - функция для которой вычисляем интегралл
#   a, b - диапазон интегрирования
#   n_inter - количество интеграций
    cdef int acc=0
    #  счетчик, к которому мы будем прибавлять значения интегралов
    cdef double step
    step=(b-a) / n_iter
    #  переменная stp отвечает за ширину прямоугольникам интегрирования
    cdef int i
    for i in range(n_iter):
    #  проходимся по всем прямоугольникам интегрирования
        acc += f(a + i*step)*step
    #  высчитывем их площадь и прибовляем к счетчику
    return acc
#   возвращаем сумму







