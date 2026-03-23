import board
import digitalio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# 板载 LED 闪烁 5 次，证明代码运行
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
for _ in range(5):
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.2)

print("Code is running!")

keyboard = KMKKeyboard()

PINS = [board.D7, board.D8, board.D9, board.D10]

# 注意：根据实际接线，如果按键接 GND，按下为低电平，用 False
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,   # 改为 False
)

# 最简单映射：四个按键输出 A B C D
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

print("Keyboard ready. Press keys A B C D")
keyboard.go()
