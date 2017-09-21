function G=G_function(X,Y,A,W,W_t,eita_t,namdaA,namdaI,namda)
[f_wt,ff_wt]=ff_function(X,W_t,Y,A,namdaA,namdaI);
G1=f_wt;
G2=trace(ff_wt'*(W-W_t));
G3=eita_t/2*Frobenius_norm(W-W_t)^2;
G4=namda*L21_norm(W);
G=G1+G2+G3+G4;

