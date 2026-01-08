function  [foc] = FOCforExpectedExact(stigma);
% NOTES:
% First Order Condition for Portfolio Optmization Problem
% Risky retun has a lognormal distribution
% Integration is calculated based on Gauss-Hermite Quadrature
%==========================================================================
% Inputs:
%   1. Global
%       mu      Mean for the log normal distribution
%       sigma   STD for the log normal distribution
%       n       Number of Nodes that will be used to evaluate integral
%       Rfree   Risk Free Rate for the Portfolio Problem
%       rho     CRRA Parameter coming from CRRA Utility Function
%   2. Local
%       stigma  Share of risky asset in the Portfolio Problem
%
% Output
%   foc     First Order Condition
%==========================================================================
% Global Variables
global mu Rho_1 Rfree sigma n

% Get the Nodes
[z_nodes, z_weights] = GaussHermite(n);

% Evaluation of FOC
y = sqrt(2) * sigma * z_nodes + mu;
fy = (Rfree + (exp(y) - Rfree) * stigma).^(-Rho_1).* (exp(y) - Rfree);
foc = pi^(-1/2) * sum(fy.* z_weights);
end