function [f_w,ff_w]=ff_function(X,W,Y,A,namdaA,namdaI)
D=zeros(size(A));
for j=1:size(A,1)
    D(j,j)=sum(A(j,:));
end
L=D-A;

M1=X'*W-Y;
M2=W;
M3=W'*X*L*X'*W;
f_w=1/2*Frobenius_norm(M1)^2+namdaA/2*Frobenius_norm(M2)^2+namdaI/2*trace(M3);
ff_w=X*X'*W-X*Y+namdaA*W+namdaI*X*L*X'*W;