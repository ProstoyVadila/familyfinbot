import re
from typing import Optional


def parse_value(message_raw: str) -> Optional[float]:
    if message_raw.isdigit():
        return float(message_raw)
    message = re.sub(r'\s+', ' ', message_raw)
    print(f'__________________{message}____________________')
    regexp = re.search(r'([.]?\d[\d\s.,]*)', message, re.VERBOSE)
    if regexp:
        value = regexp.group(0).replace(',', '.')
        value_float = float(value)
        return round(value_float, 2)
    return None
