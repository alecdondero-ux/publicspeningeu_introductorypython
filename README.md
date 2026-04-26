# Public Spending and Social Outcomes in the EU

## Project Overview

Our project analyzes the relationship between public spending and social outcomes in the European Union (EU). Specifically, we study whether countries that spend more on health and education tend to have:

- Lower poverty rates  
- Higher life expectancy  

The analysis is based on descriptive statistics and data visualization using Python.



## Research Questions

- How does public spending differ between EU-15 and post-2004 countries?  
- Is higher spending associated with:  
  - Lower poverty?  
  - Higher life expectancy?  
- What are the main trends between 2016 and 2023?  



## Data Sources

All data comes from Eurostat:

- Government spending (health and education): GOV_10A_EXP  
- Poverty rate: ILC_LI02  
- Life expectancy: DEMO_MLEXPEC  

We focus on:

- 24 EU countries  
- Period: 2016–2023  
- Variables expressed as % of GDP when relevant  



## Methodology

The project uses the descriptive data analysis techniques seen in class:

- Data cleaning and filtering (Python, pandas)  
- Merging multiple datasets  
- Creation of key variables (e.g., total spending = health + education)  
- Group comparison (in this case, EU-15 vs post-2004)  
- Visualization using seaborn and matplotlib  



## Key Results

- EU-15 countries spend more on average (12.1% vs 10.7% of GDP)  
- Higher spending is associated with:  
  - Lower poverty (correlation ≈ -0.45)  
  - Higher life expectancy (correlation ≈ +0.35)  
- COVID-19 had a visible impact on both spending and outcomes (2020–2021)  

**N-B:** Results are correlational and do not imply causality.



## Repository Structure


.
├── data/
│ ├── gov_exp.csv
│ ├── ilc.csv
│ └── life_exp.csv
├── output/
├── main.py
├── report.pdf
└── README.md




## How to Run the Code

1. Install required packages:

pip install -r requirements.txt


2. Make sure the data files are in the `data/` folder:
- gov_exp.csv  
- ilc.csv  
- life_exp.csv  

3. Run the script:

python main.py


### Output:
- Charts will be saved in the `output/` folder  
- Summary statistics will appear in the terminal  



## Authors

- Juliette Lassus  
- Diego Bussola  
- Alec Dondero  



## Notes & Limitations

- The analysis is somewhat descriptive  
- Results may reflect underlying differences in wealth across countries  
- Visualizations are presented individually, which may limit direct comparison  
