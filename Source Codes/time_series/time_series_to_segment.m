function S = time_series_to_segment(X, M)
% X time series
% M segments
[m,n] = size(X);
[u,v] = size(M);

for i=1:m
    for j=1:u
        min_distance = inf;
        for k=1:n-v+1
            distance = norm(X(i,[k: k+v-1]) - M(j,:));
            if distance < min_distance
                min_distance = distance;
            end;
            S(i,j) = min_distance;
        end;
    end;
end;


         