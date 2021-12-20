from config_file import *
from request_module import request
from get_general_vaccinated_data_asia import total_vaccinated
import json


def asia_function():
    headers = headers_asia
    html = request(url_asia, headers)

    all_infected = html.find("td", class_="bg-total larger").text
    deaths = html.find_all("td", class_="bg-total")[3].text
    recovered = html.find_all("td", class_="bg-total")[5].text
    now_ill = html.find_all("td", class_="bg-total")[7].text
    total_vaccinated_people = total_vaccinated()
    # print(f"\n{all_infected}\n\n {deaths} \n {recovered} \n {now_ill} \n {total_vaccinated_people}")
    # info_text.insert(1.0, f"\n{all_infected}\n\n {deaths} \n {recovered} \n {now_ill} \n {total_vaccinated_people}")
    # info_text['state'] = 'disabled'

    dict = {}
    dict['Infected'] = all_infected
    dict['Deaths'] = deaths
    dict['Recovered'] = recovered
    dict['Now ill'] = now_ill
    dict['Total vaccinated people'] = total_vaccinated_people

    # for key,value in dict.items():
    #     print(key, value)
    with open("file.json", "w") as out:
        # out = json.dumps(dict)
        out.write(json.dumps(dict))

    json_dictionary = json.dumps(dict)

    print(json_dictionary)


if __name__ == "__main__":
    asia_function()
