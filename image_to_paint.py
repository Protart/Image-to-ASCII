
import cv2
import time
import pyautogui
import numpy as np
import mss

img = cv2.imread('rickroll.jpg', 1)
vid = cv2.VideoCapture('pew.mp4')

x = 0
pyautogui.hotkey('alt', 'tab')
for ಠ_ಠ in range(225):
    ret, img = vid.read()
    print(x)
    x += 1

    gscale = "NK0OdXkoxlc;:,'. "
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    for row, i in enumerate(img.tolist()):
        i = [gscale[int(o/16)] for o in i]
        pixel_index = 0
        click_down = 0
        click_up = 0
        while True:
            try:
                if i[pixel_index] in gscale[:8] and i[pixel_index+1] in gscale[:8]:
                    click_up = pixel_index+1
                
                elif i[pixel_index] in gscale[:8] and i[pixel_index+1] not in gscale[:8]:
                    pyautogui.moveTo(click_down, row+170)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(click_up, 170+row)
                    pyautogui.mouseUp()

                else:
                    click_down = pixel_index

            except IndexError as e:
                break
            

            pixel_index += 1

    
    with mss.mss() as sct:
        sct.shot(output=f"{x}.png")