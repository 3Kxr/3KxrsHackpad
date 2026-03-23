import board
import digitalio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

"""
SW1 -> D7
SW2 -> D8
SW3 -> D9
SW4 -> D10
LED DIN (first SK6812MINI-E) -> D4
Encoder -> D0,D1,D2
"""
PINS = [board.D7, board.D8, board.D9, board.D10]
ENCODER_PINS = [board.D0, board.D1]  # Adjust based on your actual encoder wiring
LED_PIN = board.D4
NUM_LEDS = 2

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


"""
TODO: Implement the following functions
"""
# Encoder configuration (if using encoders)
#encoder_handler = EncoderHandler()
#encoder_handler.pins = ENCODER_PINS
# Uncomment and configure encoder behavior if you have encoders
#encoder_handler.map = [ (KC.VOLU, KC.VOLD, KC.MUTE) ]


#keyboard.modules.append(encoder_handler)

# Example macro: Save (Cmd+S on Mac; swap LCTRL for LCMD on Windows)
SAVE_MACRO = KC.MACRO(
    Press(KC.LCMD),
    Tap(KC.S),
    Release(KC.LCMD),
)

"""
TODO:Implement the following functions
Keymap:
SW1 = Play/Pause
SW2 = Next Track
SW3 = Toggle LEDs on/off
SW4 = Cycle RGB modes (solid → rainbow → breathe)
"""
keyboard.keymap = [
    [
        KC.LWIN(KC.L),
        KC.LEFT,
        KC.DOWN,
        KC.RIGHT
        ]
]

if __name__ == "__main__":
    keyboard.go()
