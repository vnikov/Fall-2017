A = [4 -2 5 -5 ; -9 7 -8 0 ; -6 4 5 3 ; 5 -3 8 -4] % Matrix A of part (a)
rref([A [0;0;0;0]]) % Find the rref of the augmented matrix, which gives 
                    % the answer to part(i).
rref([A [7;5;9;7]]) % Find the rref of the augmented matrix, which gives
                    % the x under the image b of transformation.
                    
B = [-9 -4 -9 4 ; 5 -8 -7 6 ; 7 11 16 -9 ; 9 -7 -4 5] % Matrix A of part (b)
rref([B [0;0;0;0]]) % Find the rref of the augmented matrix, which gives 
                    % the answer to part(i).
rref([B [-7;-7;13;-5]]) % Find the rref of the augmented matrix, which gives
                        % the x under the image b of transformation.