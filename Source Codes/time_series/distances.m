function U = distances(X_omega)

[num,num2] = size(X_omega);

for i=1: num
    for j=1:num
        U(i,j)= norm(X_omega(i,:) - X_omega(j,:));
    end;
end;


for i=1:num
    for j=1:num
       if (i ~= j)
           U(i,i) = U(i,i) + U(i,j);
       end;
    end;
end;




        



