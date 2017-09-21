function record = trace_sort(u)
    [m,n] = size(u);
    for i=1: n
        record(i) = i;
    end;
    

    for i=1:n
        for j=1:n-i
            if u(j+1) >u(j)
                temp = u(j);
                u(j) = u(j+1);
                u(j+1) = temp;
                
                swap = record(j);
                record(j) = record(j+1);
                record(j+1) = swap;
            end
        end;
    end;
    
    


