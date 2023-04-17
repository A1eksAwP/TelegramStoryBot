from typing import Tuple, Iterable, Sequence, Mapping
from typing_extensions import SupportsIndex


class BasicStr(str):
    '''
    способы создания строки:

    my_str = ''  # Пустая строка

    next_str = 'new'  # Новая строка

    add_str = my_str + next_str  # -> 'new' это конкатенация строк

    my_str += next_str  # -> 'new' это конкатенация строк через переопределение переменной

    best_str = my_str.join(next_str)  # -> 'new' конкатенация строк через метод *.join(). Работает быстрее чем через "+"

    f_str = f'{my_str}{next_str}'  # -> 'new' конкатенация строк через f-строки. Работает быстрее чем через "+"

    r_str = r'сырая строка\n\t\r'  # -> 'сырая строка\n\t\r' на ней не будут применяться функциональные символы

    b_str = b'123'  # -> b'123' строка для записи в битовый формат

    любую переменную можно ПОПЫТАТЬСЯ привести к строке с помощью функции str()

    my_num = 123

    str(my_num) -> '123'

    my_list = ['Okay', 'Go']

    str(my_list) -> "['Okay', 'Go']"

    my_set = {1, '5', 10.7}

    str(my_set) -> "{1, 10.7, '5'}"

    my_dict = {1: 'One', 2: 'Two'}

    str(my_dict) -> "{1: 'One', 2: 'Two'}"

    my_tuple = (1, 2, '6', 9, 'Wow')

    str(my_tuple) -> "(1, 2, '6', 9, 'Wow')"

    my_bool = True

    str(my_bool) -> 'True'

    my_none = None

    str(my_none) -> 'None'
    '''
    def capitalize(self) -> str:
        '''
        *.capitalize(): делает первую букву строки заглавной

        :return: "hello world".capitalize()  # -> "Hello world"
        '''
    def casefold(self) -> str:
        '''
        # *.casefold(): приводит строку к нижнему регистру и удаляет некоторые особенности букв:
        акценты и диакритические знаки.

        :return: "Héllo Wôrld".casefold()  # -> "hello world"
        '''
    def center(self, __width: SupportsIndex, __fillchar: str = ...) -> str:
        '''
        *.center(width, fillchar): центрирует строку в строке заданной ширины (width), дополняя пустые пространства
        символами fillchar (по умолчанию - пробелами).

        :return:"hello".center(10, "-")  # -> "--hello---"
        '''
    def count(self, x: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int:
        '''
        *.count(substring, start, end): возвращает количество вхождений подстроки substring в
        строке в диапазоне (start, end).

        :return:"hello world".count("l")  # -> 3
        '''
    def encode(self, encoding: str = ..., errors: str = ...) -> bytes:
        '''
        *.encode(encoding, errors): кодирует строку в байтовый объект, используя заданную кодировку.

        :return: "hello world".encode("utf-8")  # -> b'hello world'
        '''
    def endswith(
        self, __suffix: str | Tuple[str, ...], __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...
    ) -> bool:
        '''
        *.endswith(suffix, start, end): возвращает True, если строка заканчивается подстрокой suffix
        в заданном диапазоне (start, end).

        :return: "hello world".endswith("world")  # -> True
        '''
    def expandtabs(self, tabsize: SupportsIndex = ...) -> str:
        '''
        *.expandtabs(tabsize): заменяет табуляции в строке на заданное количество пробелов (tabsize).

        :return: "hello\tworld".expandtabs(4)  # -> "hello   world"
        '''
    def find(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int:
        '''
        *.find(sub, start, end): находит первое вхождение подстроки substring в строке в диапазоне
        (start, end) и возвращает его индекс. Если подстрока не найдена, возвращает -1.

        :return: "hello world".find("world")  # -> 6
        '''
    def format(self, *args: object, **kwargs: object) -> str:
        '''
        *.format(*args, **kwargs): форматирует строку, заменяя в ней заполнители {} на
        значения из переданных аргументов.

        name = "Alice"

        age = 25

        :return: formatted_string = "My name is {0} and I'm {1} years old".format(name, age) ->
        "My name is Alice and I'm 25 years old"
        '''
    def format_map(self, map) -> str:
        '''
        *.format_map(mapping): аналогичен методу format(), но в качестве аргумента принимает словарь.

        values = {"name": "Alice", "age": 25}

        "My name is {values['name']} and I'm {values['age']} years old".format_map(values)
        :return: -> "My name is Alice and I'm 25 years old"
        '''
    def index(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int:
        '''
        *.index(sub, start, end): находит первое вхождение подстроки sub в строке в заданном диапазоне (start, end)
        и возвращает его индекс. Если подстрока не найдена, вызывает ValueError.
        :return: "hello world".index("world")  # -> 6
        '''
    def isalnum(self) -> bool:
        '''
        *.isalnum(): возвращает True, если все символы в строке являются буквами или цифрами.

        :return:  "hello123".isalnum()  # -> True
        '''
    def isalpha(self) -> bool:
        '''
        *.isalpha(): возвращает True, если все символы в строке являются буквами.

        :return: "hello".isalpha()  # -> True
        '''
    def isascii(self) -> bool:
        '''
        *.isascii(): возвращает True, если все символы в строке являются ASCII-символами.

        :return: "hello".isascii()  # -> True
        '''
    def isdecimal(self) -> bool:
        '''
        *.isdecimal(): возвращает True, если все символы в строке являются десятичными цифрами.

        :return: "123".isdecimal()  # -> True
        '''
    def isdigit(self) -> bool:
        '''
        *.isdigit(): возвращает True, если все символы в строке являются цифрами.

        :return: "123".isdigit()  # -> True
        '''
    def isidentifier(self) -> bool:
        '''
        *.isidentifier(): возвращает True, если строка является допустимым идентификатором в Python.

        :return: "hello_world".isidentifier()  # -> True
        '''
    def islower(self) -> bool:
        '''
        *.islower(): возвращает True, если все буквы в строке являются строчными.

        :return: "hello".islower()  # -> True
        '''
    def isnumeric(self) -> bool:
        '''
        *.isnumeric(): возвращает True, если все символы в строке являются числами.

        :return: "123".isnumeric()  # -> True
        '''
    def isprintable(self) -> bool:
        '''
        *.isprintable(): возвращает True, если все символы в строке являются печатаемыми.

        :return: "hello".isprintable()  # -> True
        '''
    def isspace(self) -> bool:
        '''
        *.isspace(): возвращает True, если все символы в строке являются пробельными.

        :return: "   ".isspace()  # -> True
        '''
    def istitle(self) -> bool:
        '''
        *.istitle(): возвращает True, если строка начинается с заглавной буквы и все остальные буквы являются строчными.

        :return: "Hello World".istitle()  # -> True
        '''
    def isupper(self) -> bool:
        '''
        *.isupper(): возвращает True, если все буквы в строке являются заглавными.

        :return: "HELLO".isupper()  # -> True
        '''
    def join(self, __iterable: Iterable[str]) -> str:
        '''
        *.join(iterable): возвращает строку, которая является объединением строк в итерируемом объекте iterable.

        :return: ' '.join(["Hello", "World"])  # -> "Hello World"
        '''
    def ljust(self, __width: SupportsIndex, __fillchar: str = ...) -> str:
        '''
        *.ljust(width, fillchar): выравнивает строку по левому краю, заполняя ее символом
        fillchar до заданной длины width.

        :return: "Hello".ljust(10, "-")  # -> "Hello-----"
        '''
    def lower(self) -> str:
        '''
        *.lower(): возвращает строку, все символы которой приведены к нижнему регистру.

        :return: "HELLO".lower()  # -> "hello"
        '''
    def lstrip(self, __chars: str | None = ...) -> str:
        '''
        *.lstrip(): удаляет все пробельные символы в начале строки.

        :return: " Hello".lstrip()  # -> "Hello"
        '''
    def maketrans(__x: str, __y: str, __z: str | None = ...) -> dict[int, int | None]:
        '''
        *.maketrans(x[, y[, z]]): возвращает таблицу перевода символов для использования с методами translate().

        table = str.maketrans("aeiou", "12345")

        :return: "hello".translate(table)  # -> "h2ll4"
        '''
    def partition(self, __sep: str) -> tuple[str, str, str]:
        '''
        *.partition(separator): разбивает строку на три части: все, что находится до первого вхождения
        разделителя separator,
        сам разделитель и все, что находится после него.
        :return: "hello world".partition(" ")  # -> ("hello", " ", "world")
        '''
    def removeprefix(self, __prefix: str) -> str:
        '''
        *.removeprefix(prefix): удаляет указанный префикс prefix из начала строки, если он присутствует.

        :return: "Hello World".removeprefix("Hello ")  # -> "World"
        '''
    def removesuffix(self, __suffix: str) -> str:
        '''
        *.removesuffix(suffix): удаляет указанный суффикс suffix из конца строки, если он присутствует.

        :return: "Hello World".removesuffix(" World")  # -> "Hello"
        '''
    def replace(self, __old: str, __new: str, __count: SupportsIndex = ...) -> str:
        '''
        *.replace(old, new[, count]): заменяет все вхождения подстроки old в строке на подстроку new.
        Можно указать необязательный аргумент count, который указывает максимальное количество замен.

        :return: "Hello World".replace("o", "X", 1)  # -> "HellX World"
        '''
    def rfind(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int:
        '''
        *.rfind(substring, start, end): находит последнее вхождение подстроки substring в строке в заданном диапазоне
        (start, end) и возвращает его индекс. Если подстрока не найдена, возвращает -1.

        :return: "hello world".rfind("o")  # -> 7
        '''
    def rindex(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int:
        '''
        *.rindex(substring, start, end): находит последнее вхождение подстроки substring в строке в заданном диапазоне
        (start, end) и возвращает его индекс. Если подстрока не найдена, вызывает ValueError.

        :return: "hello world".rindex("o")  # -> 7
        '''
    def rjust(self, __width: SupportsIndex, __fillchar: str = ...) -> str:
        '''
        *.rjust(width, fillchar): выравнивает строку по правому краю, заполняя ее символом fillchar
        до заданной длины width.

        :return: "Hello".rjust(10, "-")  # -> "-----Hello"
        '''
    def rpartition(self, __sep: str) -> tuple[str, str, str]:
        '''
        *.rpartition(separator): разбивает строку на три части: все, что находится до последнего вхождения разделителя
        separator, сам разделитель и все, что находится после него.
        :return: "hello world".rpartition(" ")  # -> ("hello", " ", "world")
        '''
    def rsplit(self, sep: str | None = ..., maxsplit: SupportsIndex = ...) -> list[str]:
        '''
        *.rsplit(sep=None, maxsplit=-1): разбивает строку на список, используя sep как разделитель. Если не указан,
        используется пробел. Можно указать необязательный аргумент maxsplit, который ограничивает количество разбиений.

        :return: "hello world".rsplit()  # -> ["hello", "world"]
        '''
    def rstrip(self, __chars: str | None = ...) -> str:
        '''
        *.rstrip(): удаляет все пробельные символы в конце строки.

        :return: "Hello    ".rstrip()  # -> "Hello"
        '''
    def split(self, sep: str | None = ..., maxsplit: SupportsIndex = ...) -> list[str]:
        '''
        *.split(sep=None, maxsplit=-1): разбивает строку на список, используя sep как разделитель (по умолчанию пробел).
        Можно указать необязательный аргумент maxsplit, который ограничивает количество разбиений.

        :return: "hello world".split()  # -> ["hello", "world"]
        '''
    def splitlines(self, keepends: bool = ...) -> list[str]:
        '''
        *.splitlines(keepends=False): разбивает строку на список, используя символы перевода строки.
        Если keepends=True, включает символы перевода строки в результирующие строки.

        :return: "hello\nworld".splitlines()  # -> ["hello", "world"]
        '''
    def startswith(
        self, __prefix: str | Tuple[str, ...], __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...
    ) -> bool:
        '''
        *.startswith(prefix[, start[, end]]): возвращает True, если строка начинается с указанного префикса prefix.
        Можно указать необязательные аргументы start и end, которые определяют диапазон поиска.

        :return: "hello world".startswith("hello")  # -> True
        '''
    def strip(self, __chars: str | None = ...) -> str:
        '''
        *.strip(): удаляет все пробельные символы в начале и конце строки.

        :return: "    Hello    ".strip()  # -> "Hello"
        '''
    def swapcase(self) -> str:
        '''
        *.swapcase(): возвращает новую строку, где все заглавные буквы приведены к строчным, а все строчные буквы -
        к заглавным

        :return: 'Hello WorlD'.swapcase()  # -> "hELLO wORLd"
        '''
    def title(self) -> str:
        '''
        *.title(): возвращает новую строку, в которой каждое слово начинается с заглавной буквы.

        :return: "hello world".title()  # -> "Hello World"
        '''
    def translate(self, __table: Mapping[int, int | str | None] | Sequence[int | str | None]) -> str:
        '''
        *.translate(table): возвращает новую строку, в которой все символы заменены в соответствии с
        таблицей перевода table.

        translation_table = str.maketrans("o", "0")

        :return: "hello world".translate(translation_table)  # -> "hell0 w0rld"
        '''
    def upper(self) -> str:
        '''
        *.upper(): возвращает новую строку, в которой все символы приведены к верхнему регистру.

        :return: "hello world".upper()  # -> "HELLO WORLD"
        '''
    def zfill(self, __width: SupportsIndex) -> str:
        '''
        *.zfill(width): возвращает новую строку, в которой исходная дополнена слева символами '0' до
        указанной длины width.

        :return: "123".zfill(5)  # -> "00123"
        '''