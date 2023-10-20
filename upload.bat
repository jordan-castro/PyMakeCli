@ECHO OFF

CALL build.bat

twine upload -r pypi dist/*
