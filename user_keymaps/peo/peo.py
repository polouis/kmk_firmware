import board

from kb import KMKKeyboard
from kmk.keys import KC
# from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.extensions.media_keys import MediaKeys
from storage import getmount

keyboard = KMKKeyboard()
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())
layers_ext = Layers()
# side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)

keyboard.modules = [layers_ext, split]

keyboard.keymap = [
    [
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,         KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.LSFT,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,         KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LCTL,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,         KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.ESC,
        KC.NO,    KC.NO,    KC.NO,    KC.LGUI,  KC.MO(1), KC.SPC,       KC.ENT,   KC.MO(2), KC.RALT,  KC.NO,    KC.NO,    KC.NO
    ],
    [  # MO(1)
        KC.TRNS,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,        KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.NO,    KC.NO,    KC.UP,    KC.NO,    KC.NO,    KC.NO,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.NO,    KC.LEFT,  KC.DOWN,  KC.RIGHT, KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.LGUI,  KC.TRNS, KC.SPC,        KC.ENT,   KC.MO(3), KC.RALT,  KC.NO,    KC.NO,    KC.NO
    ],
    [  # MO(2)
        KC.TRNS,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,      KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.BSPC,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.MINS,  KC.EQL,   KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.GRV,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.UNDS,  KC.PLUS,  KC.LCBR,  KC.RCBR,  KC.PIPE,  KC.TILD,
        KC.NO,    KC.NO,    KC.NO,    KC.LGUI,  KC.MO(3), KC.SPC,       KC.ENT,   KC.TRNS,  KC.LALT,  KC.NO,    KC.NO,    KC.NO
    ],
    [  # MO(3)
        KC.TRNS,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,      KC.VOLU,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.BSPC,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.VOLD,  KC.EQL,   KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.GRV,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,        KC.UNDS,  KC.PLUS,  KC.LCBR,  KC.RCBR,  KC.PIPE,  KC.TILD,
        KC.NO,    KC.NO,    KC.NO,    KC.LGUI,  KC.MO(3), KC.SPC,       KC.ENT,   KC.TRNS, KC.RALT,  KC.NO,    KC.NO,    KC.NO
    ],
]

# encoder_handler = EncoderHandler()
# encoder_handler.pins = ((keyboard.encoder_pin_1, keyboard.encoder_pin_0, None, False),)
# encoder_handler.map = (
#     ((KC.VOLD, KC.VOLU),),  # base layer
#     ((KC.VOLD, KC.VOLU),),  # Raise
#     ((KC.VOLD, KC.VOLU),),  # Lower
# )
# keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
