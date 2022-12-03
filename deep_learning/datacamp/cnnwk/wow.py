import matplotlib.pyplot as plt

image = plt.imread('./media/01_Naruto.png')

image[:,:,0] = 0
image[:,:,1] = 0
plt.imshow(image)
plt.show()




