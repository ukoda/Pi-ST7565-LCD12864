#!/usr/bin/python3.9
import st7565
import xglcd_font as font
import time



arcadepix    = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/ArcadePix9x11.c',       9, 11)
ballys       = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Bally5x8.c',            5,  8)
ballyl       = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Bally7x9.c',            7,  9)
broadway     = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Broadway17x15.c',      17, 15)
espressdolce = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/EspressoDolce18x24.c', 18, 24)
fixedfont    = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/FixedFont5x8.c',        5,  8)
neato        = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Neato5x7.c',            5,  7)
neatoreduced = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/NeatoReduced5x7.c',     5,  7)
robotrons    = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Robotron7x11.c',        7, 11)
unispaced    = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Unispace12x24.c',      12, 24)
wendy        = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Wendy7x8.c',            7,  8)

glcd = st7565.Glcd()
glcd.init()

page = 1

try:
  while True:
    glcd.clear_back_buffer()

    if page == 1:
      glcd.draw_string('ArcadePix9x11',   arcadepix,    0,  0)
      glcd.draw_string('Bally5x8',        ballys,       0, 13)
      glcd.draw_string('Bally7x9',        ballyl,       0, 23)
      glcd.draw_string('Broadway17',      broadway,     0, 34)
      glcd.draw_string('FixedFont5x8',    fixedfont,    0, 51)
      
    if page == 2:
      glcd.draw_string('EspressoD',       espressdolce, 0,  0)
      glcd.draw_string('Neato5x7',        neato,        0, 26)
      glcd.draw_string('NeatoReduced5x7', neatoreduced, 0, 35)
      
    if page == 3:
      glcd.draw_string('Robotron7x11',    robotrons,    0, 0)
      glcd.draw_string('Unispace',        unispaced,    0, 13)
      glcd.draw_string('Wendy7x8',        wendy,        0, 39)
    
    glcd.flip()

    time.sleep(5)    
    page += 1
    if page > 3:
      page = 1

except KeyboardInterrupt:
    print('\nCtrl-C pressed.  Cleaning up and exiting...')
finally:
    glcd.cleanup()        
    
