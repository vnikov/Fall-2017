D = dlmread('Question6matlabData.txt')
A = D(:,1,1)
Y = D(:,2,1)
scatter(A, Y)
hold on;
A = [ones(size(A, 1), 1) A sin(0.5.*pi.*A)]
ANS = inv(A'*A)*A'*Y
plot(A, ANS(1) + ANS(2)*A + ANS(3)*sin(0.5*pi*A), 'r', 'LineWidth', 3)