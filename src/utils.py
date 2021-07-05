import re
from string import ascii_letters as alphabet
from typing import Optional

alphabet_length = len(alphabet)
# stolen directly from Django sources
regex = re.compile(r'^(?:http|ftp)s?://'  # http:// or https://
                   r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                   r'localhost|'  # localhost...
                   r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                   r'(?::\d+)?'  # optional port
                   r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def make_code(number: int) -> str:
    number = number * 1_000_000  # hack to make urls look random

    url = ''
    while number:
        url += alphabet[number % alphabet_length]
        number //= alphabet_length
    return url


def check_and_wrap_url(url: str) -> Optional[str]:
    if not url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
        url = 'http://' + url
    if re.match(regex, url):
        return url
    else:
        return None
