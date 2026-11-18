"""
Спецификация команд учебной виртуальной машины (вариант 13).

Каждая команда занимает COMMAND_SIZE_BYTES байт и кодируется
как A | (B << shift_b) | (C << shift_c) в порядке little-endian.
"""
from typing import Dict, NamedTuple

COMMAND_SIZE_BYTES = 6
OP_KEY = 'op'
MIN_FIELD_VALUE = 0
BIT_BASE = 1
ONE = 1

OP_LOAD_CONST = 'load_const'
OP_READ_MEM = 'read_mem'
OP_WRITE_MEM = 'write_mem'
OP_BIT_NOT = 'bit_not'
FIELD_A = 'A'
FIELD_B = 'B'
FIELD_C = 'C'

BYTE_ORDER = 'little'
BYTE_FORMAT = '0x{:02X}'
BYTE_SEPARATOR = ', '
FIRST_BYTE = 0

class FieldSpec(NamedTuple):
    """
    Описание операнда команды.
    """
    name: str
    shift: int
    width: int


class CommandSpec(NamedTuple):
    """
    Описание формата команды УВМ.
    """
    opcode: int
    field_b: FieldSpec
    field_c: FieldSpec


SPECS: Dict[str, CommandSpec] = {
    OP_LOAD_CONST: CommandSpec(
        opcode=77,
        field_b=FieldSpec('const', 7, 9),
        field_c=FieldSpec('addr', 16, 3),
    ),
    OP_READ_MEM: CommandSpec(
        opcode=44,
        field_b=FieldSpec('dst_reg', 7, 3),
        field_c=FieldSpec('src_reg', 10, 3),
    ),
    OP_WRITE_MEM: CommandSpec(
        opcode=90,
        field_b=FieldSpec('src_reg', 7, 3),
        field_c=FieldSpec('addr', 10, 20),
    ),
    OP_BIT_NOT: CommandSpec(
        opcode=43,
        field_b=FieldSpec('dst_addr', 7, 20),
        field_c=FieldSpec('src_addr', 27, 20),
    ),
}


def field_limit(width: int) -> int:
    """
    Вычисляет максимальное значение поля заданной разрядности.
    """
    return (BIT_BASE << width) - ONE