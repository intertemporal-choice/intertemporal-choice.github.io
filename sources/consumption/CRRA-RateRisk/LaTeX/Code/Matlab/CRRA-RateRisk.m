% Emek Karaca
% Replication of Figures in CRRA-RateRisk-Derivations Handout
% Novermber 22, 2012
%
% NOTEs:
% 1. I try to use the same notation as the CRRA-RateRisk-Derivations.nb code
% as much as I can.
% 2. Parameters are defined separetly for 2 different figures to make the code
% easier to read

% Housekeeping
clear all;
close all;
clc;

% Parameters
% NOTE:     _1 is for figure 1
%           _2 is for figure 2 
Sigma_GothicR_1 = 0.1;
Sigma_GothicR_2 = [0:0.0001:0.2]';
GothicR = 0.05; 
CurlyTheta = 0.05;
Beta = 1/(1 + CurlyTheta);
Rho_1 = [1:0.001:5]';
Rho_2 = 3; 
% Assigning the Specific Locations
Location = 1;                       % 1 for My Laptop
                                    % 2 for Desktop

% Approximations and Exact Results for Figure 1
E_GothicCapitalR_Part_1 = exp((1 - Rho_1).* GothicR - Rho_1.* (1 - Rho_1).* ...
    Sigma_GothicR_1^2 / 2); 
Kappa_Exact_1 = 1 - (Beta * E_GothicCapitalR_Part_1).^((Rho_1).^(-1));
Kappa_ApproxApprox_1 = - GothicR * (-1 + (Rho_1).^(-1)) + CurlyTheta * ...
    (Rho_1).^(-1) + 1 / 2 * (1 - Rho_1).* Sigma_GothicR_1^2;
Kappa_Error_1 = Kappa_Exact_1 - Kappa_ApproxApprox_1;

% Plot Figure 1
figure(1)
plot(Rho_1, Kappa_Exact_1, '-k', 'LineWidth', 3);
hold on
plot(Rho_1, Kappa_ApproxApprox_1, '--k', 'LineWidth', 2);
set(gca,'XLim',[1 5]);
set(gca,'XTick',[1:1:5]);
set(gca,'YLim',[0.03 0.05]);
set(gca,'YTick',[0.03:0.005:0.05]);
xlabel('\rho', 'fontsize', 12, 'fontweight', 'b', 'color','k');
ylabel('\kappa', 'fontsize', 12, 'fontweight', 'b', 'color','k');
h = legend('Exact','Approximation',1);
set(h,'Interpreter','none');
set(h,'fontsize',12);
% Save the figure to a specific location in my computer
if Location == 1;
    saveas(gcf, 'E:\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure1', 'epsc');
else
    saveas(gcf, 'C:My Documents\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure1', 'epsc');
end

% Approximations and Exact Results for Figure 2
E_GothicCapitalR_Part_2 = exp((1 - Rho_2) * GothicR - Rho_2 * (1 - Rho_2) * ...
    Sigma_GothicR_2.^2/ 2);
Kappa_Exact_2 = 1 - (Beta * E_GothicCapitalR_Part_2).^((Rho_2)^(-1));
Kappa_ApproxApprox_2 = - GothicR * (-1 + (Rho_2)^(-1)) + CurlyTheta * (Rho_2)^(-1) + 1 / 2 * (1 - Rho_2)* Sigma_GothicR_2.^2;
Kappa_Error_2 = Kappa_Exact_2 - Kappa_ApproxApprox_2;

% Figure 2
figure(2)
plot(Sigma_GothicR_2, Kappa_Exact_2, '-k', 'LineWidth', 3);
hold on
plot(Sigma_GothicR_2, Kappa_ApproxApprox_2, '--k', 'LineWidth', 2);
set(gca,'XLim',[0 0.20]);
set(gca,'XTick',[0:0.05:0.20]);
set(gca,'YLim',[0.00 0.06]);
set(gca,'YTick',[0.00:0.01:0.06]);
xlabel('\sigma_r', 'fontsize', 12, 'fontweight', 'b', 'color','k');
ylabel('\kappa', 'fontsize', 12, 'fontweight', 'b', 'color','k');
h = legend('Exact','Approximation',1);
set(h,'Interpreter','none');
set(h,'fontsize',12)
if Location == 1;
    saveas(gcf, 'E:\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure2', 'epsc');
else
    saveas(gcf, 'C:My Documents\Dropbox\emek\UandEA\Meetings\C. Carroll\To Do List\November 20 Meeting\FRvsUR\figure1', 'epsc');
end

