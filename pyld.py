from ahk import goahk

goahk('''run,"C:\Program Files\Git\git-bash.exe"
Sleep, 1000
WinWait, ahk_class mintty, 
Sleep, 1000
ControlSend , , git add * -f{Enter}, ahk_class mintty
Sleep, 800
ControlSend , , git commit -m "general update"{Enter}, ahk_class mintty
Sleep, 800
ControlSend , , git push origin master{Enter}, ahk_class mintty''')