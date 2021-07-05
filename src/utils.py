from string import ascii_letters as alphabet

alphabet_length = len(alphabet)


def make_code(number: int) -> str:
    number = number * 1_000_000  # hack to make urls look random

    url = ''
    while number:
        url += alphabet[number % alphabet_length]
        number //= alphabet_length
    return url
