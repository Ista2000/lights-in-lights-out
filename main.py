import cv2
import numpy as np 
from matplotlib import pyplot as plt

images = []

for i in range(0, 11):
	filename = "Earthlights_" + str(i+1992) + ".png"
	img = cv2.imread(filename);

	img = cv2.resize(img, (1080, 650))

	if i == 10:
		final_img = img.copy()

	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	images.append(img)


for i in range(0, len(images[0])):
	for j in range(0, len(images[0][i])):

		if abs(int(images[0][i][j]) - int(images[1][i][j])) < 25:
			continue
		if int(images[0][i][j]) < int(images[1][i][j]):
			final_img[i][j] = [min(255, 220 * ((int(images[1][i][j]) - int(images[0][i][j])) / 100) + 10), 0, min(255, 120 * ((int(images[1][i][j]) - int(images[0][i][j])) / 100) + 10)]
		elif int(images[0][i][j]) > int(images[1][i][j]):
			final_img[i][j] = [min(255, 70 * ((int(images[1][i][j]) - int(images[0][i][j])) / 100) + 10), 0, min(255, 70 * ((int(images[1][i][j]) - int(images[0][i][j])) / 100) + 10)]



cv2.imshow('final', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.png', final_img)
