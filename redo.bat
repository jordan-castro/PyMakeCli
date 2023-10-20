@ECHO OFF

python -m pip uninstall pymake-cli

CALL build.bat

@REM Get filename of the latest file in the dist folder
for /f "delims=" %%i in ('dir /b /od dist\*.gz') do set "newest=%%i"

python -m pip install dist\%newest%
