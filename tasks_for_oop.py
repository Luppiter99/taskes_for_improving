"""
Задача 1: Создание библиотеки
Создайте библиотеку для управления коллекцией книг. Каждая книга
должна быть представлена как объект, содержащий атрибуты: название,
автор, год издания, жанр и количество страниц. Библиотека должна поддерживать
следующие операции:
1. Добавление книги.
2. Удаление книги.
3. Поиск книги по названию.
4. Вывод всех книг одного автора.
5. Вывод всех книг, отсортированных по году издания.
"""


class Book:
    """
    Класс для представления книги с атрибутами:
    - название,
    - автор,
    - год издания,
    - жанр,
    - количество страниц.
    Все атрибуты проверяются на корректность с помощью свойств (property).
    """

    def __init__(self, name: str, author: str, year: int,
                 genre: str, pages: int) -> None:
        """
        Инициализирует объект книги с основными атрибутами.

        Args:
            name (str): Название книги.
            author (str): Имя автора книги.
            year (int): Год издания книги.
            genre (str): Жанр книги.
            pages (int): Количество страниц в книге.
        """
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @name.setter
    def name(self, book_name: str) -> None:
        """Устанавливает название книги с проверкой на пустую строку."""
        if not book_name:
            raise ValueError('Название книги не может быть пустым')
        self._name = book_name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    @author.setter
    def author(self, author_name: str) -> None:
        """Устанавливает имя автора с проверкой на пустую строку."""
        if not author_name:
            raise ValueError('Имя автора не может быть пустым')
        self._author = author_name

    @property
    def year(self) -> int:
        """Возвращает год издания книги."""
        return self._year

    @year.setter
    def year(self, published_year: int) -> None:
        """Устанавливает год издания книги с проверкой на
        положительное значение."""
        if published_year < 0:
            raise ValueError('Год не может быть отрицательным числом')
        self._year = published_year

    @property
    def genre(self) -> str:
        """Возвращает жанр книги."""
        return self._genre

    @genre.setter
    def genre(self, genre_category: str) -> None:
        """Устанавливает жанр книги с проверкой на пустую строку."""
        if not genre_category:
            raise ValueError('Жанр не может быть пустой строкой')
        self._genre = genre_category

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, page_count: int) -> None:
        """Устанавливает количество страниц с проверкой на
        положительное значение."""
        if page_count < 0:
            raise ValueError('Количество страниц не может быть отрицательным')
        self._pages = page_count

    def __eq__(self, value: object) -> bool:
        """
        Сравнивает книги по названию, автору и году издания.

        Args:
            value (object): Книга для сравнения.

        Returns:
            bool: True, если книги совпадают, иначе False.
        """
        if isinstance(value, Book):
            return (
                self.name == value.name and
                self.author == value.author and
                self.year == value.year)
        return NotImplemented

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return (f'Книга - {self.name}, автор - {self.author}, '
                f'год выпуска - {self.year}')


class Library:
    """
    Класс для управления коллекцией книг.
    Позволяет добавлять, удалять книги, искать их по названию, автору и
    сортировать по году издания.
    """

    def __init__(self) -> None:
        """
        Инициализирует объект библиотеки с пустой коллекцией книг.
        """
        self.book_collection: list[Book] = []

    def add_book(self, book: Book) -> str:
        """
        Добавляет книгу в библиотеку.

        Args:
            book (Book): Объект книги для добавления.

        Returns:
            str: Сообщение об успешном добавлении книги.
        """
        if isinstance(book, Book):
            self.book_collection.append(book)
            return f'Книга "{book.name}" успешно добавлена в библиотеку!'
        raise TypeError(
            f'Объект {book} не является экземпляром класса Book.'
            'Убедитесь, что вы передаете корректный объект книги.')

    def remove_book(self, book: Book) -> str:
        """
        Удаляет все экземпляры указанной книги из библиотеки.

        Args:
            book (Book): Книга для удаления.

        Returns:
            str: Сообщение об успешном удалении книги.

        Raises:
            ValueError: Если книга не найдена в библиотеке.
        """
        if book in self.book_collection:
            for num in range(len(self.book_collection) - 1, -1, -1):
                if self.book_collection[num] == book:
                    del self.book_collection[num]
            return (f'Все экземпляры книги "{book.name}" успешно '
                    'удалены из библиотеки!')
        raise ValueError(f'Книга "{book}" не найдена в библиотеке')

    def search_by_title(self, book_name: str) -> Book | str:
        """
        Ищет книгу по названию.

        Args:
            book_name (str): Название книги для поиска.

        Returns:
            Book | str: Объект книги, если найден,
            или сообщение о её отсутствии.
        """
        for book in self.book_collection:
            if book.name.lower() == book_name.lower():
                return book
        return f'Книга "{book_name}" не найдена!'

    def get_books_by_author(self, author: str) -> list[Book] | str:
        """
        Возвращает список книг указанного автора.

        Args:
            author (str): Имя автора для поиска.

        Returns:
            list[Book] | str: Список книг автора или сообщение о ненахождении.
        """
        books_by_author = [
            book for book in self.book_collection
            if book.author.lower() == author.lower()
        ]
        if books_by_author:
            return books_by_author
        return f'Книги автора "{author}" не найдены в библиотеке'

    def sort_books_by_year(self) -> list[Book]:
        """
        Возвращает список книг, отсортированных по году издания.

        Returns:
            list[Book]: Список книг,
            отсортированных по возрастанию года издания.
        """
        sorted_books = sorted(self.book_collection, key=lambda book: book.year)
        return sorted_books


