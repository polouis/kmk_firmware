print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import SplitSide
from storage import getmount

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

if side == SplitSide.LEFT:
    col_pins = (board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,)
    row_pins = (board.GP11,board.GP10,board.GP9,board.GP8,)
else:
    col_pins = (board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,)
    row_pins = (board.GP8,board.GP9,board.GP10,board.GP11,)


class KMKKeyboard(_KMKKeyboard):
    col_pins = col_pins
    row_pins = row_pins
    diode_orientation = DiodeOrientation.COL2ROW
    # encoder_pin_0 = board.A2
    # encoder_pin_1 = board.A3
