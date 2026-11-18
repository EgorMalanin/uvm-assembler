"""
Транслятор промежуточного представления в машинный код УВМ.

Команда кодируется как A | (B << shift_b) | (C << shift_c)
и записывается в порядке little-endian.
"""
from typing import Any, Dict, List

from errors import EncodingError
from spec import (
    BYTE_ORDER,
    COMMAND_SIZE_BYTES,
    FIELD_A,
    FIELD_B,
    FIELD_C,
    OP_KEY,
    SPECS,
)


def encode_instruction(item: Dict[str, Any]) -> bytes:
    """
    Кодирует одну команду промежуточного представления.
    """
    name = item[OP_KEY]
    if name not in SPECS:
        raise EncodingError(f"Unknown command in IR: {name}")

    command = SPECS[name]
    code = item[FIELD_A]
    code |= item[FIELD_B] << command.field_b.shift
    code |= item[FIELD_C] << command.field_c.shift

    try:
        return code.to_bytes(COMMAND_SIZE_BYTES, BYTE_ORDER)
    except OverflowError:
        raise EncodingError(f"Command '{name}' exceeds field size")


def encode_program(program: List[Dict[str, Any]]) -> bytes:
    """
    Кодирует всю программу в машинное представление.
    """
    chunks: List[bytes] = []

    for item in program:
        chunks.append(encode_instruction(item))

    return b''.join(chunks)