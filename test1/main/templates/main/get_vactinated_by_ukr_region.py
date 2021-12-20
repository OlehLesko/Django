import config_file
from request_module import request

headers = config_file.headers_ukraine
html = request(config_file.url_ukraine_vactinated, headers)
list_region = []


# get info vaccinated people in the region of Ukraine
def total_vaccinated_region_ukr(region):
    all_info = html.find("div", class_="compact-table expand-table").find('table').find_all('td')
    for i in all_info:
        if i.string == region:
            return i.parent.find_all("td", class_="blank")[7].text


if __name__ == "__main__":
    total_vaccinated_region_ukr()
