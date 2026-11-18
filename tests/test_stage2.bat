@echo off
echo === Test 1: machine code of specification vectors ===
python src\main.py tests\spec_test.yaml -t

echo.
echo === Test 2: auto-compare with expected bytes ===
cmd /c "python src\main.py tests\spec_test.yaml -t > tests\actual_bytes.txt"
C:\Windows\System32\fc.exe tests\expected_bytes.txt tests\actual_bytes.txt

echo.
echo === Test 3: write binary file ===
python src\main.py tests\spec_test.yaml -o build\spec_test.bin

echo.
echo === Test 4: binary file size ===
dir build\spec_test.bin

echo.
echo === Test 5: hex dump of binary file ===
certutil -dump build\spec_test.bin

echo.
echo === Test 6: demo program ===
python src\main.py tests\demo_not.yaml -t

echo.
echo === Test 7: unwritable output path ===
python src\main.py tests\spec_test.yaml -o Z:\nope\out.bin


