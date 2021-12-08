import numpy as np
import cv2

# color 설정

blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

# 모두 0으로 되어 있는 빈 Canvas(검정색)

#circle img,center,radius,color,thickness
back_ground = np.zeros((500, 500, 3), np.uint8)
red_circle = cv2.circle(back_ground, (250, 250), 30, red_color, -1)
blue_circle = cv2.circle(back_ground, (250, 100), 30, blue_color, -1)

cv2.imshow('circle',back_ground)
cv2.waitKey(0)
cv2.destroyAllWindows()