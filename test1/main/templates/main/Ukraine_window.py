from config_file import *
from get_vactinated_by_ukr_region import total_vaccinated_region_ukr
from ukraine_regions_data import get_region_list
from PIL import Image as Pil_Image
from PIL import ImageTk as Tk_Img
import Main_window
from request_module import request
from deep_translator import GoogleTranslator
from translitua import translit
from tkinter import *
import tkinter.ttk
from screeninfo import get_monitors

# get monitor parameters
monitor = get_monitors()[0]
monitor_width = int(monitor.width)
monitor_height = int(monitor.height)


# -----------------------------------------------
def ukraine_function():
    # use it for request
    headers = headers_ukraine
    html = request(url_ukraine, headers)

    # translate ukrainian region in english transliteration
    translate_elements = []
    ukraine_regions = get_region_list()
    for element in ukraine_regions:
        translate_elements.append(translit(element))

    # get period of time
    period_of_time = html.find("table", class_="line").find("caption").text
    period_of_time = GoogleTranslator(source='auto', target='en').translate(period_of_time)

    # create tkinter window of Ukraine
    ukraine_window = Tk()
    ukraine_window.state(first_window_size)
    ukraine_window.title('Covid-19 information')
    ukraine_window.iconbitmap('Images/icon.ico')
    ukraine_window.minsize(550, 700)

    # create canvas window
    canvas = Canvas(ukraine_window,
                    width=monitor_width,
                    height=monitor_height)
    fon_image = Pil_Image.open("Images/Virus_E_U_A.png")
    resized_image = fon_image.resize((monitor_width, monitor_height))
    fon_photo = Tk_Img.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=fon_photo)

    # create main label of window
    label_region_of_ukraine = Label(canvas, text="Region of Ukraine:", bg="#d7d5d8", font=('Arial', 56))
    label_region_of_ukraine.place(relx=0, rely=0.2)
    canvas.pack()

    # show result in the text field about selected region
    def show_result(event):
        field_ukraine.delete(1.0, END)
        selected_region = combobox_ukraine_second_window.get()
        selected_region = ukraine_regions[translate_elements.index(selected_region)]
        all_info = html.find_all('table')[1].find_all('td')

        # looking for and get information about selected region
        for i in all_info:
            if i.string == selected_region:
                times = period_of_time
                all_infected = i.parent.find("td", class_="blank larger").text
                all_deaths = i.parent.find_all("td", class_="blank")[2].text
                all_recovered = i.parent.find_all("td", class_="blank")[4].text
                all_now_ill = i.parent.find_all("td", class_="blank")[6].text
                total_vaccinated = total_vaccinated_region_ukr(i.string)

                field_ukraine.insert(1.0, (
                    f'{times}\n'
                    f'\nConfirmed: {all_infected}\n'
                    f'\nRecovered: {all_recovered}\n'
                    f'\nDeaths: {all_deaths}\n'
                    f'\nNow ill: {all_now_ill}\n'
                    f'\nTotal vaccinated: {total_vaccinated}\n'))

    # create combobox with list of Ukraine regions
    combobox_ukraine_second_window = tkinter.ttk.Combobox(ukraine_window, values=ukraine_regions,
                                                          width=30, height=20,
                                                          state='readonly', font=('Courier', 17, 'bold'))
    ukraine_window.option_add('*TCombobox*Listbox.font', ('Arial', '10'))
    combobox_ukraine_second_window.set("Choose the region.")
    combobox_ukraine_second_window['values'] = translate_elements
    combobox_ukraine_second_window.place(relx=0.01, rely=0.35)
    combobox_ukraine_second_window.bind('<<ComboboxSelected>>', show_result)

    # create text_field show info
    field_ukraine = Text(ukraine_window, width=58, height=20, bg='White', fg='Black', font=('Arial', 15))
    field_ukraine.place(relx=0.52, rely=0.1)

    # we change dynamically our window
    def resize(e):
        size = e.width
        print(f"width={e.width}")
        print(f"height={e.height}")
        if size > 960:
            label_region_of_ukraine.config(font=('Arial', 36))
            field_ukraine.config(width=58, height=20)
            field_ukraine.place(relx=0.59, rely=0.1)
        elif size > 790:
            label_region_of_ukraine.config(font=(None, 30))
            field_ukraine.config(width=38, height=13)
            field_ukraine.place(relx=0.01, rely=0.45)
        else:
            label_region_of_ukraine.config(font=('Arial', 28))
            field_ukraine.config(width=38, height=13)
            field_ukraine.place(relx=0.01, rely=0.45)

    canvas.bind('<Configure>', resize)

    # back to the main window
    def return_to_first_window():
        ukraine_window.destroy()
        Main_window.create_general_window()

    return_to_main = Button(ukraine_window, text='<<',
                            font=('Arial', 14), width=5, height=1, command=return_to_first_window)
    return_to_main.place(x=1, y=2)

    ukraine_window.mainloop()
