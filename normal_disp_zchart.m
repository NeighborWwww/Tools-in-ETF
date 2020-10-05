%This program will generate a normal distribution z-score table

%Generate z table
sig = (0:0.01:0.09);
z = (0:0.1:3.9);
z_table = [];
for i = 1:length(z)
    row = [];
    for j = 1:length(sig)
        digits(5);
        row = [row normcdf(z(i)+sig(j))];
    end
    
    %Mark the row label
    row = [z(i) row];
    z_table = [z_table; row];
end
%Mark the colume label
r = ["z",string(sig)];
%Generate z-table
T = array2table(z_table, 'VariableNames', r);
%Output the table file
writetable(T,'Ztable.xlsx');