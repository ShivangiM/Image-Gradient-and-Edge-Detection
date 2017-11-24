import PIL
import matplotlib
from PIL import Image
import numpy as np
import os
import sys

print("*"*50)
print("System Info : " + str(sys.version))
print("Files/Folders in this Directory : " + str(os.listdir("./")) + "\n")
print("Numpy Version : " + str(np.__version__))
print("PIL Version : " + str(PIL.__version__))
print("*"*50)

# Taking input File as argument
inFile = sys.argv[1]

# Open the PPM File and get the image object
def open_ppm_file(filename):
    with open(filename, 'r') as ppm:
        d_file = ppm.read()
    encoding, height, width, max_v,*values_1 = d_file.split()
    # print(encoding)
    # print(height)
    # print(width)
    # print(max_v)
    # print(int(height)*int(width))
    # print(len(values_1))

    s_values = values_1
    values = []
    for i in s_values:
        values.append(int(i))

    rgb = [tuple(values[i:i+3]) for i in range(0, len(values), 3)]
    
    img_flat = []
    for i in rgb:
        pixel = int((int(i[0]) + int(i[1]) + int(i[2])))
        img_flat.append(pixel)

    # Reshaping
    data = np.reshape(img_flat, (int(width),int(height)))

    print(data.shape)

    img = data
    
    return img


#Image object
img = open_ppm_file(inFile)

# Convolution for getting Image Gradient and Edge Detection
def convolution2d(image, kernel):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
    return new_image

# Finding Image Gradient
go_x = np.array([[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]]) #Gradient Operator x
go_y = np.array([[-1., -2., -1.], [0., 0., 0.], [1., 2., 1.]]) #Gradient Operator y

gx = convolution2d(img, go_x)
gy = convolution2d(img, go_y)

# IG = np.sqrt(gx + gy) #Not doing square root as it gives poor results
IG_add = gx + gy

#Showing the gradients 
img_IG_add = Image.fromarray(IG_add)
img_IG_add.show(title="IG")

second_d_operator = np.array([[0., 1., 0.], [1., -4., 1.], [0., 1., 0.]])
DE = convolution2d(img, second_d_operator) # Detected Edges

img_secondDerivative = Image.fromarray(DE)
img_secondDerivative.show(title="SE")

#Function to write PPM file
def write_ppm_file(img, filename,encoding):
    height = img.shape[1]
    width = img.shape[0]
    max_value = img.max()
    with open(filename, 'a') as f:
        f.write(str(encoding) + "\n")
        f.write(str(height) + "\n")
        f.write(str(width) + "\n")
        f.write(str(max_value) + "\n")
        for i in range(0,height):
            for j in range(0, width):
                if img[i][j] > 150:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
                f.write(str(int(img[i][j])) + " " + str(int(img[i][j])) + " " + str(int(img[i][j])) + " ")
            f.write("\n")
    print("Written to file " + str(filename))
    return("Written to file " + str(filename))

write_ppm_file(IG_add, "output_IG.ppm", "P3")
write_ppm_file(DE,"output_DE.ppm","P3")

# references = ["https://stackoverflow.com/questions/22946241/using-python-3-x-to-properly-read-ppm-files","https://www.researchgate.net/post/What_are_the_differences_in_first_order_derivative_edge_detection_algorithms_and_second_order_edge_detection_algorithms","https://dsp.stackexchange.com/questions/10605/kernels-to-compute-second-order-derivative-of-digital-image","http://paulbourke.net/dataformats/ppm/","https://stackoverflow.com/questions/2448015/2d-convolution-using-python-and-numpy","https://www.youtube.com/watch?v=bc0NYna3swE"]

# print("References : " + str(references))

