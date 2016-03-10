import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp


def svd_img(n): #define function svd_img
    
    #creating new sigma matrix for red, green, blue
    Sigma_red=Sred.copy()
    Sigma_green=Sgreen.copy()
    Sigma_blue=Sblue.copy()

    # to keep the 30 non-zero elements
    Sigma_red[n:800]=np.zeros_like(Sred[n:800])
    Sigma_green[n:800]=np.zeros_like(Sgreen[n:800])
    Sigma_blue[n:800]=np.zeros_like(Sblue[n:800])

    # to create diagonal matrix to perform dot multiplication
    Sigma_red = sp.linalg.diagsvd(Sigma_red,800,1000)
    Sigma_green = sp.linalg.diagsvd(Sigma_green,800,1000)
    Sigma_blue = sp.linalg.diagsvd(Sigma_blue,800,1000)

    # to perform dot multiplication for new matrix
    Red_new = np.dot(np.dot(Ured,Sigma_red), Vred)
    Green_new = np.dot(np.dot(Ugreen,Sigma_green), Vgreen)
    Blue_new = np.dot(np.dot(Ublue,Sigma_blue), Vblue) 

    #the new resolution matrix
    img[:,:,0]= Red_new
    img[:,:,1]= Green_new
    img[:,:,2]= Blue_new

    #to plot the images
    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()


#the original image
img=mpimg.imread('Watchtower_coast.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#to find U, Sigma and V for red matrix
Ured, Sred, Vred = sp.linalg.svd(r) 
#to find U, sigma and V for green matrix
Ugreen, Sgreen, Vgreen = sp.linalg.svd(g) 
#U, sigma and V for blue matrix
Ublue, Sblue, Vblue = sp.linalg.svd(b) 

#to find the non zero elements in sigma of each red, green and blue matrices
nonzero_r=np.count_nonzero(Sred)
nonzero_g=np.count_nonzero(Sgreen)
nonzero_b=np.count_nonzero(Sblue)
print("The number of non-zero elements in the original Sigma of red, green, blue matrices are", nonzero_r,"," ,nonzero_g,"and" ,nonzero_b, "respectively.")


#lower resolution of sigma 30
print("When n = 30, this is a lower resolution")
svd_img(30)

#better resolution of sigma 200
print("When n = 200, this is a better resolution")
svd_img(200)
