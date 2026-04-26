# project: public spending and social outcomes in the EU
# course: intro to data analysis with python
# working group: Juliette Lassus, Diego Bussola, Alec Dondero

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output", exist_ok=True)
sns.set_theme(style="whitegrid")

# we first define the country groups
# EU-15 = old members (without the UK, which left in 2020)
# post-2004 = countries that joined later

eu15 = ["AT", "BE", "DE", "DK", "EL", "ES", "FI", "FR", "IE", "IT", "LU", "NL", "PT", "SE"]
post2004 = ["BG", "CY", "CZ", "EE", "HR", "HU", "LT", "LV", "MT", "PL", "RO", "SI", "SK"]
all_countries = eu15 + post2004

names = {
    "AT": "Austria", "BE": "Belgium", "DE": "Germany", "DK": "Denmark",
    "EL": "Greece", "ES": "Spain", "FI": "Finland", "FR": "France",
    "IE": "Ireland", "IT": "Italy", "LU": "Luxembourg", "NL": "Netherlands",
    "PT": "Portugal", "SE": "Sweden",
    "BG": "Bulgaria", "CY": "Cyprus", "CZ": "Czechia", "EE": "Estonia",
    "HR": "Croatia", "HU": "Hungary", "LT": "Lithuania", "LV": "Latvia",
    "MT": "Malta", "PL": "Poland", "RO": "Romania", "SI": "Slovenia",
    "SK": "Slovakia",
}


# with the importation of the Eurostat files, we save the three tabs in the data folder

gov  = pd.read_csv("data/gov_exp.csv")
ilc  = pd.read_csv("data/ilc.csv")
life = pd.read_csv("data/life_exp.csv")


# then we clean the data by filtering it to what the theme of our case is about

# health spending (GF07) and education spending (GF09)

# health spending (GF07)
health = gov[gov["cofog99"] == "GF07"]
health = health[health["sector"] == "S13"]
health = health[health["unit"] == "PC_GDP"]
health = health[health["geo"].isin(all_countries)]
health = health[["geo", "TIME_PERIOD", "OBS_VALUE"]]
health.columns = ["geo", "year", "health"]

# education spending (GF09)
educ = gov[gov["cofog99"] == "GF09"]
educ = educ[educ["sector"] == "S13"]
educ = educ[educ["unit"] == "PC_GDP"]
educ = educ[educ["geo"].isin(all_countries)]
educ = educ[["geo", "TIME_PERIOD", "OBS_VALUE"]]
educ.columns = ["geo", "year", "educ"]

# poverty rate, total population, in percentage
poverty = ilc[ilc["sex"] == "T"]
poverty = poverty[poverty["unit"] == "PC"]
poverty = poverty[poverty["geo"].isin(all_countries)]
poverty = poverty[["geo", "TIME_PERIOD", "OBS_VALUE"]]
poverty.columns = ["geo", "year", "poverty"]

# life expectancy at birth, total (male and female combined)
lifedf = life[life["sex"] == "T"]
lifedf = lifedf[lifedf["age"] == "Y_LT1"]
lifedf = lifedf[lifedf["geo"].isin(all_countries)]
lifedf = lifedf[["geo", "TIME_PERIOD", "OBS_VALUE"]]
lifedf.columns = ["geo", "year", "life_exp"]


# to have a simpler view, we merge everything

df = health.merge(educ, on=["geo", "year"])
df = df.merge(poverty, on=["geo", "year"])
df = df.merge(lifedf, on=["geo", "year"])
df = df.dropna()

# we only keep recent years
df["year"] = df["year"].astype(int)
df = df[df["year"] >= 2016]
df = df[df["year"] <= 2023]

# we add useful columns
df["name"] = df["geo"].map(names)

df["group"] = "Post-2004"
df.loc[df["geo"].isin(eu15), "group"] = "EU-15"

df["total"] = df["health"] + df["educ"]


# from there we can write the descriptive statistics

print(df.describe().round(2))
print(df.groupby("group")[["total", "poverty", "life_exp"]].mean().round(2))


# and then draw the charts that are the most needed for the report

# chart 1: histogram
sns.histplot(data=df, x="total", hue="group", bins=20)
plt.savefig("output/chart1_histograms.png")
plt.clf()

# chart 2: boxplots
sns.boxplot(data=df, x="group", y="total", hue="group")
plt.savefig("output/chart2_boxplots.png")
plt.clf()

# chart 3: time series
ts = df.groupby(["year", "group"])["total"].mean().reset_index()
sns.lineplot(data=ts, x="year", y="total", hue="group", marker="o")
plt.savefig("output/chart3_timeseries.png")
plt.clf()

# chart 4: spending by country in 2023
df_2023 = df[df["year"] == 2023].copy()
df_2023 = df_2023.sort_values("total")
sns.barplot(data=df_2023, y="name", x="total", hue="group")
plt.savefig("output/chart4_by_country.png")
plt.clf()

# chart 5: correlation scatter
sns.scatterplot(data=df, x="total", y="life_exp", hue="group")
plt.savefig("output/chart5_scatter.png")
plt.clf()


# correlations
print(df[["total", "poverty", "life_exp"]].corr().round(3))

print("This line marks the end of the code's work! Everything's done.")
