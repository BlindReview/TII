function acc=accuracy(X,Y,W)
Y_hat_real=X'*W;
y=max(abs(Y_hat_real),[],2);
[mt,nt]=size(Y_hat_real);
Y_hat=zeros(mt,nt);
R=0;
for j=1:mt
    k=find(abs(Y_hat_real(j,:))==y(j));
    Y_hat(j,k)=1;
    if Y(j,k)==1
        R=R+1;
    end
end
acc=R/mt;