"""
Задача 2: Создание банковской системы
Создайте систему для управления банковскими счетами. У каждого счета
должны быть атрибуты: номер счета, имя владельца, баланс.
Система должна поддерживать следующие операции:
1. Депозит средств.
2. Снятие средств.
3. Проверка баланса.
4. Перевод средств с одного счета на другой.
Используйте магические методы для вывода информации о счете и для
проверки равенства счетов (например, по номеру счета).
"""


class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
        account_numbers (set): множество всех номеров счетов для
        проверки уникальности.
        number (str): номер счета.
        owner (str): имя владельца счета.
        balance (float): текущий баланс счета.
    """
    account_numbers = set()

    def __init__(self, number: str, owner: str, balance: float = 0.0) -> None:
        """
        Инициализирует объект банковского счета с заданными номером,
        владельцем и балансом.

        Args:
            number (str): номер счета.
            owner (str): имя владельца счета.
            balance (float, optional): начальный баланс счета.
            По умолчанию 0.0.

        Raises:
            ValueError: если номер счета уже используется или баланс
            отрицательный.
        """
        if number in BankAccount.account_numbers:
            raise ValueError('Этот номер счёта уже используется.')
        self.number = number
        self.owner = owner
        self.balance = balance
        BankAccount.account_numbers.add(number)

    @property
    def balance(self) -> float:
        """float: Возвращает текущий баланс счета."""
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        """
        Устанавливает новый баланс счета.

        Args:
            amount (float): сумма для установки баланса.

        Raises:
            ValueError: если сумма отрицательная.
        """
        if amount < 0.0:
            raise ValueError('Баланс не может быть отрицательным')
        self._balance = amount

    def deposit(self, dep_sum: float) -> None:
        """
        Вносит средства на счет.

        Args:
            dep_sum (float): сумма для внесения на счет.

        Raises:
            ValueError: если сумма пополнения неположительная.
        """
        if dep_sum <= 0.0:
            raise ValueError(
                'Сумма пополнения должна быть положительным числом'
                )
        self.balance += dep_sum

    def withdraw(self, amount: float) -> None:
        """
        Снимает средства со счета.

        Args:
            amount (float): сумма для снятия со счета.

        Raises:
            ValueError: если сумма снятия неположительная или превышает баланс.
        """
        if amount <= 0.0:
            raise ValueError('Сумма снятия должна быть положительным числом')
        if amount > self.balance:
            raise ValueError('Сумма снятия превышает баланс счета')
        self.balance -= amount

    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух счетов по номеру счета.

        Args:
            other (object): другой объект для сравнения.

        Returns:
            bool: True, если счета равны, иначе False.
        """
        if isinstance(other, BankAccount):
            return self.number == other.number
        return False

    def __str__(self) -> str:
        """
        Возвращает строковое представление счета.

        Returns:
            str: строковое представление счета.
        """
        return f'Счёт {self.number}: Владелец {self.owner}'


class BankSystem:
    """
    Класс, представляющий банковскую систему для управления счетами.

    Атрибуты:
        bank_accounts (dict): словарь счетов с номером счета в качестве ключа.
    """

    def __init__(self) -> None:
        """Инициализирует банковскую систему с пустым списком счетов."""
        self.bank_accounts = {}

    def add_account(self, account: BankAccount) -> None:
        """
        Добавляет счет в банковскую систему.

        Args:
            account (BankAccount): счет для добавления.

        Raises:
            ValueError: если счет уже добавлен в систему.
        """
        if account.number in self.bank_accounts:
            raise ValueError(f'Счёт {account.number} уже добавлен в систему')
        self.bank_accounts[account.number] = account

    def check_balance(self, account_number: str) -> float:
        """
        Проверяет баланс счета по его номеру.

        Args:
            account_number (str): номер счета.

        Returns:
            float: текущий баланс счета.

        Raises:
            ValueError: если счет не найден в системе.
        """
        if account_number in self.bank_accounts:
            return self.bank_accounts[account_number].balance
        raise ValueError(f'Счёта {account_number} нет в банковской системе')

    def transfer(self, acc_from: str, acc_to: str, amount: float) -> None:
        """
        Переводит средства с одного счета на другой.

        Args:
            acc_from (str): номер счета отправителя.
            acc_to (str): номер счета получателя.
            amount (float): сумма для перевода.

        Raises:
            ValueError: если сумма перевода неположительная или счета
            не найдены.
        """
        if amount <= 0.0:
            raise ValueError('Сумма перевода должна быть положительным числом')
        if acc_from not in self.bank_accounts:
            raise ValueError(f'Счёт отправителя {acc_from} не найден.')
        if acc_to not in self.bank_accounts:
            raise ValueError(f'Счёт получателя {acc_to} не найден.')
        self.bank_accounts[acc_from].withdraw(amount)
        self.bank_accounts[acc_to].deposit(amount)
