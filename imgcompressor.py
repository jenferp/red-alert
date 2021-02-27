from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt

def compress_images():

    # create new directory for compressed images
    new_path = './compressed_train_images_hands'
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    # To extract non-compressed images
    path = 'train_images_hands'      # directory path
    paths = os.listdir(path)   # subdirectory paths
    print(paths)              # <class 'list'>: ['.DS_Store', 'blood', 'non_blood']
    for sub in paths[1:]:

        # create new sub-directories for blood and non_blood inside new_path
        new_sub = new_path + '/{}'.format(sub)
        if not os.path.exists(new_sub):
            os.mkdir(new_sub)

        # get image names
        sub_path = '{}/{}'.format(path, sub)
        print(sub_path)
        files = os.listdir(sub_path)
        images = [file for file in files if file.endswith('jpg')]
        print(images[0])

        for image in images:
            image_path = sub_path + '/' + image
            img = Image.open(image_path)                   # open image
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize((224, 224), Image.ANTIALIAS)  # resize and set quality
            new_image_path = new_sub + '/' + image
            img.save(new_image_path, optimize=True, quality=95)

compress_images()




'''plt.rcParams['figure.figsize'] = [16, 8]

# image read full color image into matrix A
A = imread('./train_images2/apple4.jpg')
X = np.mean(A, -1);  # convert RBG to grayscale

img = plt.imshow(X) # plot
img.set_cmap('gray')
plt.axis('off')
plt.show()

# compute (economy) SVD; return first m columns of U corresponding to non-zero singular values, not full square matrix
U, S, VT = np.linalg.svd(X, full_matrices=False)
S = np.daig(S) # extract diagonal singular values

j = 0
# low rank approximations at rank 5, 20, 100
for r in (5, 20, 100):
    # Construct approximate image: first r col U * rxr block sigma * first r col V transpose
    Xapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
    plt.figure(j+1)
    j += 1
    img = plt.imshow(Xapprox) # plot
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r = ' + str(r))
    plt.show()

plt.figure(1)
plt.semilogy(np.diag(S))
plt.title('Singular Values')
plt.show()

plt.figure(2)
plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S)))
plt.title('Singular Values: Cumulative Sum')
plt.show()'''
