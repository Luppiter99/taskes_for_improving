"""
Задача 1: Реверсирование строки
Напишите функцию, которая принимает строку и возвращает её,
но со словами в обратном порядке.
"""


def reverse_string(string: str) -> str:
    """
        Возвращает строку, в которой слова идут в обратном порядке.

        Args:
            string (str): Любая строка.

        Returns:
            str: Строка в обратном порядке.
        """
    reversed_string = ''.join(reversed(string.split()))
    return reversed_string


"""
Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются символы, а значениями — их частота в строке.
"""


def count_symbols(string: str) -> dict:
    """

    Создает словарь, который подсчитывает количество повторений
    каждого символа в строке

    Args:
        string (str): Любая строка.

    Returns:
        dict: Словарь, где ключи - символы в строке,
        а значения - сколько раз этот символ встречается в этой строке
    """
    counting = {}
    for char in string:
        if char in counting:
            counting[char] += 1
        else:
            counting[char] = 1
    return counting


"""
Задача 4: Проверка анаграммы
Напишите функцию, которая принимает две строки и проверяет,
являются ли они анаграммами (т.е. состоят ли они из одних и тех же
символов в одинаковом количестве).
"""


def are_anagrams(word1: str, word2: str) -> bool:
    """
    Проверяет, являются ли две строки анаграммами.

    Для каждой строки создается словарь, где ключи — символы строки,
    а значения — количество их вхождений. Если словари одинаковы,
    строки являются анаграммами.
    Args:
        word1 (str): первая проверяемая строка.
        word2 (str): вторая проверяемая строка.

    Returns:
        bool: True, если строки являются анаграммами, иначе False.
    """
    symbols_in_word1 = {}
    symbols_in_word2 = {}

    for char in word1:
        if char in symbols_in_word1:
            symbols_in_word1[char] += 1
        else:
            symbols_in_word1[char] = 1

    for char in word2:
        if char in symbols_in_word2:
            symbols_in_word2[char] += 1
        else:
            symbols_in_word2[char] = 1

    return symbols_in_word1 == symbols_in_word2


"""
Задача 2: Максимальная сумма подмассива
Напишите функцию, которая принимает список чисел и возвращает
максимальную сумму подмассива.
"""


def max_subarray_sum(array: list[int]) -> int:
    """
    Возвращает максимальную сумму подмассива в списке чисел.

    Использует алгоритм Кадане для нахождения максимальной суммы подмассива
    за линейное время. Подмассив должен содержать хотя бы один элемент.
    Args:
        array (list[int]): список чисел.

    Returns:
        int: максимальная сумма подмассива.
    """
    max_sum = float('-inf')
    cur_sum = 0
    for num in array:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)

        if cur_sum < 0:
            cur_sum = 0

    return max_sum
