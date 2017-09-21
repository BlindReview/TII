
namdaA=1;
namdaI=1;
namda=1;
window = 3; 
candidate_shapelet = 3;

[X, Network, Y] = read_data();

[rows, columns] = size(X);

X_omega = segments(X, window);
U = distances(X_omega);
[M, location] = trace_max(U, X_omega, candidate_shapelet, rows, columns)
S_train = time_series_to_segment(X,M);
S_test = S_train;

addpath(genpath('../supervised_feature_selection')); 

[acc_train, acc_test, W_tp1] = NetRLS(S_train', Y , Network, S_test', Y, namdaA, namdaI, namda);
acc_train
acc_test
W_tp1

%addpath(genpath('../data_input_output')); 
%plot(S);

b=sum(W_tp1.*W_tp1,2)
location


    


fid=fopen('test.txt','wt');%??????
matrix=S_test;                        %input_matrix??????
[m,n]=size(matrix);
 for i=1:1:m
   for j=1:1:n
      if j==n
        fprintf(fid,'%g\n',matrix(i,j));
     else
       fprintf(fid,'%g,',matrix(i,j));
      end
   end
end
fclose(fid);




