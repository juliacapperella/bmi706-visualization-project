import altair as alt
import pandas as pd
import streamlit as st

### P1.2 ###


@st.cache_data
def load_data():
    bci_df = pd.read_csv("https://raw.githubusercontent.com/juliacapperella/bmi706-visualization-project/refs/heads/main/final_data.csv")

    return bci_df

df = load_data()

### P1.2 ###


st.write("## Antimicrobial Resistance")

### P2.1 ###
# replace with st.slider
year = st.slider("Year", df["Year"].min(), df["Year"].max())
# year = st.slider("Year", 2016, 2022)
subset = df[df["Year"] == year]
### P2.1 ###



### P2.3 ###
# replace with st.multiselect
# (hint: can use current hard-coded values below as as `default` for selector)
default = [
    "France",
    "Libya",
    "Argentina",
    "Poland",
    "United States of America",
    "Madagascar",
    "Singapore"
]
countries = st.multiselect("Countries",df["CountryTerritoryArea"].unique(), default)
subset = subset[subset["CountryTerritoryArea"].isin(countries)]
### P2.3 ###


### P2.4 ###
# replace with st.selectbox
infection = st.selectbox("Infectious Syndrome",df["Infectious Syndrome"].unique())
subset = subset[subset["Infectious Syndrome"] == infection]

bacteria = st.selectbox("Bacterial Pathogen",df["Bacterial Pathogen"].unique())
subset = subset[subset["Bacterial Pathogen"] == bacteria]
### P2.4 ###


### P2.5 ###
 
# chart = alt.Chart(subset).mark_rect().encode(
#     x=alt.X("Age", sort=ages),
#     y=alt.Y("Country"),
#     color=alt.Color("Rate:Q", scale=alt.Scale(type="log",domain=(0.01, 1000), clamp=True),
#                     title="Mortality rate per 100k"),
#     tooltip=["Rate"],
# ).properties(
#     title=f"{cancer} mortality rates for {'males' if sex == 'M' else 'females'} in {year}",
# )

# chart2 = alt.Chart(subset).mark_bar().encode(
#     x=alt.X("sum(Pop)", title="Sum of Population Size", axis=alt.Axis(tickMinStep=50000000)),
#     y=alt.Y("Country", sort="-x"),
#     tooltip=("sum(Pop)","Country")
# )

# charttotal = alt.vconcat(chart, chart2).resolve_scale(
#     color = "independent"
# )

### P2.5 ###

# st.altair_chart(charttotal, use_container_width=True)

# countries_in_subset = subset["Country"].unique()
# if len(countries_in_subset) != len(countries):
#     if len(countries_in_subset) == 0:
#         st.write("No data avaiable for given subset.")
#     else:
#         missing = set(countries) - set(countries_in_subset)
#         st.write("No data available for " + ", ".join(missing) + ".")



