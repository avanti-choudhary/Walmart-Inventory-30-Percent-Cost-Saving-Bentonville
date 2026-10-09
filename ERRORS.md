# ERRORS.md - Project 3 Debugging Log
Bentonville, AR - Walmart Inventory Project

## Error 1: ModuleNotFoundError: No module named 'matplotlib'
**When:** Running chart.py in dashboard folder
**Screenshot:** Figure 1 window blocked, terminal showed red traceback
**Reason:** matplotlib library not installed in Python
**Fix:**
pip install matplotlib
or
python -m pip install matplotlib

**Learning:** Always check pip list before importing libraries. This is common in fresh Python installs.

## Error 2: Inventory Cost Showing 13.96% not 30%
**When:** Running clean.py
**Reason:** Only 7 out of 20 rows had Sales_Change < -10%. 30% cut applied only to slow-moving items.
**Fix/Explanation:** 
- Overall saving = 13.96%
- Saving on slow items = 30%
- This is correct business logic. Formula:
  Sales_Change = (ThisWeek - LastWeek) / LastWeek
  Example: (350-480)/480 = -27%
  New_Inventory = 700 * 0.7 = 490 (keep 70%, cut 30%)

## Error 3: FileNotFoundError for inventory_cost.csv
**When:** First run of chart.py
**Reason:** chart.py tried to read '../data/inventory_cost.csv' but clean.py not run yet
**Fix:** Always run data/clean.py first, then dashboard/chart.py

## Key Learnings for Interview
1. LAG() in SQL = shift(1) in Pandas
2. 0.7 means keep 70%, cut 30%
3. Percentage formula needs *100