Public Spending and Social Outcomes in the EU
Project Overview

This project analyzes the relationship between public spending and social outcomes in the European Union (EU). Specifically, we study whether countries that spend more on health and education tend to have:

Lower poverty rates
Higher life expectancy

The analysis is based on descriptive statistics and data visualization using Python.

Research Questions
How does public spending differ between EU-15 and post-2004 countries?
Is higher spending associated with lower poverty and higher life expectancy?
What are the main trends between 2016 and 2023?
Data Sources

All data comes from Eurostat:

Government spending (health and education): GOV_10A_EXP
Poverty rate: ILC_LI02
Life expectancy: DEMO_MLEXPEC

We focus on:

24 EU countries
Period: 2016–2023
Variables expressed as % of GDP when relevant
Methodology

The project uses descriptive data analysis techniques:

Data cleaning and filtering (Python, pandas)
Merging multiple datasets
Creation of key variables (e.g., total spending = health + education)
Group comparison (EU-15 vs post-2004)
Visualization using seaborn and matplotlib
Key Results
EU-15 countries spend more on average (12.1% vs 10.7% of GDP)
Higher spending is associated with:
Lower poverty (correlation ≈ -0.45)
Higher life expectancy (correlation ≈ +0.35)
COVID-19 had a visible impact on both spending and outcomes (2020–2021)
However, results are correlations only (not causal relationships)
Repository Structure
.
├── data/                # Raw datasets (Eurostat)
├── output/              # Generated charts
├── main.py          # Main Python script
├── PublicSpendingEU_Python_BUSSOLA_LASSUS_DONDERO.pdf.pdf           # Final report (5 pages)
└── README.md
How to Run the Code
Install required packages:
pip install pandas matplotlib seaborn
Make sure the data files are in the data/ folder:
gov_exp.csv
ilc.csv
life_exp.csv
Run the script:
python analysis.py
Output:
Charts will be saved in the output/ folder
Summary statistics will appear in the terminal
Authors
Juliette Lassus
Diego Bussola
Alec Dondero
Notes & Limitations
The analysis is purely descriptive
Results may reflect underlying differences in wealth across countries
Visualizations are presented individually (not combined), which may limit direct comparison
