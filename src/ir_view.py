"""
Вывод промежуточного представления в формате тестов спецификации.
"""
from typing import Any, Dict, List

FIELD_A = 'A'
FIELD_B = 'B'
FIELD_C = 'C'


def format_ir(program: List[Dict[str, Any]]) -> str:
    """
    Форматирует промежуточный код как последовательность полей.
    """
    lines: List[str] = []

    for item in program:
        lines.append(
            f"{FIELD_A}={item[FIELD_A]}, "
            f"{FIELD_B}={item[FIELD_B]}, "
            f"{FIELD_C}={item[FIELD_C]}"
        )

    return '\n'.join(lines)