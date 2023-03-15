from pynput.mouse import Button, Controller
import time
import keyboard
mouse = Controller()
time_for_stroka= 14 # 14 секунд - время на строку 128 блоков(если 256 то 18 и тд)
koord = 999999 # начальная z
keyboard.wait("1") # программа ждет эту клавишу потом она строит
time.sleep(2)
while True:
    mouse.press(Button.right)
    keyboard.press("d")
    time.sleep(time_for_stroka)
    keyboard.release("d")
    mouse.release(Button.left)
    keyboard.send('t')
    time.sleep(1)
    keyboard.write(f'/tppos 9792 ~ {koord}')
    time.sleep(1)
    keyboard.send('enter')
    koord += 1
