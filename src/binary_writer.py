"""
Запись машинного кода УВМ в двоичный файл.
"""
import os

from errors import OutputFileError


def write_binary(path: str, data: bytes) -> None:
    """
    Записывает машинный код в двоичный файл.
    """
    _ensure_directory(path)

    try:
        with open(path, 'wb') as stream:
            stream.write(data)
    except OSError as error:
        raise OutputFileError(f"Cannot write binary file: {error}")


def _ensure_directory(path: str) -> None:
    """
    Создаёт каталог для выходного файла при необходимости.
    """
    directory = os.path.dirname(path)

    if not directory:
        return

    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        raise OutputFileError(f"Cannot create directory: {error}")