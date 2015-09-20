

run,"C:\Program Files\Git\git-bash.exe"
WinWait, ahk_class mintty, 

ControlSend , , git add * -f{Enter}, ahk_class mintty
Sleep, 800
ControlSend , , git commit -m "常规更新"{Enter}, ahk_class mintty
Sleep, 800
ControlSend , , git push origin master{Enter}, ahk_class mintty