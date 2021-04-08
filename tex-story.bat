@echo off
set homedir=%cd%
set targetdir=C:\Users\Eclair\Documents\projects\latex\preview\scenes
if not exist %targetdir% md %targetdir%
set sourcedir=C:\Users\Eclair\Documents\projects\untitled
cd %sourcedir%
forfiles /p . /c "cmd /c if @isdir == "FALSE" copy @file %targetdir%"
cd %targetdir%
py C:\Users\Eclair\Documents\projects\python\overused\quotes.py
cd ..
pdflatex preview
set story=C:\Users\Eclair\Documents\projects\latex\preview\preview.pdf
start %story%
py C:\Users\Eclair\Documents\projects\python\overused\word_count.py
if not exist D:\ exit /b
copy /y %story% D:\NOOK\