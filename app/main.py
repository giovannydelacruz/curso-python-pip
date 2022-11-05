import read_csv
import charts
import utils
import pandas as pd


def run():
    # data = read_csv.read_csv("data.csv")
    # data = list(filter(lambda item: item["Continent"] == "South America", data))
    
    # countries = list(map(lambda x: x["Country/Territory"],data))
    # percentages = list(map(lambda x: x["World Population Percentage"],data))

    df = pd.read_csv("data.csv")
    df = df[["Continent"]=="South America"]

    countries = df["Country/Territory"].values
    percentages = df["World Population Percentage"].values

    charts.generate_pie_chart(countries, percentages)

    country = input("Type Country --> ")

    result = utils.population_by_country(df,country)

    if len(result) > 0:
        country = result[0]
        name = country["Country/Territory"] 
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(name, labels, values)

if __name__ == "__main__":
    run()