"""
Модуль содержит набор функций
для формирования строк,
представляющих собой регулярные выражения

"""

EMPTY_STRING = ''

class REPR_ENVIRON:
    # следующую переменную необходимо инициализровать
    # при подключении модуля RE выражением вроде
    # [<символы, которые не могут входить в слово>]
    # либо [^<символы, составляющие слова>]
    NON_LETTERS = ''

def cat(*list_of_strings):
    return EMPTY_STRING.join(list_of_strings)

def token(*list_of_strings):
    return r'[%s]' % EMPTY_STRING.join(list_of_strings)

def neg_token(*list_of_strings):
    return r'[^%s]' % EMPTY_STRING.join(list_of_strings)

def left_context(*list_of_strings):
    return r'(?<=%s)' % EMPTY_STRING.join(list_of_strings)

def neg_left_context(*list_of_strings):
    return '(?<!%s)' % EMPTY_STRING.join(list_of_strings)

def right_context(*list_of_strings):
    return r'(?=%s)' % EMPTY_STRING.join(list_of_strings)

def neg_right_context(*list_of_strings):
    return '(?!%s)' % EMPTY_STRING.join(list_of_strings)

def initial(*list_of_strings):
    x = cat(*list_of_strings)
    return '((^%s)|(%s%s))' % (x, REPR_ENVIRON.NON_LETTERS, x)

def initial_context(*list_of_strings):
    x = cat(*list_of_strings)
    return '((?<=^%s)|(?<=%s%s))' % (x, REPR_ENVIRON.NON_LETTERS, x)
