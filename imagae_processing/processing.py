from skimage.color import rgb2gray
from skimage import io 
import matplotlib.pyplot as plt


image = io.imread("image.jpg")

#convert it into grey scale
grey = rgb2gray(image)
plt.imshow(grey,cmap="grey")

plt.savefig("output.png")
plt.title("Original image")
plt.show()