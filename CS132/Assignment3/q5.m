%% Part a %%
A = [1/6 1/2 1/3 ; 1/2 1/4 1/4 ; 1/3 1/4 5/12]
A5 = A^5
A10 = A^10
A20 = A^20
A30 = A^30
%% Part a %%

%% Part b %%
% Section i %
I = [1 0 0 0 ; 0 1 0 0 ; 0 0 1 0 ; 0 0 0 1]
A = rand(4)
result1 = ((A + I)*(A - I)) - (A^2 -I)
A = rand(4)
result2 = ((A + I)*(A - I)) - (A^2 -I)
A = rand(4)
result3 = ((A + I)*(A - I)) - (A^2 -I)
A = rand(4)
result4 = ((A + I)*(A - I)) - (A^2 -I)

A = randi([1 50],4,4) % Random the 4x4 integer matrix
result5 = ((A + I)*(A - I)) - (A^2 -I)
% Section i %

% Section ii %
A = rand(4)
B = rand(4)
result1 = ((A + B)*(A - B)) - (A^2 - B^2)
A = rand(4)
B = rand(4)
result2 = ((A + B)*(A - B)) - (A^2 - B^2)
A = rand(4)
B = rand(4)
result3 = ((A + B)*(A - B)) - (A^2 - B^2)

A = randi([1 50],4,4) % Random the 4x4 integer matrix
B = randi([1 50],4,4) % Random the 4x4 integer matrix
result4 = ((A + B)*(A - B)) - (A^2 - B^2)
% Section ii%

% Section iii %
S = [0 1 0 0 0 ; 0 0 1 0 0 ; 0 0 0 1 0 ; 0 0 0 0 1 ; 0 0 0 0 0]
S2 = S^2
S3 = S^3
S4 = S^4
S5 = S^5
S6 = S^6
% Section iii %
%% Part b %%