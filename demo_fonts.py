"""SSD1309 demo (fonts)."""
from time import sleep
from machine import Pin, I2C  # type: ignore
from xglcd_font import XglcdFont
from ssd1309 import Display


def test():
    """Test code."""
    i2c = I2C(0, freq=400000, scl=Pin(1), sda=Pin(0))  # Pico I2C bus 1
    display = Display(i2c=i2c, rst=Pin(2), flip=True)

    print("Loading fonts.  Please wait.")
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    rototron = XglcdFont('fonts/Robotron7x11.c', 7, 11)
    unispace = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)
    wendy = XglcdFont('fonts/Wendy7x8.c', 7, 8)

    print("Drawing fonts.")

    text_height = bally.height
    display.draw_text(display.width, display.height // 2 - text_height // 2,
                      "Bally", bally, rotate=180)

    text_width = rototron.measure_text("ROTOTRON")
    display.draw_text(display.width // 2 - text_width // 2, 0, "ROTOTRON",
                      rototron)

    text_width = unispace.measure_text("Unispace")
    text_height = unispace.height
    display.draw_text(display.width // 2 - text_width // 2,
                      display.height - text_height, "Unispace",
                      unispace, invert=True)

    text_width = wendy.measure_text("Wendy")
    display.draw_text(0, display.height // 2 - text_width // 2,
                      "Wendy", wendy, rotate=90)

    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()
