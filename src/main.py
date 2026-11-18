"""
Точка входа CLI-ассемблера учебной виртуальной машины.
"""
import argparse
import sys
from typing import List, Optional

from assembler import assemble
from binary_writer import write_binary
from byte_view import format_machine_code
from encoder import encode_program
from errors import AssemblerError
from loader import load_source

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
DEFAULT_OUTPUT = 'program.bin'


def build_parser() -> argparse.ArgumentParser:
    """
    Создаёт разборщик аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        prog='uvm-asm',
        description='Ассемблер УВМ, вариант 13, этап 2',
    )
    parser.add_argument(
        'source',
        help='путь к исходному файлу на языке YAML',
    )
    parser.add_argument(
        '-o', '--output',
        default=DEFAULT_OUTPUT,
        help='путь к двоичному файлу-результату',
    )
    parser.add_argument(
        '-t', '--test',
        action='store_true',
        help='режим тестирования: вывод машинного кода в байтах',
    )
    return parser


def run(args: argparse.Namespace) -> int:
    """
    Выполняет ассемблирование программы.
    """
    program = assemble(load_source(args.source))
    machine_code = encode_program(program)

    if args.test:
        print(format_machine_code(machine_code))
        return EXIT_SUCCESS

    write_binary(args.output, machine_code)
    print(f"Source: {args.source}")
    print(f"Output: {args.output}")
    print(f"Instructions: {len(program)}")
    print(f"Bytes: {len(machine_code)}")
    return EXIT_SUCCESS


def main(argv: Optional[List[str]] = None) -> int:
    """
    Главная функция приложения.
    """
    args = build_parser().parse_args(argv)

    try:
        return run(args)
    except AssemblerError as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        return EXIT_FAILURE


if __name__ == '__main__':
    sys.exit(main())