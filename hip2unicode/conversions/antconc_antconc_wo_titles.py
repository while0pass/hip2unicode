"""
Раскрытие титл для кодировки АнтКонк.

Подразумевается, что в тексте для перекодирования не будут втречаться слова,
состоящие только из заглавных букв. А также, что заглавные буквы будут
встречаться только на месте титл. Иначе конвертация не будет правильной.

Также подразумевается, что на вход будет подаваться не текст, а отдельное
слово.

"""

from hip2unicode.representations.RE import *
from hip2unicode.representations.antconc import *

conversion = (
    ('апСтл',  "апо'стол"),
    ('апСл',   "апо'стол"),
    ('апС',    "апо'с"),  # апостол...
    ('бг~мт~', "богома'т"),
    ('бг~',    'бог'),
    ('бж~тв',  'божеств'),
    ('бж~',    "бо'ж"),
    ('бжСтв',  'божеств'),
    ('бз~',    "бо'з"),
    ('бл~г',   'благ'),
    ('бл~ж',   'блаж'),
    ('бл~з',   'блаз'),
    ('блГв',   'благов'),
    ('блгДт',  "благода'т"),
    ('блгСв',  'благослов'),
    ('блгСл',  'благосл'),
    ('блгС',   'благос'),
    ('бцД',    "богоро'диц"),
    ('влДк',   "влады'к"),
    ('влДца',  "влады'чица"),
    ('влДцѣ',  "влады'цѣ"),
    ('влДце',  "влады'чице"), # Иногда может употребляться в знач. "влады'цѣ"
    ('влДц',   "влады'ц"),
    ('влДчц',  "влады'чиц"),
    ('влДч',   "влады'ч"),
    ('ѵГл',    'вангел'), # Евангел...
    ('ѵГ',     'ванг'),   # Евангел...
    ('гг~л',   'нгел'), # ангел
    ('гл~г',   'глаг'),   # глагол...
    ('гл~',    'глагол'),
    ('глВ',    'глав'),
    ('гдСнь',  'господень'),
    ('гдСв',   'господев'),
    ('гдС',    'господ'),
    ('гпСж',   'госпож'),
    ('дв~д',   'давид'),
    ('дв~',    'дев'),
    ('двСтв',  'девств'),
    ('дс~',    'дꙋс'),
    ('дх~',    'дꙋх'),
    ('дш~',    'дꙋш'),
    ('и~с',    'исꙋс'),
    ('іи~л',   'израил'),
    ('кр~с',   'крес'),
    ('кр~ш',   'креш'),
    ('крСт',   'крест'),
    ('крСні',  'кресени'), # Это правило не 100%-ное. Слово ``воскрСнiи``
                             # может быть как формой предл.п. сущ. ВОСКРЕСЕНИЕ,
                             # так и формой мн.ч. прилагательного ВОСКРЕСНЫЙ,
                             # которая встречается, правда, достаточно редко.
                             # Возможно, есть и другие формы, для которых это правило
                             # также будет работать неправильно.
    ('крС',    'крес'),
    ('мДр',    'мꙋдр'),
    ('мл~тв',  'молитв'),
    ('млДнцъ', 'младенец'),
    ('млДн',   'младен'),
    ('млСрд',  'милосерд'),
    ('млСт',   'милост'),
    ('млС',    'милос'),
    ('мт~р',   "ма'тер"),
    ('мт~',    "ма'т"),
    ('мр~і',   'мари'),
    ('мРк',    'мѧрек'),   # Имярек
    ('мч~нк',  "мꙋ'ченик"),
    ('мч~нц',  "мꙋ'чениц"),
    ('мч~нч',  "мꙋ'ченич"),
    ('мч~н',   "мꙋ'чен"),
    ('мцС',    "ме'сѧц"),
    ('нб~с',   'небес'),
    ('нбСс',   'небес'),
    ('нбС',    'небес'),
    ('нб~',    'неб'),
    ('нлД',    'недел'),
    ('нн~',    'нын'),
    ('ѻч~ь',   "ѻте'чь"),
    ('ѻч~[єе]с', "ѻте'чес"),
    ("ѻ'ч~",   "ѻ'тч"),
    ("ѻц~ъ",   "ѻте'цъ"),
    ("ѻц~",    'ѻтц'),
    ('првДнъ', 'праведенъ'),
    ('првДн',  'праведн'),
    ('прДтч',  'предтеч'), # Предтеча
    ('прДт',   'предт'),   # Предтеча
    ('прпДб',  'преподоб'),
    ('прОр',   'прор'),    # Пророк
    ('прСн',   'присн'),
    ('прСт',   'прест'),
    ('прчСт',  'пречист'),
    ('пСкп',   'пископ'),  # епископ
    ('пСк',    'писк'),
    ('ржСтв',  'рождеств'),
    ('рСл',    'рꙋсал'),   # Иерусалим
    ('сл~нц',  'солнц'),
    ('сн~',    'сын'),
    ('сп~с',   'спас'),
    ('спСн',   'спасен'),
    ('срДц',   'сердц'),
    ('срДч',   'сердеч'),
    ('ст~',    'свѧт'),
    ('стрСт',  'страст'),
    ('сХ',     'стих'),
    ('стХр',   'стихир'),
    ('сщ~',    'свѧщ'),
    ('трОц',   'троиц'),
    ('трОч',   'троич'),
    ('трСт',   'трисвѧт'),
    ('хрСт',   'христ'),
    ('цр~к',   'церк'),
    ('цр~',    'цар'),
    ('црС',    'царс'),
    ('чл~в',   'челов'),
    ('ч~нк',   'ченик'),
    ('ч~нц',   'чениц'),
    ('ч~тл',   'чител'),
    ('чн~к',   'ченик'),
    ('чн~ц',   'чениц'),
    ('чн~',    'чен'),
    ('чСтн',   'честн'),
    ('чтСн',   'честн'),
    ('чСт',    'чист'),
    ('чтС',    'чист'),
    ('чт~л',   'чител'),
)
