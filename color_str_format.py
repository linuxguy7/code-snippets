#!/usr/bin/python3

def get_color_code(red, green, blue):
    return "0x{0:0>2X}{1:0>2X}{2:0>2X}".format(red, green, blue)


RED=255
BLUE=10
GREEN=0
ccode=get_color_code(RED, GREEN, BLUE)

print("Hex color: {0}".format(ccode))


#NOTE: Can swap 'X' with 'x' in the format string to change hex ABCDEF to abcdef
