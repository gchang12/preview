@echo off
set scenedir=.\scenes
set targetdir=..\scenes
set sourcedir=.\raw
set texdir=.\tex
set errmsg=echo Please redownload the raw story files from my GitHub and reinsert them into the root of this directory: https://github.com/gchang12/preview
if not exist %sourcedir% %errmsg% & exit /b
if not exist %texdir% %errmsg% & exit /b
if not exist %scenedir% md %scenedir%
cd %sourcedir%
forfiles /p . /c "cmd /c if @isdir == "FALSE" copy @file %targetdir%"
cd ..
py quotes.py
cd %texdir%
pdflatex preview
start preview.pdf
cd ..
py word_count.py
