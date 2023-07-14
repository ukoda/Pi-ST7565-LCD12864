#!/usr/bin/python3.9
import st7565
import xglcd_font as font
import math
import time
import os
import psutil
import sys



neato     = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Neato5x7.c',       5,  7)
unispaced = font.XglcdFont('/home/david/Dev/Pi-ST7565-LCD12864/fonts/Unispace12x24.c', 12, 24)
glcd = st7565.Glcd()
glcd.init()

# Stuff that doesn't normally change

# Host name

with open('/etc/hostname', 'r') as file:
  hostname = file.read().replace('\n', '')
  file.close()

# IP address

mine = os.popen('ifconfig eth0 | grep "inet 1" | cut -c 14-25')
ip = mine.read().split()[0]
mine.close()

# Title

if len(sys.argv) > 1:
  title = str(sys.argv[1])
else:
  title = hostname

try:

  # Main loop
  
  while True:
    glcd.clear_back_buffer()
    
    # Title

    glcd.draw_string(title, unispaced, 0, 0)

    # Host name and IP address
    
    glcd.draw_string(hostname + ' ' + ip, neato, 0, 26)

    # Time and uptime
    
    timestr = time.strftime("%H:%M:%S")
    mine = os.popen('uptime')
    up = mine.read().split()[2].split(',')[0]
    mine.close()

    glcd.draw_string(timestr + ' up ' + up, neato, 0, 36)
    
    # Temperature and CPU usage

    mine = os.popen('vcgencmd measure_temp')
    temperature = mine.read().split('=')[1].split("'")[0]
    mine.close()
    cpu = psutil.cpu_percent()

    glcd.draw_string(f'{temperature}C  {cpu}%', neato, 0, 46)
    
    # Memory usage
    
    memory = psutil.virtual_memory()
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)    
    
    glcd.draw_string(f'{available}/{total} MB', neato, 0, 56)

    # Display all the information

    glcd.flip()
    time.sleep(2)
except KeyboardInterrupt:
    print('\nCtrl-C pressed.  Cleaning up and exiting...')
finally:
    glcd.cleanup()        
    
