@echo off
echo === Test 1: unknown command ===
python src\main.py tests\err_unknown_op.yaml -t

echo.
echo === Test 2: operand out of range ===
python src\main.py tests\err_range.yaml -t

echo.
echo === Test 3: missing operand ===
python src\main.py tests\err_missing_field.yaml -t

echo.
echo === Test 4: broken YAML ===
python src\main.py tests\err_syntax.yaml -t

echo.
echo === Test 5: empty program ===
python src\main.py tests\err_empty.yaml -t

echo.
echo === Test 6: missing source file ===
python src\main.py tests\no_such_file.yaml -t