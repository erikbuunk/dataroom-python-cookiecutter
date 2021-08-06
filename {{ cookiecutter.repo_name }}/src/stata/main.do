clear all

cap clear
cap log close
set more 1
set matsize 10000
set maxvar 10000

log using "results/log/main_do", t replace

/* PUT CODE HERE */

cap log close
