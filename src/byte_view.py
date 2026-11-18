"""
Представление машинного кода в байтовом формате спецификации УВМ.
"""
from typing import List

from spec import (
    BYTE_FORMAT,
    BYTE_SEPARATOR,
    COMMAND_SIZE_BYTES,
    FIRST_BYTE,
)


def format_command(data: bytes) -> str:
    """
    Форматирует одну команду как список hex-байтов.
    """
    parts: List[str] = []

    for value in data:
        parts.append(BYTE_FORMAT.format(value))

    return BYTE_SEPARATOR.join(parts)


def format_machine_code(data: bytes) -> str:
    """
    Форматирует машинный код по одной команде на строку.
    """
    lines: List[str] = []

    for start in range(FIRST_BYTE, len(data), COMMAND_SIZE_BYTES):
        chunk = data[start:start + COMMAND_SIZE_BYTES]
        lines.append(format_command(chunk))

    return '\n'.join(lines)