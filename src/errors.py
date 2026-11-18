"""
Пользовательские исключения ассемблера учебной виртуальной машины.
"""
class AssemblerError(Exception):
    """Базовое исключение ассемблера."""


class SourceFileError(AssemblerError):
    """Ошибка доступа к исходному файлу."""


class StructureError(AssemblerError):
    """Ошибка структуры YAML-документа."""


class InstructionError(AssemblerError):
    """Ошибка отдельной инструкции программы."""