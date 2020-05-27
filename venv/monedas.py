
##############
# prep image - blur and convert to grey scale

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (17, 17), 0)
# plt.imshow(grey, cmap='gray')
# plt.imshow(blurred, cmap='gray')

###########
# show blurred image and grey scaled image
#genera ventanas emergentes
cv2.imshow("grey scale", grey)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

# canny edge detector
outline = cv2.Canny(blurred, 30, 150)
# show canny edge detector
cv2.imshow("The edges", outline)

cv2.waitKey(0)