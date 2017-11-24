# Image-Gradient-and-Edge-Detection

Author: Shivangi Motwani

To run the program: python task_final_version.py input_file.ppm
where, input_file.ppm is any file input file in ppm format.

This code reads the ppm image files and outputs the image gradient using Sobel 
operator and detects edges based of Laplacian operator.

References for this code will be displayed at the end of program and also 
the name of file in which output is stored will be displayed.

Task:
1) Write a C++ (or python) program to read in a PPM file with "P6" encoding [ASCII files].
2) Store the image as an object of an Image class.
3) Use finite difference formulae to find colour gradients at each pixel of the input image.
4) Use second order derivatives of pixel colour to find which pixels belong to edges.
5) Output an image object where pixels on edges are coloured white (1,1,1) and others are coloured black (0,0,0), in the form of a PPM file with P6 encoding.
Note: The colours are specified as on RGB model.

Road Map:
1) Read PMM image
2) Decode it(Unable to understand, p6 coding)
3) Use Sobel operator for image gradient =>  Hx = [[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]]and Hy = [[-1., -2., -1.], [0., 0., 0.], [1., 2., 1.]]
4) Use Laplacian operator for edge detection => H = [1 1 1; 1 -8 1; 1 1 1] or [0 1 0; 1 -4 1; 0 1 0] 
5) Save it in ppm file(Unable to get what it means)


References:
https://stackoverflow.com/questions/22946241/using-python-3-x-to-properly-read-ppm-files

https://www.researchgate.net/post/What_are_the_differences_in_first_order_derivative_edge_detection_algorithms_and_second_order_edge_detection_algorithms

https://dsp.stackexchange.com/questions/10605/kernels-to-compute-second-order-derivative-of-digital-image

http://paulbourke.net/dataformats/ppm/

https://stackoverflow.com/questions/2448015/2d-convolution-using-python-and-numpy

https://www.youtube.com/watch?v=bc0NYna3swE
