"""
Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь,
где ключами являются уникальные слова, а значениями — множества
индексов строк, в которых эти слова встречаются.
"""


def words_index_map(strings: list[str]) -> dict[str, set[int]]:
    """
    Принимает список строк и возвращает словарь, где ключами являются
    уникальные слова, а значениями — множества индексов строк, в которых
    эти слова встречаются.
    Args:
        strings (list[str]): список строк.

    Returns:
        dict: словарь, в котором ключи - уникальные слова,
        а значения множества индексов строк.
    """
    words_count = {}
    for index, value in enumerate(strings):
        for word in value.lower().split():
            if word in words_count:
                words_count[word].add(index)
            else:
                words_count[word] = {index}

    return words_count


"""
Задача 3: Работа с файлами
Напишите программу, которая читает текстовый файл, удаляет из него все
пустые строки и строки, состоящие только из пробелов, а затем
записывает результат в новый файл.
"""


def clean_file(input_file: str, output_file: str) -> None:
    """
    Читает текстовый файл, удаляет пустые строки и строки,
    состоящие только из пробелов, и записывает результат в новый файл.

    Args:
        input_file (str): Имя файла, который нужно обработать (входной файл).
        output_file (str): Имя файла, в который нужно записать
        результат (выходной файл).

    Returns:
        None: Функция ничего не возвращает, результат записывается в указанный
        выходной файл.
    """
    with open(input_file, 'r') as file_with_spaces:
        lines_without_spaces = [
            line for line in file_with_spaces if line.strip()
        ]

    with open(output_file, 'w') as clean_file:
        clean_file.writelines(lines_without_spaces)
