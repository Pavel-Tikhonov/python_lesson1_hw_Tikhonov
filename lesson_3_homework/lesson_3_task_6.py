# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(word: str):
    """Функция принимает слово из маленьких латинских букв и возвращает его же, но с прописной первой буквой.

    Позиционные параметры:
    :param word: str
    :return word_title: str

    """
    try:
        word_title = word.title()
    except AttributeError as e:
        print(f'Возникла ошибка: {e}.\nВходной аргумент должен являться строкой.')
    else:
        return word_title


print(int_func('word'))

# Часть 2
words = 'example of sentence with words and spaces.'
words_list = words.split(' ')
words_list_title = list(map(int_func, words_list))
space_str = ' '
words_result = space_str.join(words_list_title)
print(words_result)

