img_in=double((rgb2gray(imread('BU.jpg'))));
image(img_in)
[V,D] = eig(cov(img_in))
image((V(:,1:400)*V(:,1:400)'*img_in')')