import time
import cv2
import os
import numpy as np

i = 0
caminho = "Originais\\"

for numero_imagem, imagem in enumerate(os.listdir(caminho), start=1):
    caminho_imagem = caminho + imagem
    print(caminho_imagem)

    image = cv2.imread(caminho_imagem)
    w, h, _ = image.shape

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    imgblur = cv2.blur(gray, (5, 5))

    ret, thresh = cv2.threshold(imgblur, 150, 280, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
    imgmorph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    gaussian = cv2.GaussianBlur(imgmorph,(3,3),cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian,100,200)

    contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contour = max(contours, key = len)

    contourImg = cv2.drawContours(image, contour, -1, (255,0,255), 3)

    cv2.imwrite(('P&B\\' + str(i) + '.png'), gray)
    cv2.imwrite(('Blur\\' + str(i) + '.png'), imgblur)
    cv2.imwrite(('Threshold\\' + str(i) + '.png'), thresh)
    cv2.imwrite(('Morph\\' + str(i) + '.png'), imgmorph)
    cv2.imwrite(('Gaussian\\' + str(i) + '.png'), gaussian)
    cv2.imwrite(('Contornadas\\' + str(i) + '.png'), contourImg)

    # cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Contours', h//4, w//4)
    # cv2.imshow("Contours", contourImg)

    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('img', h//4, w//4)
    # cv2.imshow('img', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    i = i + 1