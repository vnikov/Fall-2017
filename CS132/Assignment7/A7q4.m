A = [1 1 0;1 1 0;1 1 0;1 0 1;1 0 1;1 0 1]
b = [7;2;3;6;5;4]
X = rref([A'*A A'*b]) % An augnemted matrix