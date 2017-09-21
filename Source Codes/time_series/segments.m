function X_omega = segments(X, window)
%input time series data X, generate a segment space Xomega
%l is the length of shapelets
[row, column] = size(X); 
X_omega = zeros(row*(column-window+1), window);
u=1; 
for i=1: row
    for j=1: column-window+1
        for k = 1: window
            X_omega(u, k) = X(i, j+k-1);
        end;
        u = u+1; 
    end;
end;




