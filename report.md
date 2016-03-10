UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** Loo Li Ping**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/graceloo94/UECM3033_assign2](https://github.com/graceloo94/UECM3033_assign2)

Explain your selection criteria here.
In order to decide which method to solve for matrix A, we will need to check if matrix A is positive definite. We can find the eigenvalues of A and check if A is symmetry to determine if it is positive definite. SOR method will be used if matrix A is positive definite, else,  LU decomposition will be used. In order to use SOR method, matrix A needs to be positive definite to find an optimal ω that will converge. 

Explain how you implement your `task1.py` here.


---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Watchtower_coast.jpg)

![Watchtower_coast.jpg](Watchtower_coast.jpg)

How many non zero element in $\Sigma$?
All the elements (R,G,B) in $\Sigma$  are non zero elements.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

Original image:
![original.png](original.png)

Lower resolution picture: $\Sigma_{30}$
![svd_30.png](svd_30.png)

Better resolution picture : $\Sigma_{200}$
![svd_200.png](svd_200.png)

A chosen image with resolution of 1000x800 pixels is uploaded and read in the r,g,b format which is a 3 dimensional matrix. Then, we find the U,$\Sigma$ and V of the red, green, blue matrices respectively by using scipy.linalg.svd. Next, we find the non zero elements in $\Sigma$ by using numpy.count_nonzero. A lower resolution matrix is formed by keeping the first 30 non zero elements in $\Sigma$, and setting the other non zero elements to zero. The process can be repeated to find a better resolution matrix for the image as shown in the figures above.

To prevent any loss of information for the matrix, we first create a copy of the original $\Sigma$ for all the red, green blue matrices such as Sred.copy. After this, we will start to keep the first n non zero elements and setting the others to zero. The new $\Sigma$ generated for each r, g, b matrices is then converted from (800,1) into (800,1000) by using scipy.linalg.diagsvd to perform dot multiplication for U,$\Sigma$,V by using numpy.dot. Thus, a new matrix can be created to generate images of lower or better resolutions.


What is a sparse matrix?
A sparse matrix is a matrix whereby most of the elements are zero. The matrix is considered dense if most of the elements are nonzero. In task 1, when the first 30 elements of $\Sigma$ is kept, and all the other elements are set to zero, a sparse matrix is formed. The dimension of $\Sigma$ is changed from (800,1) to (800,1000). Thus, a large sparse matrix of (800,1000) is formed. When combining U and V using dot multiplication, a lower resolution pictures is created.

-----------------------------------

<sup>last modified: 11 March 2016</sup>

