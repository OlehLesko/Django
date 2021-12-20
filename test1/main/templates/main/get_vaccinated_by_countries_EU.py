import config_file
from request_module import request
import awoc  # import library of countries
import urllib.request, json

my_world = awoc.AWOC()
europe = my_world.get_countries_list_of('Europe')

headers = config_file.headers_asia_vaccinated_data
html = request(config_file.asia_vaccinated, headers)


with urllib.request.urlopen("https://jhucoronavirus.azureedge.net/jhucoronavirus/global_vaccines.json") as url:
    data = json.loads(url.read().decode())


def vaccinated(euro_country):
    for element in data:
        if element['country'] == euro_country:
            vaccinated = int(element['data']['raw_full_vac'])
            return vaccinated







