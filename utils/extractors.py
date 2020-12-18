import re
from typing import Optional


def parse_value(message_raw: str) -> Optional[float]:
    if message_raw.isdigit():
        return float(message_raw)
    message = re.sub(r'\s+', ' ', message_raw)
    regexp = re.search(r'([.]?\d[\d\s.,]*)', message, re.VERBOSE)
    if regexp:
        print(regexp)
        value = regexp.group(0).replace(',', '.')
        print(value)
        return float(value)
    return None
