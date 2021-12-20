from countrygroups import EUROPEAN_UNION as EU_country
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
from PIL import Image as im
from PIL import ImageTk as imtk
from get_vaccinated_by_countries_EU import vaccinated
from config_file import *
import Main_window
from screeninfo import get_monitors

Monitor = get_monitors()

a = Monitor[0]

w = int(a.width)
h = int(a.height)


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

    Europe_window = Tk()
    Europe_window.state(first_window_size)
    Europe_window.title('Covid-19 information')
    Europe_window.iconbitmap('Images/icon.ico')
    Europe_window.minsize(600, 400)

    canvas = Canvas(Europe_window,
                    width=w,
                    height=h)
    fon_image = im.open("Images/Virus_E_U_A.png")
    resized_image = fon_image.resize((w, h))
    fon_photo = imtk.PhotoImage(resized_image)

    # transparent text_1
    canvas.create_image(0, 0, anchor=NW, image=fon_photo)

    txt_select_a_country = Label(canvas, text="Select a country:", bg="#d7d5d8", font=('Arial', 56))
    txt_select_a_country.place(relx=0, rely=0.2)
    canvas.pack()

    def show_result(event):
        Field_Europe.delete(1.0, END)
        get_combobox_country = Combobox_Europe_second_window.get()

        if get_combobox_country in top_10:
            last_updated = sorted_dic[get_combobox_country.lower()]["last_updated"]
            confirmed = sorted_dic[get_combobox_country.lower()]["confirmed"]
            label = sorted_dic[get_combobox_country.lower()]["label"]
            recovered = sorted_dic[get_combobox_country.lower()]["recovered"]
            deaths = sorted_dic[get_combobox_country.lower()]["deaths"]
            total_vaccinated = vaccinated(label)
            Field_Europe.insert(1.0, (f'Country: {label}\n'
                                      f'Last updated: {last_updated}\n \n'
                                      f'Confirmed: {confirmed}\n'

                                      f'Recovered: {recovered}\n'
                                      f'Deaths: {deaths}\n \n'
                                      f'Total vaccinated: {total_vaccinated}\n'))

            if '<<ComboboxSelected>>':
                Field_Europe.delete(1.0, END)
                get_combobox_second = Combobox_Europe_second_window.get()

                label_second = sorted_dic[get_combobox_second.lower()]["label"]
                last_updated_second = sorted_dic[get_combobox_second.lower()]["last_updated"]

                confirmed_second = sorted_dic[get_combobox_second.lower()]["confirmed"]
                recovered_second = sorted_dic[get_combobox_second.lower()]["recovered"]
                deaths_second = sorted_dic[get_combobox_second.lower()]["deaths"]
                total_vaccinated_second = vaccinated(label_second)

                Field_Europe.insert(1.0, (f'Country: {label_second}\n'
                                          f'Last updated: {last_updated_second}\n \n'

                                          f'Confirmed: {confirmed_second}\n'

                                          f'Recovered: {recovered_second}\n'
                                          f'Deaths: {deaths_second}\n \n'
                                          f'Total vaccinated: {total_vaccinated_second}\n'))

    fontExample = ('Courier', 17, 'bold')
    text_font = ('Arial', '20')
    Combobox_Europe_second_window = tkinter.ttk.Combobox(Europe_window, values=top_10, exportselection=0, width=36,
                                                         height=0,
                                                         state='readonly', font=fontExample)
    Combobox_Europe_second_window.option_add('*TCombobox*Listbox.font', text_font)
    Combobox_Europe_second_window.set("Choose a country")
    Combobox_Europe_second_window['values'] = top_10
    Combobox_Europe_second_window.place(relx=0.01, rely=0.35)
    Combobox_Europe_second_window.bind('<<ComboboxSelected>>', show_result)

    def return_to_first_window():
        Europe_window.destroy()
        Main_window.create_general_window()

    return_to_main = Button(Europe_window, text='<<',
                            font=('Arial', 14), width=5, height=1, command=return_to_first_window)
    return_to_main.place(x=1, y=2)

    Field_Europe = Text(Europe_window, width=58, height=20, bg='White', fg='Black', font=('Arial', 15))
    Field_Europe.place(relx=0.52, rely=0.1)

    def resize(e):
        size = e.width

        if size > 960:
            txt_select_a_country.config(font=('Arial', 36))
            Field_Europe.config(width=58, height=20)
            Field_Europe.place(relx=0.52, rely=0.1)





        elif size > 790:
            txt_select_a_country.config(font=(None, 30))
            Field_Europe.config(width=38, height=10)
            Field_Europe.place(relx=0.01, rely=0.4)



        else:
            txt_select_a_country.config(font=('Arial', 28))
            Field_Europe.config(width=37, height=12)
            Field_Europe.place(relx=0.01, rely=0.45)

    canvas.bind('<Configure>', resize)
    Europe_window.mainloop()


if __name__ == "__main__":
    europe_function()
