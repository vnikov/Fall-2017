x=linspace(0,10,1000)';
y=6+5*x+3*x.^2+3*x.^3+x.^3.*rand(size(x));
plot(x,y,'bo')
hold on;
A = [ones(1000, 1) x x.^2 x.^3]
ANS = inv(A' * A)*A'*y
plot(x, ANS(1) + ANS(2)*x + ANS(3)*x.^2 + ANS(4)*x.^3, 'r', 'LineWidth', 3)