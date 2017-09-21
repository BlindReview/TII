function[TS, Network, Y] = read_data()
clc;
clear;

%%%%%%%%%%%% Time Series matrix %%%%%%%%%%%%
f_ts = fopen('matrix_TS.dat', 'r');
i = 1;
while ~feof(f_ts)
    ts = fgetl(f_ts);
    ts = deblank(ts);
    S = regexp(ts, ',', 'split');
    for j = 1:length(S)
        xx = eval(S{j});
        TS(i,j) = xx;
    end
    i = i + 1;
end

timeseries_size = size(TS)

%%%%%%%%%%%% Network matrix %%%%%%%%%%%%
f_ts = fopen('matrix_network.dat', 'r');
i = 1;
while ~feof(f_ts)
    ts = fgetl(f_ts);
    ts = deblank(ts);
    S = regexp(ts, ',', 'split');
    for j = 1:length(S)
        xx = eval(S{j});
        Network(i,j) = xx;
    end
    i = i + 1;
end

Network_size = size(Network)

%%%%%%%%%%%% Label matrix %%%%%%%%%%%%
f_ts = fopen('matrix_Y.dat', 'r');
i = 1;
while ~feof(f_ts)
    ts = fgetl(f_ts);
    ts = deblank(ts);
    S = regexp(ts, ',', 'split');
    for j = 1:length(S)
        xx = eval(S{j});
        Y(i,j) = xx;
    end
    i = i + 1;
end

Label_size = size(Y)