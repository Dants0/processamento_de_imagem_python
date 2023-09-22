import cv2

img = cv2.imread("star.jpg")

flip_horizontal = img[::-1,:]
flip_vertical = img[:,::-1]

cv2.imshow("Flip Horizontal", flip_horizontal)

cv2.imshow("Flip Vertical", flip_vertical)


flip_hv = img[::-1, ::-1]

cv2.imshow("Flip Horizontal e Flip Vertical", flip_hv)

cv2.waitKey(0)