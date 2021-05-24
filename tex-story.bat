@echo off
set targetdir=..\scenes
set sourcedir=.\raw
set texdir=.\tex
set errmsg=echo Please redownload the raw story documents from: https://github.com/gchang12/preview
if not exist %sourcedir% %errmsg% & exit /b
if not exist %texdir% %errmsg% & exit /b
cd %sourcedir%
if not exist %targetdir% md %targetdir%
copy *.txt %targetdir%
cd ..
py quotes.py
cd %texdir%
pdflatex preview
start preview.pdf
rd /q /s %targetdir%
cd ..
py word_count.py
pause
