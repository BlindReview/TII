function W=Phi_function(X,Y,W_t,A,namdaA,namdaI,namda,eita_t)
[f_wt,ff_wt]=ff_function(X,W_t,Y,A,namdaA,namdaI);
U_t=W_t - 1/eita_t*ff_wt;
W=[];

for j=1:size(W_t,1)
    if norm(U_t(j,:)) > namda/eita_t;
        co=1-namda/(eita_t*norm(U_t(j,:)));
        w_i=co*U_t(j,:);
        W=[W;w_i];
    else
        w_i=zeros(size(U_t(j,:)));
        W=[W;w_i];
    end
end
