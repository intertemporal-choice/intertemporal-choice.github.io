function  [value] = ExpectedExact(stigmastar);
% NOTES:
% 1. Exact expected value that corresponds to \[DoubleStruckCapitalE]\[GothicCapitalR]ToTheOneMinusRhoExact 
% in C-With-Optimal-Portfolio Handout
% 2. Risky retun has a lognormal distribution
% 3. Integration is calculated based on Gauss-Hermite Quadrature
%==========================================================================
% Inputs:
%   1. Global
%       mu      Mean for the log normal distribution
%       sigma   STD for the log normal distribution
%       n       Number of Nodes that will be used to evaluate integral
%       Rfree   Risk Free Rate for the Portfolio Problem
%       Rho_1   CRRA Parameter coming from CRRA Utility Function
%   2. Local
%       stigmastar  Optimal Share of risky asset in the Portfolio Problem
%       that comes from FOC Condition
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
fy = (Rfree + (exp(y) - Rfree) * stigmastar).^(1 - Rho_1);
value = pi^(-1/2) * sum(fy.* z_weights);
end