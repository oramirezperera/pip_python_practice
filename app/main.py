import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item : item['continent'] == 'South America', data))

    countries = list(map(lambda x : x['Country/Territory'], data))

    percentages = list(map(lambda x : x['World Population Percentage'], data))

    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()