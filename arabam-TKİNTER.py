from tkinter import *
from PIL import ImageTk,Image
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from  openpyxl import *
import pkg_resources.py2_warn
kitap = Workbook()
pencere = Tk() # Pencere oluştu
pencere.title("Arabam.com Botu") #Başlık oluştu
pencere.geometry("270x200+550+100") #Pencere boyutlandırma ve komutlandırma
pencere.iconphoto(False, ImageTk.PhotoImage(Image.open("ikon.ico")))


def yazdır():
    mark = marko.get()
    numar = numara.get()
    marka = mark+"?page"+str(numar)
    url = "https://www.arabam.com/ikinci-el/otomobil/"+marka
    yeniurl = requests.get(url)
    soup = BeautifulSoup(yeniurl.content,"lxml")
    ne = soup.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})
    for a in ne:
        model = a.find("h3",attrs={"class":"crop-after"}).text
        baslik =a.find("td",attrs={"class":"horizontal-half-padder-minus pr"}).text
        Yıl = a.find_all("td",attrs={"class":"listing-text pl8 pr8 tac pr"})[0].text
        Km = a.find_all("td",attrs={"class":"listing-text pl8 pr8 tac pr"})[1].text
        Renk = a.find_all("td",attrs={"class":"listing-text pl8 pr8 tac pr"})[2].text
        Fiyat = a.find("td",attrs={"class":"pl8 pr8 tac pr"}).text
        sheet = kitap.active
        sheet.append((model,baslik,Yıl,Km,Renk,Fiyat))
        kitap.save("{}.xlsx".format(mark))
        kitap.close
    wb = load_workbook("{}.xlsx".format(mark))
    ws = wb.active
    veri = Label(pencere,text ="İşlem Tamamlandı!")
    veri.grid(row=4,column=1)
    messagebox.showinfo("Bilgi","{} araç ilanları {}.xlsx dosyasına kaydedildi.".format(mark,mark))

markolabel = Label(pencere,text="Markalar").grid(row=0, column=0, sticky='e')
clicked = StringVar()
clicked.set("Opel")
drop = OptionMenu(pencere,clicked,'Acura ', 'Alfa Romeo ', 'Anadol ', 'Aston Martin ', 'Audi ', 'Bentley ', 'BMW ', 'Buick ', 'Cadillac ', 'Chery ', 'Chevrolet ', 'Chrysler ', 'Citroen ', 'Dacia ', 'Daewoo ', 'Daihatsu ', 'Dodge ', 'DS Automobiles ', 'Ferrari ', 'Fiat ', 'Ford ', 'GAZ ', 'Geely ', 'Honda ', 'Hyundai ', 'Ikco ', 'Infiniti ', 'Isuzu ', 'Jaguar ', 'Kia ', 'Lada ', 'Lamborghini ', 'Lancia ', 'Lexus ', 'Lincoln ', 'Lotus ', 'Maserati ', 'Mazda ', 'Mercedes - Benz ', 'MG ', 'MINI', 'Mitsubishi ', 'Moskvitch ', 'Nissan ', 'Oldsmobile ', 'Opel ', 'Peugeot ', 'Plymouth ', 'Pontiac ', 'Porsche ', 'Proton ', 'Renault ', 'Rolls Royce ', 'Rover ', 'Saab ', 'Seat ', 'Skoda ', 'Smart ', 'Subaru ', 'Suzuki ', 'Tata ', 'Tofaş ', 'Toyota ', 'Volkswagen ', 'Volvo ')
drop.grid(padx=10,pady=10,row=0,column=1,columnspan=10)
markoyaz = Label(pencere,text="Marka yazın:").grid(row=1, column=0, sticky='e')
marko = Entry()
marko.grid(padx=10,pady=10,row=1,column=1)
numaralabel = Label(pencere,text="Kaç Sayfa:").grid(row=2, column=0, sticky='e')
numara = Entry()
numara.grid(padx=10,row=2,column=1,sticky='w')

buton = Button(text = "Getir",command =yazdır,font={"Helvetica",2})
buton.grid(padx=10,pady=10,row=3,column=1)


mainloop()