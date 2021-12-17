from django.shortcuts import render
# from django.http import HttpResponse
from main.templates.main.get_general_vaccinated_data_asia import total_vaccinated
from main.templates.main.config_file import *
from main.templates.main.request_module import request as req


def index(request):
    return render(request, "main/index.html")


def europe_window(request):
    return render(request, "main/Europe.html")


def ukraine_window(request):
    return render(request, "main/Ukraine.html")


def asia_window(request):
    # return render(request, "main/Asia.html")
    result = my_list = []
    headers = headers_asia
    html = req(url_asia, headers)

    all_infected = f'Infected: {html.find("td", class_="bg-total larger").text}'
    my_list.append(all_infected)
    deaths = f'Deaths: {html.find_all("td", class_="bg-total")[3].text}'
    my_list.append(deaths)
    recovered = f'Recovered: {html.find_all("td", class_="bg-total")[5].text}'
    my_list.append(recovered)
    now_ill = f'Now ill: {html.find_all("td", class_="bg-total")[7].text}'
    my_list.append(now_ill)
    total_vaccinated_people = f'Total vaccinated people: {total_vaccinated()}'
    my_list.append(total_vaccinated_people)
    return render(request, "main/Asia.html", {'result': result})