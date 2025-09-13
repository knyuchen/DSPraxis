function exercise_1()
    fprintf('=== Exercise 1: Basic Matrix Operations ===\n');
    
    % Create matrices
    A = [1, 2, 3; 4, 5, 6; 7, 8, 9];
    B = ones(3, 3);
    v = [1; 2; 3];
    
    fprintf('Matrix A:\n');
    disp(A);
    
    fprintf('Matrix B (ones):\n');
    disp(B);
    
    fprintf('Vector v:\n');
    disp(v);
    
    % Basic operations
    C = A + B;
    D = A * B;
    E = A .* B;  % Element-wise multiplication
    
    fprintf('A + B:\n');
    disp(C);
    
    fprintf('A * B (matrix multiplication):\n');
    disp(D);
    
    fprintf('A .* B (element-wise multiplication):\n');
    disp(E);
    
    % Matrix-vector operations
    result = A * v;
    fprintf('A * v:\n');
    disp(result);
    
    fprintf('Exercise 1 completed.\n\n');
end
