from queue import Queue
def gen_bin_tree2(height: int, root: int,
                  left_branch: callable,
                  right_branch: callable):
    """
    :param root: изначальный корень
    :param height: высота дерева
    :param left_branch: lambda - функция для вычисления левого потомка
    :param right_branch:lambda - функция для вычисления правого потомка
    :return: на выходе получаем словарь
    """

    res = {str(root): []}
    # создаем начальный словарик
    q = Queue()
    # создаем очередь
    q.put((res, 0))
    # в очередь помещаем изначальные значаения (корень + высота)

    while not q.empty():
        now_node, now_height = q.get()
        # получаем значение текущего узла и высоту
        if now_height >= height:
            continue
        # если не достигли максимальной высоты, продолжаем (считаем, корень == 1 высоте)
        current_key = list(now_node.keys())[0]
        # получаем ключ узла
        left_value = left_branch(int(current_key))
        right_value = right_branch(int(current_key))
        # вычисляем значения левого и правого потомка
        left_child = {str(left_value): []}
        right_child = {str(right_value): []}
        # Создаем новые узлы
        now_node[current_key].append(left_child)
        now_node[current_key].append(right_child)
        # добавляем потомков к рассматриваемому узлу
        q.put((left_child, now_height + 1))
        q.put((right_child, now_height + 1))
        # и отправляем их в очередь с высотой + 1

    return res
    # возращаем результат
