import re

TRANSTABLE = (
    ("'", "'"),
    ('"', '"'),
    ("‘", "'"),
    ("’", "'"),
    ("«", '"'),
    ("»", '"'),
    ("“", '"'),
    ("”", '"'),
    ("–", "-"),
    ("—", "-"),
    ("‒", "-"),
    ("−", "-"),
    ("…", "..."),
    ("№", "#"),
    ("_", "_"),
    (" ", "-"),
    ("Щ", "Sch"),
    ("Щ", "SCH"),
    ("Ё", "Yo"),
    ("Ё", "YO"),
    ("Ж", "Zh"),
    ("Ж", "ZH"),
    ("Ц", "Ts"),
    ("Ц", "TS"),
    ("Ч", "Ch"),
    ("Ч", "CH"),
    ("Ш", "Sh"),
    ("Ш", "SH"),
    ("Ы", "Yi"),
    ("Ы", "YI"),
    ("Ю", "YU"),
    ("Ю", "Yu"),
    ("Я", "Ya"),
    ("Я", "YA"),
    ("А", "A"),
    ("Б", "B"),
    ("В", "V"),
    ("Г", "G"),
    ("Д", "D"),
    ("Е", "E"),
    ("З", "Z"),
    ("И", "I"),
    ("Й", "J"),
    ("К", "K"),
    ("Л", "L"),
    ("М", "M"),
    ("Н", "N"),
    ("О", "O"),
    ("П", "P"),
    ("Р", "R"),
    ("С", "S"),
    ("Т", "T"),
    ("У", "U"),
    ("Ф", "F"),
    ("Х", "H"),
    ("Э", "E"),
    ("Ъ", "`"),
    ("Ь", "'"),
    ("щ", "sch"),
    ("ё", "yo"),
    ("ж", "zh"),
    ("ц", "ts"),
    ("ч", "ch"),
    ("ш", "sh"),
    ("ы", "yi"),
    ("ю", "yu"),
    ("я", "ya"),
    ("а", "a"),
    ("б", "b"),
    ("в", "v"),
    ("г", "g"),
    ("д", "d"),
    ("е", "e"),
    ("з", "z"),
    ("и", "i"),
    ("й", "j"),
    ("к", "k"),
    ("л", "l"),
    ("м", "m"),
    ("н", "n"),
    ("о", "o"),
    ("п", "p"),
    ("р", "r"),
    ("с", "s"),
    ("т", "t"),
    ("у", "u"),
    ("ф", "f"),
    ("х", "h"),
    ("э", "e"),
    ("ъ", "`"),
    ("ь", "'"),
    ("c", "c"),
    ("q", "q"),
    ("y", "y"),
    ("x", "x"),
    ("w", "w"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("0", "0"),
)

RU_ALPHABET = [x[0] for x in TRANSTABLE]
EN_ALPHABET = [x[1] for x in TRANSTABLE]
ALPHABET = RU_ALPHABET + EN_ALPHABET


def my_translify(in_string, strict=True):
    translit = in_string
    for symb_in, symb_out in TRANSTABLE:
        translit = translit.replace(symb_in, symb_out)

    if strict and any(ord(symb) > 128 for symb in translit):
        raise ValueError("" + "")

    return translit


def my_detranslify(in_string):
    try:
        russian = str(in_string)
    except UnicodeDecodeError:
        raise ValueError("" + "" + "")

    for symb_out, symb_in in TRANSTABLE:
        russian = russian.replace(symb_in, symb_out)

    return russian


def my_slugify(in_string):
    try:
        u_in_string = str(in_string).capitalize()
    except UnicodeDecodeError:
        raise ValueError("We expects when in_string is str type," + "it is an ascii, but now it isn't. Use unicode " + "in this case.")
    u_in_string = re.sub('\&amp\;|\&', ' and ', u_in_string)
    u_in_string = re.sub('[-\s]+', ' ', u_in_string)
    u_in_string = ''.join([symb for symb in u_in_string if symb in ALPHABET])
    out_string = my_translify(u_in_string)
    return re.sub('[^\w\s-]', '', out_string).strip().lower()
