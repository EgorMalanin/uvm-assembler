@echo off
echo === Test 1: specification vectors ===
python src\main.py tests\spec_test.yaml -t

echo.
echo === Test 2: auto-compare with expected fields ===
cmd /c "python src\main.py tests\spec_test.yaml -t > tests\actual_ir.txt"
C:\Windows\System32\fc.exe tests\expected_ir.txt tests\actual_ir.txt

echo.
echo === Test 3: demo program (normal mode) ===
python src\main.py tests\demo_not.yaml -o build\demo.bin

echo.
echo === Test 4: unknown command ===
python src\main.py tests\err_unknown_op.yaml -t

echo.
echo === Test 5: operand out of range ===
python src\main.py tests\err_range.yaml -t

echo.
echo === Test 6: missing operand ===
python src\main.py tests\err_missing_field.yaml -t

echo.
echo === Test 7: broken YAML ===
python src\main.py tests\err_syntax.yaml -t

echo.
echo === Test 8: empty program ===
python src\main.py tests\err_empty.yaml -t

echo.
echo === Test 9: missing source file ===
python src\main.py tests\no_such_file.yaml -t