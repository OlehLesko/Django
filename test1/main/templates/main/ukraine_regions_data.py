import config_file
from request_module import request

headers = config_file.headers_ukraine
html = request(config_file.url_ukraine, headers)
list_region = []


# get list of Ukraine region
def get_region_list():
    region_of_ukraine = html.find("div", class_="compact-table expand-table").find("table").find_all("tr")
    for element in region_of_ukraine[1:-1]:
        list_region.append(element.find("a").text)
    return list_region



