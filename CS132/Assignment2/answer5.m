%%%% Part (a) %%%%

B = [8 -3 2;-9 4 -7;6 -2 4;5 -1 10]
rref([B, [0;0;0;0]])
result_B = B*[0;0;0]
% Explanation: I choose the first, second, and the fifth column of
% the matrix A, then use rref() to check whether the augmented matrix
% of B and[0;0;0;0], which is equvalent to Bx = 0, has only the trivial
% solution or not. 

%%%% Part (a) %%%%

%%%% Part (b) %%%%

C = [10 -3 7 10;-6 7 -9 5;9 -5 6 -1;-3 6 -8 9;7 -9 11 -8]
rref([C, [0;0;0;0;0]])
result_C = C*[0;0;0;0]
% Explanation: I choose the second, the fourth, the fifth, and the
% sixth column of the matrix A,then use rref() to check whether the 
% augmented matrix of B and[0;0;0;0;0], which is equvalent to Bx = 0
% , has only the trivial solution or not. 

%%%% Part (b) %%%%