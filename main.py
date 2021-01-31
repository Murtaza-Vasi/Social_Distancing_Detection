import cv2

# Here the second argument represents a flag which denotes how to read the image the flag has three values
# 1 for reading the image as a colored image
# 0 for reading the image as grayscale image
# -1 for reading the image as a colored image with alpha channel

# Here in the first argument if we provide a wrong path or wrong file name then also the function will
# not throw any error instead it will return None

image = cv2.imread('lena.jpg', -1)
print(image)

# To display the image we can use the imshow() method of the opencv package

cv2.imshow('image', image)

# Waiting for 5 seconds after the image is displayed
# cv2.waitKey(5000)

# If we want to display the image for any amount of time then we can use the waitKey() method with 0 as the argument
key = cv2.waitKey(0)

# 27 indicates the user has pressed the escape key

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):

    # To write an image we can use the imwrite() method
    cv2.imwrite('lena_copy.png', image)

    # We can destroy the window in which the image was displayed
    cv2.destroyAllWindows()
