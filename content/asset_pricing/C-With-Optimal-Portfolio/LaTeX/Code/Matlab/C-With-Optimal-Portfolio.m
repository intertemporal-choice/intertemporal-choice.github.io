% Emek Karaca
% Replication of Figures in C-With-Optimal-Portfolio Handout
% Novermber 22, 2012
%
% NOTEs:
% 1. I try to use the same notation as the CRRA-RateRisk-Derivations.nb code
% as much as I can.
% 2. Parameters are defined separetly for 2 different figures to make the code
% easier to read
% 3. This Program calls 3 functions: 
%   i. ExpectedExact.m - calculates the exact integral of
%   \[DoubleStruckCapitalE]\[GothicCapitalR]ToTheOneMinusRhoExact in the
%   handout based on Gauss-Hermite quadrature
%   ii. FOCforExpectedExact.m - calcultes the First Order Condition of
%   \[DoubleStruckCapitalE]\[GothicCapitalR]ToTheOneMinusRhoExact
%   iii. GaussHermite.m - gives the nodes of Gauss-Hermite quadrature based
%   on n nodes (assumed to be 10 in the below m file)
%==========================================================================


% Housekeeping
clear all;
close all;
clc;

% Parameters
% NOTE:     _1 is for figure 1
%           _2 is for figure 2 
%   Declare Globals
global mu sigma Rfree Rho_1 n
%   Assign Parameter Values
Rho_1 = 3;
Rho_2 = [1:0.001:2]';
rfree = 0.02;
Rfree = exp(rfree);
ScriptR = 0.05;
CurlyTheta = 0.02;                  
Beta = exp(-CurlyTheta);
phi = ScriptR - rfree;
        % sigma_r = [0.10:0.001:0.2]';
Sigma_1 = [0.10:0.001:0.2]';
Sigma_2 = 0.2;
n = 10;                             % The number of nodes for Gauss Hermite Quadrature
        % stigma0 = 0;
stigma_init = 0;
        % sigma = sigma_r;
% Assign the Specific Locations
Location = 1;                       % 1 for My Laptop
                                    % 2 for Desktop

% Numerical Computation of the Exact and Approximated Formula for Figure 1
options = optimset('Display','iter');       % Option to display output
%   Optimization Loop
for inc = 1:size(Sigma_1,1);
    sigma = Sigma_1(inc);
    mu = ScriptR - sigma^2/2;       % Mean of LogNormalDistribution that is used to calculate 
                                    % \[DoubleStruckCapitalE]\[GothicCapitalR]ToTheOneMinusRhoExact 
                                    % in C-With-Optimal-Portfolio.nb file
                                    % or E_GothicCapitalR in my notation
    [stigma_1(inc,1), fval_1(inc,1)] = fsolve(@FOCforExpectedExact, stigma_init, options);
    E_GothicCapitalR_1(inc,1) = ExpectedExact(stigma_1(inc,1));
    Kappa_Approx_1(inc,1) = (Rho_1^(-1) * CurlyTheta + (1 - Rho_1^(-1)) * (rfree + phi^2 /(2 * sigma^2 * Rho_1)));
    Kappa_Exact_1(inc,1) = 1 - (Beta * E_GothicCapitalR_1(inc,1)).^((Rho_1)^(-1));
end

% Figure 1
figure(1)
plot(Sigma_1, Kappa_Exact_1, '-k', 'LineWidth', 2);
hold on
plot(Sigma_1, Kappa_Approx_1, '-r', 'LineWidth', 2);
set(gca,'XLim',[0.10 0.20]);
set(gca,'XTick',[0.10:0.02:0.20]);
set(gca,'YLim',[0.022 0.030]);
set(gca,'YTick',[0.022:0.002:0.030]);
xlabel('\sigma', 'fontsize', 12, 'fontweight', 'b', 'color','k');
ylabel('\kappa', 'fontsize', 12, 'fontweight', 'b', 'color','k');
h = legend('Exact','Approximation',1);
set(h,'Interpreter','none');
set(h,'fontsize',12);
if Location == 1;
    saveas(gcf, 'E:\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure6', 'epsc');
else
    saveas(gcf, 'C:\My Documents\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure6', 'epsc');
end


% Numerical Computation of the Exact and Approximated Formula for Figure 2
%   New Parameters
mu = ScriptR - Sigma_2^2/2;
sigma = Sigma_2;                % Redifne the global sigma
%   Optimization Loop
for inc = 1:size(Rho_2,1);
    Rho_1 = Rho_2(inc,1);
    [stigma_2(inc,1), fval_2(inc,1)] = fsolve(@FOCforExpectedExact, stigma_init, options);
    E_GothicCapitalR_2(inc,1) = ExpectedExact(stigma_2(inc,1));
    Kappa_Approx_2(inc,1) = (Rho_1^(-1) * CurlyTheta + (1 - Rho_1^(-1)) * (rfree + phi^2 /(2 * sigma^2 * Rho_1)));
    Kappa_Exact_2(inc,1) = 1 - (Beta * E_GothicCapitalR_2(inc,1)).^((Rho_1)^(-1));
end

% Figure 2
figure(2)
plot(Rho_2, Kappa_Exact_2, '-k', 'LineWidth', 2);
hold on
plot(Rho_2, Kappa_Approx_2, '-r', 'LineWidth', 2);
set(gca,'XLim',[1 2]);
set(gca,'XTick',[1:0.2:2]);
set(gca,'YLim',[0.0195 0.023]);
set(gca,'YTick',[0.0195:0.0005:0.023]);
xlabel('\rho', 'fontsize', 12, 'fontweight', 'b', 'color','k');
ylabel('\kappa', 'fontsize', 12, 'fontweight', 'b', 'color','k');
h = legend('Exact','Approximation',4);
set(h,'Interpreter','none');
set(h,'fontsize',12);
if Location == 1;
    saveas(gcf, 'E:\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure7', 'epsc');
else
    saveas(gcf, 'C:\My Documents\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure7', 'epsc');
end
