import cv2

img = cv2.imread('test.jpg')
f = open('test.txt', 'w')
gscale = "NK0OdXkoxlc;:,'. " #16 shades of grey
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for i in img.tolist():
    i = [gscale[int(o/16)] for o in i] #pixel to ascii
    f.write(f"{''.join(i)}\n")