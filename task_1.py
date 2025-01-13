# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Book:

    def __init__(self, author: str, pages: int):

        """ Создание и подготовка к работе объекта Book

        :param author: Автор книги
        :param pages: Количество страниц в книге

        Пример:

        >>> book1 = Book('А.С.Пушкин', 500)

        """

        if not isinstance(author, str):

            raise TypeError("Иия автора должно быть типа str")

        if pages <= 0:

            raise ValueError('Количество страниц должно быть целым положительным числом')

        if not isinstance(pages, int):

            raise TypeError('Количетсво страниц должно быть типа int')

        self.author = author
        self.pages = pages

    def author_of_book(self) -> str:

        """ Функция, которая позволяет узнать имя автора

        :return: ФИО автора книги

        >>> book1 = Book('А.С.Пушкин', 500)
        >>> book1_author = book1.author_of_book()

        """

        ...

    def pages_count(self) -> int:

        """ Функция, которая позволяет узнать количество страниц книги

        :return: Количество страниц в книги

        >>> book1 = Book('А.С.Пушкин', 500)
        >>> pagesCountBook1 = book1.pages_count()

        """

        ...

class Student:

    def __init__(self, name: str, group: int, favouriteSubject: str):

        """ Создание и подготовка к работе объекта Student

        :param name: Имя студента
        :param group: Номер учебной группы
        :param favouriteSubject: Любимый предмет ученика

        Пример:

        >>> student1 = Student('Максим', 11, 'Информатика')

        """

        if not isinstance(name, str):

            raise TypeError("Иия студента должно быть типа str")

        if not isinstance(group, int):

            raise TypeError('Номре группы студента должен быть типа int')

        if not isinstance(favouriteSubject, str):

            raise TypeError('Любимый предмет студента должен быть типа str')

        if group < 0:

            raise ValueError('Номер группы студента должен быть положительным числом')

        self.name = name
        self.group = group
        self.favouriteSubject = favouriteSubject

    def getGroupNumber(self) -> int:

        """ Метод, который позволяет узнать номер группы студента

        :return: Номер группы выбранного студента

        >>> student1 = Student('Максим', 11, 'Информатика')
        >>> student1_group = student1.getGroupNumber()

        """

        ...

    def getFavouriteSubject(self) -> str:

        """ Метод, который позволяет узнать любимый предмет выбранного студента

        :return: Любимый предмет выбранного студент

        >>> student1 = Student('Максим', 11, 'Информатика')
        >>> student1_subject = student1.getFavouriteSubject()

        """

        ...

class Worker:

    def __init__(self, name: str, salary: int, job_title: str):

        """ Создание и подготовка к работе объекта Worker

        :param name: Имя работника
        :param salary: Зарплата работника ( тыс.руб. )
        :param job_title: Должность работника

        Пример:

        >>> worker1 = Worker("Максим", 500, "Программист")

        """

        if not isinstance(name, str):
            raise TypeError("Иия работника должно быть типа str")

        if not isinstance(salary, int):
            raise TypeError('Зарплата работника должна быть типа int')

        if not isinstance(job_title, str):
            raise TypeError('Отдел работника должен быть типа str')

        if salary < 0:
            raise ValueError('Зарплата работника должна быть положительным числом')

        self.name = name
        self.salary = salary
        self.job_title = job_title

    def getSalary(self) -> int:

        """ Метод, который позволяет узнать зарплату сотрудника

        :return: Зарплата выбранного сотрудника

        >>> worker1 = Worker('Максим', 500, 'Программист')
        >>> worker1_salary = worker1.getSalary()

        """

        ...

    def getJobTitle(self) -> str:

        """ Метод, который позволяет узнать должность работника

        :return: Должность работника

        >>> worker1 = Worker('Максим', 500, 'Программист')
        >>> worker1_title = worker1.getJobTitle()

        """

        ...

if __name__ == "__main__":

    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()

