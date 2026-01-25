from typing import Callable
#импортируем функции ввиде типов
def gen_bin_tree (root:int, height: int,
                  l: callable, r: callable) -> dict:
    """
    :param root: изначальный корень
    :param height: высота дерева
    :param l: lambda - функция для вычисления левого потомка
    :param r:lambda - функция для вычисления правого потомка
    :return: на выходе получаем словарь
    """

    if height == 1:
        return {str(root): []}
    #если высота равна 1, возращаем список из корня и массива
    return {str(root) : [gen_bin_tree(l(root), height-1,l,r),
                         gen_bin_tree(l(root), height-1,l,r)]}
    #возращаем для каждого корня левого и правого потомка
print(gen_bin_tree(18,5, lambda x: (x-8)*3, lambda x: (x+8)*2))
# выводим значние функии, для моего варианта