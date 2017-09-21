function [M, location] = trace_max(U, X_omega, rho, rows, columns)

[num, num2] = size(U);

vector = zeros(1, num);

for i=1: num
    vector(i) = U(i,i);
end;

record = trace_sort(vector);
    
for i=1: rho   
   location(i,1) = fix(record(i)/columns) ;
   location(i,2) = mod(record(i), columns);
   M(i,:) = X_omega(record(i),:);
end


