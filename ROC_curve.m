%Refresh the workspace
clear all; close all; clc;

%This code is use to generate a ROC curve figure
%Theta 1 for alternate hypothesis test, the variance is 1
%theta1 = [0.1 0.2 0.5 1 2 5];
ts = [[0.1,1];[1,1];[5,1];[0.1 2];[1,2];[5,2]];
z = (0:0.1:3);
%Initialize FPR (x-axis) and TPR (y-axis) array
TPR = zeros(1, length(z));
FPR = zeros(1, length(z));
lgd = string(zeros(1, length(ts)));
%Using normcdf to calculate FPR and TPR, plot the curves
%for j = (1:length(theta1))
for j = (1:length(ts))
    for i = (1:length(z))
        FPR(i) = normcdf(z(i));
        TPR(i) = normcdf(z(i), ts(j,1), ts(j,2));
    end
    %create each legend and curve
    %lgd for only question 3
    lgd(j) = strcat("mean=", string(ts(j,1)),", sd=",string(ts(j,2)));
    plot(FPR, TPR);
    hold on
end
%add legend, labels
%legend(string(theta1));
legend(string(lgd));
xlabel('FPR');
ylabel('TPR');
hold off;