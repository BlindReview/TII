function F_w=F_function(X,W,Y,A,namdaA,namdaI,namda)
f_w=ff_function(X,W,Y,A,namdaA,namdaI);
F_w=f_w+namda*L21_norm(W);