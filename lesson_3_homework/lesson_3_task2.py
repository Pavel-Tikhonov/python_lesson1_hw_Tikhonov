# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_info_func(
                u_name='Не было указано',
                u_surname='Не было указано',
                u_birth='Не было указано',
                u_city='Не было указано',
                u_mail='Не было указано',
                u_phone='Не было указано'
                ):
    """Функция реализует вывод данных о пользователе одной строкой.

    Предполагается ввод именованных аргументов:
    :param u_name: str - Имя пользователя
    :param u_surname: str - Фамилия пользователя
    :param u_birth: str - дата рождения
    :param u_city: str - город проживания
    :param u_mail: str - адрес электронной почты
    :param u_phone: str - телефон
    :return user_info_dict: dict - словарь с данными о пользователе

    """
    user_info_dict = {}
    user_info_dict['Имя'] = u_name
    user_info_dict['Фамилия'] = u_surname
    user_info_dict['Дата рождения'] = u_birth
    user_info_dict['Город проживания'] = u_city
    user_info_dict['Электронынй адрес'] = u_mail
    user_info_dict['Телефон'] = u_phone

    print(user_info_dict)


user_info_func(
                u_name='Иван',
                u_surname='Иванов',
                u_birth='16.04.2020',
                u_city='Москва',
                u_mail='12345@mail.ru',
                u_phone='123456789'
                )


