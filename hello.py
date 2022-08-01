import pyautogui as gui
import sys

print('中断するにはCrt+Cを入力してください。')

try:
    while True:
    if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
       x=input("取得したい箇所にカーソルを当てEnterキー押してください\n")
       print(gui.position())

       
except KeyboardInterrupt:
    print('\n終了')
    sys.exit()
