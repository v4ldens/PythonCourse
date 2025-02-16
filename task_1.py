from datetime import datetime
import doctest

if __name__ == "__main__":

    class Business:

        def __init__(self, owner: str, organization_form: str, foundation_date: int):

            """ Создание и подготовка к работе объекта Book

            :param owner: Владелец бизнеса
            :param organization_form: Форма организации
            :param foundation_date: Дата основания

            Пример

            >>> owner_1 = Business('Иван', 'АО', 2010)

            """

            self.owner = owner
            self.foundation_date = foundation_date

            organization_forms = ['ИП', 'ООО', 'ЗАО', 'АО']

            if organization_form not in organization_forms:

                raise ValueError('Укажите корректную форму организации (ООО, ИП, ЗАО, АО)')

            self.organization_form = organization_form

        def __str__(self) -> str:

            """ Метод, позволяющий узнать информацию об атрибутах объектах класса

            :return: Информация об объекте класса

            >>> owner_1 = Business('Иван', 'АО', 2010)
            >>> print(owner_1)

            """

            return f'Владелец: {self.owner}, форма организации: {self.organization_form}, дата основания: {self.foundation_date}'

        def __repr__(self) -> str:

            """ Метод, позволяющий получить валидную python-строку, по которой можно проинициализировать точно такой же объект

            :return: валидная python-строка с информацией об объекте класса

            """

            return f"{self.__class__.__name__}(owner={self.owner!r}, organization_form={self.organization_form!r}, foundation_date={self.foundation_date!r})"

        def years_of_existence(self) -> int:

            """ Метод, позволяющий узнать, сколько лет бизнесу с момента основания

            :return: Количество лет, прошедшее с года основания

            >>> owner_1 = Business('Иван', 'АО', 2010)
            >>> print(owner_1.years_of_existence())

            """

            return datetime.now().year - self.foundation_date

        def business_owner(self) -> str:

            """ Метод, позволяющий узнать, кто владелец бизнеса

            :return: Имя владельца бизнеса

            >>> owner_1 = Business('Иван', 'АО', 2010)
            >>> print(owner_1.business_owner())

            """

            return f'Владелец бизнеса: {self.owner}'

    class Restaurant(Business):

        """ Подкласс класса Business для ресторанного дела """

        def __init__(self, owner: str, organization_form: str, foundation_date: int, number_of_restaurants: int):
            """ Создание и подготовка к работе объекта Book

            :param owner: Владелец бизнеса
            :param organization_form: Форма организации
            :param foundation_date: Дата основания
            :param number_of_restaurants: Количество ресторанов в данной сети

            Пример

            >>> owner_1 = Business('Иван', 'АО', 2010, 10)

            """

            super().__init__(owner, organization_form, foundation_date)

            if not isinstance(number_of_restaurants, int) or (number_of_restaurants < 0):
                raise TypeError('Количество ресторанов должно быть целым неотрицательным числом')

            self.number_of_restaurants = number_of_restaurants

        def __str__(self) -> str:

            """ Метод, позволяющий узнать информацию об атрибутах объектах класса

            Метод перегружен, так как у подкласса добавлен новый атрибут number_of_restaraunts

            :return: Информация об объекте класса

            >>> owner_1 = Business('Иван', 'АО', 2010, 10)
            >>> print(owner_1)

            """

            return f'Владелец: {self.owner}, форма организации: {self.organization_form}, дата основания: {self.foundation_date}, количество ресторанов: {self.number_of_restaurants}'

        def __repr__(self) -> str:

            """ Метод, позволяющий получить валидную python-строку, по которой можно проинициализировать точно такой же объект

            Метод перегружен, так как у подкласса добавлен новый атрибут number_of_restaraunts

            :return: валидная python-строка с информацией об объекте класса

            """

            return f"{self.__class__.__name__}(owner={self.owner!r}, organization_form={self.organization_form!r}, foundation_date={self.foundation_date!r}), number_of_restaurants={self.number_of_restaurants!r}"

        def business_owner(self) -> str:

            """ Метод, позволяющий узнать, кто владелец бизнеса

            Метод перегружен для уточнения типа бизнеса (в данном случае, сеть ресторанов)

            :return: Имя владельца бизнеса

            """

            return f'Владелец данной сети ресторанов: {self.owner}'

