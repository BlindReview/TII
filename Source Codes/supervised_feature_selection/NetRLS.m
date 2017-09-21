function [acc_train, acc_test, W_tp1] = NetRLS(Xtrain, Ytrain, Network, Xtest, Ytest, namdaA, namdaI, namda)

%inatialize;
X=Xtrain;
Y=Ytrain;
A=Network;
[mx,nx]=size(X);
[my,ny]=size(Y);
W1=ones(mx,ny);
V1=W1;
eita0=1;
alpha1=2;
gama=2;
epsilon=0.01;

epsilon_t=epsilon+1;
W_t=W1;
alpha_t=alpha1;
eita_tm1=eita0;
V_t=V1;
while epsilon_t>epsilon
    phi=Phi_function(X,Y,W_t,A,namdaA,namdaI,namda,eita_tm1);
    F_phi=F_function(X,phi,Y,A,namdaA,namdaI,namda);
    G_phi=G_function(X,Y,A,phi,W_t,eita_tm1,namdaA,namdaI,namda);
    while F_phi>G_phi
        eita_tm1=gama*eita_tm1;
        phi=Phi_function(X,Y,W_t,A,namdaA,namdaI,namda,eita_tm1);
        F_phi=F_function(X,phi,Y,A,namdaA,namdaI,namda);
        G_phi=G_function(X,Y,A,phi,W_t,eita_tm1,namdaA,namdaI,namda);
    end
    eita_t=eita_tm1;
    W_tp1=Phi_function(X,Y,V_t,A,namdaA,namdaI,namda,eita_t);
    alpha_tp1=(1+sqrt(1+4*alpha_t^2))/2;
    V_tp1=W_t+(alpha_t-1)/alpha_tp1*(W_tp1-W_t);
    epsilon_t=Frobenius_norm(W_tp1-W_t);  
    
    alpha_t=alpha_tp1;
    W_t=W_tp1;
    eita_tm1=eita_t;
    V_t=V_tp1;
 
end

acc_train=accuracy(Xtrain,Ytrain,W_tp1);
acc_test=accuracy(Xtest,Ytest,W_tp1);    


