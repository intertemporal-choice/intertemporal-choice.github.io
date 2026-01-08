clear
version 10
set memory 200m
set more off
capture log close
*log using StickyECStata, replace

*consider the time periods from t-2 to t+7. There is a one-time shock at t.
set obs 10
gen t=_n-3  //generate time variable t

*Omniscient Consumers
gen r=0.05  //set interest rate at 5%
gen shock=r/(r+1) //the shock for consumption
local r_R=shock
gen consum_O=shock*(t>=0) //consumption path
gen B_O=1*(t>0)  //bank balance path
*make the two scatter plots and combine them
scatter consum_O t,msize(medlarge) msymbol(O) title("Figure 1 Path of Consumption after a shock, Ominiscient Consumers") name(CO,replace) ///
ylabel(none `r_R' "r/R") xlabel(none -2 "t-2" -1 "t-1" 0 "t" 1 "t+1" 2 "t+2" 3 "t+3" 4 "t+4" 5 "t+5" 6 "t+6" 7 "t+7") xtitle("Time") ytitle("c")
scatter B_O t,msize(medlarge) msymbol(O) title("Figure 2 Path of B after a shock, Omniscient Consumers") name(BO,replace) ///
ylabel(0.0(0.2)1.0) ymtick(##5) xlabel(none -2 "t-2" -1 "t-1" 0 "t" 1 "t+1" 2 "t+2" 3 "t+3" 4 "t+4" 5 "t+5" 6 "t+6" 7 "t+7") xtitle("Time") ytitle("b")
graph combine CO BO, rows(2)
graph save Omniscient_consumers,replace

*Consumers with sticky expectations
gen PI=0.5
*generate consumption path for people with sticky expectation
gen consum_se=(_n==3)*PI*shock
replace consum_se=consum_se[_n-1]+(1-PI)*(1+r)*(consum_se[_n-1]-consum_se[_n-2]) if _n>=4
*generate bank balance path for people with sticky expectation
gen B_se=(_n==4)*(1+(consum_O-consum_se)*(1+r))
replace B_se=(B_se[_n-1]-consum_se[_n-1])*(1+r) if _n>4
*make the two scatter plots and combine them
scatter consum_O consum_se t,msize(medlarge medlarge) msymbol(O O) title("Figure 3 Path of Consumption after a shock, Sticky Expectations") name(Cse,replace) ///
ylabel(none `r_R' "r/R") xlabel(none -2 "t-2" -1 "t-1" 0 "t" 1 "t+1" 2 "t+2" 3 "t+3" 4 "t+4" 5 "t+5" 6 "t+6" 7 "t+7") xtitle("Time") ytitle("c") ///
legend(label(1 "omniscient") label(2 "sticky expectation"))
scatter B_O B_se t,msize(medlarge medlarge) msymbol(O O) title("Figure 4 Path of B after a shock, Sticky Expectations") name(Bse,replace) ///
ylabel(0.0(0.2)1.0) ymtick(##5) xlabel(none -2 "t-2" -1 "t-1" 0 "t" 1 "t+1" 2 "t+2" 3 "t+3" 4 "t+4" 5 "t+5" 6 "t+6" 7 "t+7") xtitle("Time") ytitle("b") ///
legend(label(1 "omniscient") label(2 "sticky expectation"))
graph combine Cse Bse, rows(2)
graph save StickyExpectation_Consumers,replace

*log close
exit
