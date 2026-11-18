"""
Транслятор языка ассемблера УВМ в промежуточное представление.
"""
from typing import Any, Dict, List

from errors import InstructionError
from spec import MIN_FIELD_VALUE, OP_KEY, SPECS, FieldSpec, field_limit

FIRST_INSTRUCTION = 1
FIELD_A = 'A'
FIELD_B = 'B'
FIELD_C = 'C'


def assemble(
    instructions: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Транслирует программу в промежуточное представление.
    """
    program: List[Dict[str, Any]] = []

    for number, raw in enumerate(instructions, FIRST_INSTRUCTION):
        program.append(_assemble_instruction(raw, number))

    return program


def _assemble_instruction(
    raw: Any,
    number: int
) -> Dict[str, Any]:
    """
    Транслирует одну инструкцию в набор полей команды.
    """
    if not isinstance(raw, dict):
        raise InstructionError(
            f"Instruction {number}: must be a mapping"
        )

    name = _read_opcode(raw, number)
    command = SPECS[name]

    return {
        OP_KEY: name,
        FIELD_A: command.opcode,
        FIELD_B: _read_field(raw, command.field_b, number),
        FIELD_C: _read_field(raw, command.field_c, number),
    }


def _read_opcode(raw: Dict[str, Any], number: int) -> str:
    """
    Читает и проверяет мнемонику команды.
    """
    if OP_KEY not in raw:
        raise InstructionError(
            f"Instruction {number}: missing '{OP_KEY}'"
        )

    name = raw[OP_KEY]

    if not isinstance(name, str):
        raise InstructionError(
            f"Instruction {number}: '{OP_KEY}' must be a string"
        )

    if name not in SPECS:
        raise InstructionError(
            f"Instruction {number}: unknown command '{name}'"
        )

    return name


def _read_field(
    raw: Dict[str, Any],
    field: FieldSpec,
    number: int
) -> int:
    """
    Читает и проверяет операнд команды.
    """
    if field.name not in raw:
        raise InstructionError(
            f"Instruction {number}: missing '{field.name}'"
        )

    value = raw[field.name]

    if isinstance(value, bool) or not isinstance(value, int):
        raise InstructionError(
            f"Instruction {number}: '{field.name}' must be integer"
        )

    _check_range(value, field, number)
    return value


def _check_range(
    value: int,
    field: FieldSpec,
    number: int
) -> None:
    """
    Проверяет попадание операнда в разрядную сетку поля.
    """
    limit = field_limit(field.width)

    if value < MIN_FIELD_VALUE or value > limit:
        raise InstructionError(
            f"Instruction {number}: '{field.name}'={value} "
            f"out of range {MIN_FIELD_VALUE}..{limit}"
        )