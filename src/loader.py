"""
Загрузка исходной программы на языке YAML.
"""
from typing import Any, Dict, List

import yaml

from errors import SourceFileError, StructureError

PROGRAM_KEY = 'program'


def load_source(path: str) -> List[Dict[str, Any]]:
    """
    Читает исходный файл и возвращает список инструкций.
    """
    data = _read_yaml(path)
    return _extract_program(data)


def _read_yaml(path: str) -> Any:
    """
    Открывает файл и разбирает YAML-документ.
    """
    try:
        with open(path, 'r', encoding='utf-8') as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        raise SourceFileError(f"Source file not found: {path}")
    except OSError as error:
        raise SourceFileError(f"Cannot read source file: {error}")
    except yaml.YAMLError as error:
        raise StructureError(f"Invalid YAML syntax: {error}")


def _extract_program(data: Any) -> List[Dict[str, Any]]:
    """
    Извлекает секцию program из YAML-документа.
    """
    if not isinstance(data, dict):
        raise StructureError("Document root must be a mapping")

    if PROGRAM_KEY not in data:
        raise StructureError(f"Missing '{PROGRAM_KEY}' section")

    program = data[PROGRAM_KEY]

    if not isinstance(program, list):
        raise StructureError(f"'{PROGRAM_KEY}' must be a list")

    if not program:
        raise StructureError(f"'{PROGRAM_KEY}' must not be empty")

    return program