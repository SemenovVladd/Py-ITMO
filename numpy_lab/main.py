import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector():
    """
    Returns:
        numpy.ndarray: Массив чисел от 0 до 9 включительно
    """
    return np.arange(10)


def create_matrix():
    """
    Returns:
        numpy.ndarray: Матрица 5x5 со случайными значениями от 0 до 1
    """
    return np.random.rand(5, 5)


def reshape_vector(vec):
    """
    Args:
        vec (numpy.ndarray): Входной массив формы (10,)

    Returns:
        numpy.ndarray: Преобразованный массив формы (2, 5)
    """
    return vec.reshape(2, 5)


def transpose_matrix(mat):
    """
    Args:
        mat (numpy.ndarray): Входная матрица

    Returns:
        numpy.ndarray: Транспонированная матрица
    """
    return mat.T


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================

def vector_add(a, b):
    """
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор

    Returns:
        numpy.ndarray: Результат поэлементного сложения
    """
    return a + b
    pass


def scalar_multiply(vec, scalar):
    """
    Args:
        vec (numpy.ndarray): Входной вектор
        scalar (float/int): Число для умножения

    Returns:
        numpy.ndarray: Результат умножения вектора на скаляр
    """
    return vec * scalar


def elementwise_multiply(a, b):
    """
    Args:
        a (numpy.ndarray): Первый вектор/матрица
        b (numpy.ndarray): Второй вектор/матрица

    Returns:
        numpy.ndarray: Результат поэлементного умножения
    """
    return a * b


def dot_product(a, b):
    """
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор

    Returns:
        float: Скалярное произведение векторов
    """
    return np.dot(a, b)


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

def matrix_multiply(a, b):
    """
    Args:
        a (numpy.ndarray): Первая матрица
        b (numpy.ndarray): Вторая матрица

    Returns:
        numpy.ndarray: Результат умножения матриц
    """
    return a @ b
    pass


def matrix_determinant(a):
    """
    Args:
        a (numpy.ndarray): Квадратная матрица

    Returns:
        float: Определитель матрицы
    """
    return np.linalg.det(a)


def matrix_inverse(a):
    """
    Args:
        a (numpy.ndarray): Квадратная матрица

    Returns:
        numpy.ndarray: Обратная матрица
    """
    return np.linalg.inv(a)


def solve_linear_system(a, b):
    """
    Args:
        a (numpy.ndarray): Матрица коэффициентов A
        b (numpy.ndarray): Вектор свободных членов b

    Returns:
        numpy.ndarray: Решение системы x
    """
    return np.linalg.solve(a, b)


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path="data/students_scores.csv"):
    """
    Args:
        path (str): Путь к CSV файлу

    Returns:
        numpy.ndarray: Загруженные данные в виде массива
    """
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data):
    """
    Представьте, что данные — это результаты экзамена по математике.
    Нужно оценить:
    - средний балл
    - медиану
    - стандартное отклонение
    - минимум
    - максимум
    - 25 и 75 перцентили

    Args:
        data (numpy.ndarray): Одномерный массив данных

    Returns:
        dict: Словарь со статистическими показателями
    """
    result = {'mean': np.mean(data), 'медиана': np.median(data),
              'стандартное отклонение': np.std(data), 'min': np.min(data),
              'max': np.max(data), '25 перцентили': np.percentile(data, 25),
              '75 перцентили': np.percentile(data, 75)}
    return result


def normalize_data(data):
    """
    Args:
        data (numpy.ndarray): Входной массив данных

    Returns:
        numpy.ndarray: Нормализованный массив данных в диапазоне [0, 1]
    """
    min_data = np.min(data)
    max_data = np.max(data)

    normalized_data = (data - min_data) / (max_data - min_data)

    return normalized_data


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_histogram(data):
    """
    Построить гистограмму распределения оценок по математике.

    Args:
        data (numpy.ndarray): Данные для гистограммы
    """

    plt.figure(figsize=(10, 6))

    plt.title('Распределение оценок по математике', fontsize=16)

    plt.xticks([1, 2, 3, 4, 5], fontsize=11)

    plt.xlabel('Оценки', fontsize=12)
    plt.ylabel('Частота', fontsize=12)

    plt.savefig('plots/histogram.png')

    plt.show()


def plot_heatmap(matrix):
    """
    Построить тепловую карту корреляции предметов.

    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """
    os.makedirs('plots', exist_ok=True)

    plt.figure(figsize=(10, 8))

    heatmap = sns.heatmap(
        matrix,
        annot=True,  # показывать значения
        center=0,  # центр шкалы (для корреляции - 0)
        cbar_kws={'shrink': 0.8, 'label': 'Коэффициент корреляции'},  # настройки цветовой шкалы
        vmin=-1, vmax=1  # диапазон корреляции от -1 до 1
    )

    plt.title('Тепловая карта корреляции предметов')

    plt.savefig('plots/heatmap.png')

    plt.show()


def plot_line(x, y):
    """
    Построить график зависимости: студент -> оценка по математике.

    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """

    plt.figure(figsize=(12, 6))

    plt.plot(x, y, label='Оценки по математике')

    plt.title('Зависимость оценки по математике от номера студента')

    plt.xlabel('Номер студента')
    plt.ylabel('Оценка по математике')

    plt.xticks(x)
    plt.yticks(np.arange(2, 6, 0.5))  # оценки от 2 до 5 с шагом 0.5

    plt.xlim(min(x) - 0.5, max(x) + 0.5)
    plt.ylim(1.5, 5.5)

    plt.legend(loc='best', fontsize=10)

    plt.tight_layout()

    plt.savefig('plots/line_plot.png', dpi=300, bbox_inches='tight')

    plt.show()
