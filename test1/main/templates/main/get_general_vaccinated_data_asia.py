from main.templates.main import config_file
from main.templates.main.request_module import request
import awoc  # import library of countries
import urllib.request, json

my_world = awoc.AWOC()
asia_countries = my_world.get_countries_list_of('Asia')

headers = config_file.headers_asia_vaccinated_data
html = request(config_file.asia_vaccinated, headers)
vaccinated_per_asia_country = []

# get information from each asian country
with urllib.request.urlopen("https://jhucoronavirus.azureedge.net/jhucoronavirus/global_vaccines.json") as url:
    data = json.loads(url.read().decode())


# filter information according to asian countries
def total_vaccinated():
    for country in asia_countries:
        for element in data:
            if element['country'] == country:
                vaccinated_per_asia_country.append(int(element['data']['raw_full_vac']))
    return sum(vaccinated_per_asia_country)



if __name__ == "__main__":
    print(total_vaccinated())



