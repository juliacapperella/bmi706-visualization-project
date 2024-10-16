import altair as alt
import pandas as pd
import streamlit as st

## Make the page wider
st.set_page_config(layout="wide")

## Load data set from github
@st.cache_data
def load_data():
    bci_df = pd.read_csv("https://raw.githubusercontent.com/juliacapperella/bmi706-visualization-project/refs/heads/main/final_data.csv")

    return bci_df

df = load_data()

## Make streamlit app
st.write("## Antimicrobial Resistance")

## Make year slider
year = st.sidebar.slider("Year", df["Year"].min(), df["Year"].max(), value = 2020)
subset = df[df["Year"] == year]


## Choose default countries for selector
default = [
    "Bangladesh",
    "Ethiopia",
    "Argentina",
    "Singapore",
    "Sweden"
]

## Make country selector
countries = st.sidebar.multiselect("Countries",df["CountryTerritoryArea"].unique(), default)
subset = subset[subset["CountryTerritoryArea"].isin(countries)]
subset2 = df[df["CountryTerritoryArea"].isin(countries)]

## Make infectious syndrome selector
infection = st.sidebar.selectbox("Infectious Syndrome",df["Infectious Syndrome"].unique())
subset = subset[subset["Infectious Syndrome"] == infection]

## Make bacterial pathogen selector
bacteria = st.sidebar.selectbox("Bacterial Pathogen",df["Bacterial Pathogen"].unique())
subset = subset[subset["Bacterial Pathogen"] == bacteria]

## Create chart 1 -- heat map of BCI for selection options
chart = alt.Chart(subset).mark_rect().encode(
    x=alt.X("Antibiotic Group"),
    y=alt.Y("CountryTerritoryArea"),
    color=alt.Color("BCIs per million population:Q", scale=alt.Scale(type="log",domain=(0.01, 1000), clamp=True),
                    title="BCIs per million population"),
    tooltip=["BCIs per million population"],
).properties(
    title=f"BCIs per million population in {year}",
)

## Create chart 2 -- bar chart of health expenditure for selection options
chart2 = alt.Chart(subset).mark_bar().encode(
    x=alt.X("gghed_gdp", title="Domestic Health Expenditure as Percent of GDP", axis=alt.Axis(tickMinStep=50000000)),
    y=alt.Y("CountryTerritoryArea", sort="-x"),
    tooltip=["gghed_gdp","CountryTerritoryArea"],
)

## Create chart 3 -- (unlinked) line chart of year and health expenditure
chart3 = alt.Chart(subset2).mark_line(
    point=True
).encode(
    x=alt.X("Year:N", axis=alt.Axis(title='Year')),
    y=alt.Y("gghed_gdp:Q"),
    color=alt.Color('CountryTerritoryArea:N'),
    tooltip=["gghed_gdp"]
).properties(
    title=f"Health expenditures per year",
    width=800
)

## Create chart 4 -- (unlinked) line chart of year and BCI per million population
chart4 = alt.Chart(subset2).mark_line(
    point=True
).encode(
    x=alt.X("Year:N", axis=alt.Axis(title='Year')),
    y=alt.Y("sum(BCIs per million population):Q"),
    color=alt.Color('CountryTerritoryArea:N'),
    tooltip=["sum(BCIs per million population)"]
).properties(
    title=f"BCIs per million population per year",
    width=800
)

## Combine linked charts
charttotal = alt.vconcat(chart, chart2).resolve_scale(
    color = "independent"
)

## Print linked chart and unlinked charts
st.altair_chart(charttotal, use_container_width=True)
linecharts = chart3 | chart4
st.altair_chart(linecharts, use_container_width=True)

# countries_in_subset = subset["CountryTerritoryArea"].unique()
# if len(countries_in_subset) != len(countries):
#     if len(countries_in_subset) == 0:
#         st.write("No data avaiable for given subset.")
#     else:
#         missing = set(countries) - set(countries_in_subset)
#         st.write("No data available for " + ", ".join(missing) + ".")



