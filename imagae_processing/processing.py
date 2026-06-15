from skimage.color import rgb2gray
from skimage import io 
from skimage import transform
import matplotlib.pyplot as plt

#image read
image = io.imread("image.jpg")

#convert it into grey scale
grey = rgb2gray(image)
plt.imshow(grey,cmap="grey")

resized_image = transform.resize(image, (100, 100))
io.imshow(resized_image)


plt.savefig("output.png")
plt.title("Original image")
plt.show()