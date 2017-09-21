function w_f=Frobenius_norm(w)
[m,n]=size(w);
s=[];
for j=1:m
    s(j)=norm(w(j,:));
    s(j)=s(j)^2;
end
w_f=sqrt(sum(s));