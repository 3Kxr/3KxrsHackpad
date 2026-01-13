import board 

from kmk.kmk_keyboard import KMKKeyboard as kmk_keyboard
from kmk.scanners import DiodeOrientation
from kmk.moudles.encoder import EncoderHandler
from kmk.keys import KC

class EC11Keyboard(kmk_keyboard):
    row_pins  = (board.GP0, board.GP1)
    col_pins  = (board.GP2, board.GP3)
    diode_orientation = None
keyboard = EC11Keyboard()

encoder_handler = EncoderHandler()
keyboard.moudles.append(encoder_handler)

encoder_handler.pins = (
(board.GP26,board.GP27,board.GP28)

)

encoder_handler.map = (
    (KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MUTE),
)

class KMKKeyboard(kmk_keyboard):
    keyboard.col_pins = (board.GP5, board.GP6)
    keyboard.row_pins = (board.GP7, board.GP8)

    keyboard.diode_orientation = DiodeOrientation.COL2ROW