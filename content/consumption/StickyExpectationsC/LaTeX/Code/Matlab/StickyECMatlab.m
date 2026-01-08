clc;
clear;

%Replicating the graphs on the file of Sticky Expectations and Consumption
%Dynamics 

%Defining the parameters of the model. All the values X_0 are initial
%values of the variables studied
r=.05;
R=1+r;
y_0=1;
b_0=0;
p_0=1;
G=1;
theta_0=1;
psi_0=1;
h_0=(1)/(1-(1/1.05));
lambda=.5;
theta_t=theta_0;

%Defining the value od c_0
c_0=(b_0+(theta_0-1).*p_0+h_0)*(r*R^-1);

%Defining the initial values of variables with some people presenting
%Sticky Expectations
c_sticky=c_0;
b_sticky=b_0;
deltac0=0;

%Since all variables at time t+1 depends on variables in period t, we
%generate a loop to calculate the vector of variables at t+1

for t=1:1:11
   
   %We know that the shock happens on period t (period 3, since we start in
   %period t-2)
   if t==3;
       theta_t=2;
       epsilon=lambda*(r/R);
   else
       theta_t=1;
       epsilon=0;
   end
   
   %Generating the values in period t of all variables of interest these
   %values are the ones of the form x(t), After we generate these values we
   %re-state the values of the variables at t, x_0=x(t). The variables X
   %are the variables for the perfect foresight model, meanwhile the
   %variables xs correspond to the sticky expectations model.
   
   p(t)=G*p_0*psi_0;
   h(t)=(p(t)/(1-(G/R)));
   b(t)=(b_0+y_0-c_0)*R;
   c(t)=(b(t)+(theta_t-1).*p(t)+h(t))*(r/R);
   y_0=p(t)*theta_t;
   deltac(t)=deltac0*(1-lambda).*R+epsilon;
   cs(t)=c_sticky+deltac(t);
   bs(t)=(b_sticky+y_0-c_sticky)*R;
   b_0=b(t);
   b_sticky=bs(t);
   p_0=p(t);
   c_0=c(t);
   deltac0=deltac(t);
   c_sticky=cs(t);
  
 
end

t=(1:1:11);

hold on
%How to re-name the axes with words instead of numbers.
set(gca,'XTickLabel',{'t-2','t-1','t','t+1','t+2','t+3','t+4','t+5','t+6','t+7','t+8'})
plot(t,c,'or'),title('Path of C after a shock \theta ; Sticky Expectations in Red')
plot(t,cs,'o')
hold off

figure %how to keep more than one graph open.
hold on
set(gca,'XTickLabel',{'t-2','t-1','t','t+1','t+2','t+3','t+4','t+5','t+6','t+7','t+8'})
plot(t,b,'or'), title('Path of B after a shock \theta ; Sticky Expectations in Red')
plot(t,bs,'o')
hold off
   
   
