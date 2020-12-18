import re

from messages.error import PARSE_VALUE_ERROR_MESSAGE

from .exceptions import NotCorrectValue


def parse_value(message_raw: str) -> float:
    if message_raw.isdigit():
        return float(message_raw)
    message = message_raw.replace(' ', '')
    regexp = re.search(r'\d+', message)
    if not regexp:
        raise NotCorrectValue(PARSE_VALUE_ERROR_MESSAGE)
    return float(regexp.group(0))
