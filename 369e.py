"""Convert RGB to hex
"""

def convert_rgb_to_hex(rgb):
    red,green,blue = rgb
    red = '{:02X}'.format(red)
    green = '{:02X}'.format(green)
    blue = '{:02X}'.format(blue)
    # print(red,green,blue)
    return f'#{red}{green}{blue}'
print(convert_rgb_to_hex((255,100,100)))

# hexcolor(255, 99, 71) => "#FF6347"  (Tomato)
# hexcolor(184, 134, 11) => "#B8860B"  (DarkGoldenrod)
# hexcolor(189, 183, 107) => "#BDB76B"  (DarkKhaki)
# hexcolor(0, 0, 205) => "#0000CD"  (MediumBlue)
print(convert_rgb_to_hex((255, 99, 71)))
print(convert_rgb_to_hex((184, 134, 11)))
print(convert_rgb_to_hex((189, 183, 107)))
print(convert_rgb_to_hex((0, 0, 205)))