from countrygroups import EUROPEAN_UNION as EU_country
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
from PIL import Image as im
from PIL import ImageTk as imtk
from get_vaccinated_by_countries_EU import vaccinated
from config_file import *
# import Main_window
from screeninfo import get_monitors
import json


def europe_function():
    api = CovId19Data(force=True)

    new_list = []
    sorted_dic = {}
    top_10_europe = []
    top_number = 0
    api_all = api.get_all_records_by_country()

    # get only europe country
    for elem in api_all:
        if api_all[elem]['label'] in EU_country.names:
            new_list.append(api_all[elem]["confirmed"])

    # sorted list and get top-10
    while top_number < 10:
        new_list.sort(reverse=True)
        for elem in api_all:
            if new_list[top_number] in api_all[elem].values():
                sorted_dic[elem] = api_all[elem]
        top_number += 1

    # dictionry of top-10 sorted country
    def country_from_sorted_list():
        for country in sorted_dic:
            top_10_europe.append(sorted_dic[country]["label"])
        return top_10_europe

    top_10 = country_from_sorted_list()

    dict = {}
    dict['Information_of_country'] = api_all
    dict['Top_10_country'] = top_10

    print(dict)
    with open("Europe_file.json", "w") as out:
        out.write(json.dumps(dict))

    json_dictionary = json.dumps(dict)


if __name__ == "__main__":
    europe_function()
