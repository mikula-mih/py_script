@echo off
:----------------------------------------------------------------------------
REM First try was a failure -> trying to do the job with PStools - psexec
:set pass = /A 8598
:set /p  a=
:%a%
:echo %pass% | %a%
:----------------------------------------------------------------------------
REM Here begins working stuff
set hostname= 'DESKTOP-METBNFE'
set password= '8598'
set exeBrave= 'C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe'

set /p user="Open Brave with UserAccount: "
echo Brave opened with %user%
set command=psexec \\DESKTOP-METBNFE -u "%user%" -p 8598 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

cmd /c %command%
:cls
:exit /B

