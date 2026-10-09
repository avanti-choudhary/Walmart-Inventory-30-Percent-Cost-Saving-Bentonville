# Retail Inventory Optimization Model (Bentonville-Inspired) — 30% Slow-Moving Reduction Demo

> **Disclaimer: Educational Portfolio Project. NOT affiliated with Walmart Inc. Uses synthetic/sample retail data to demonstrate inventory optimization techniques inspired by Bentonville, AR retail challenges.**

### Overview
Portfolio project modeling how reducing slow-moving inventory by 30% could impact carrying costs. Built to practice SQL LAG(), Python pandas, and dashboarding for retail analytics roles.

### What I Actually Built
- Created sample dataset: `Data/inventory_cost.csv`
- Wrote cleaning logic: `Dashboard/clean.py`
- Built cost comparison logic + visualization: `Dashboard/chart.py`
- Generated chart: `Dashboard/cost_saving_chart.png` (15.7 KB)
- Logged all errors + fixes: `ERRORS.md`

### Results (On Sample Data Only)
On my sample dataset, a 30% cut in slow-moving items projected:
- **Projected Saving: $27,720**
- **Projected % Saving: 13.96% of total sample cost**
- This is a DEMO calculation, not real Walmart savings.

### Tech Stack
- Python (pandas, matplotlib)
- SQL concepts (LAG() for inventory aging)
- GitHub for version control

### Dashboard
![Cost Saving Chart](Dashboard/cost_saving_chart.png)
*Walmart Bentonville - Old vs New Inventory Cost — Old_Cost vs New_Cost after 30% slow-moving reduction (sample data)*

### Repo Structure