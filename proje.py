from tkinter import *
from tkinter import messagebox
from googlemaps import client
import mouseImage
import googlemaps
from datetime import datetime
from pymongo import MongoClient
# from pprint import pprint as print

host="localhost"
port=27017
db="Proje"
connection=MongoClient(host,port)

try:
    db=connection[db]
except:
    print("db baglanamadi")

collection = db['Araçlar']

gmaps = googlemaps.Client(key="AIzaSyC-U82YTDFyM8Uu7cbe1990VIEoYDkX9Mk")
now = datetime.now()

results = client.geolocate

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label=Label(self)
        label.config(text="Aracınızın Marka - Modelini Seçiniz",bg="purple",fg = "white",width=50,height=2,font=("Arial",15))
        label.place(x=20,y=20)

        label=Label(self)
        label.config(text="TESLA",bg="pink",fg = "black",width=15,height=1,font=("Arial",20))
        label.place(x=20,y=100)

        buton=Button(self)
        buton.config(text="Models P100D ",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("TESLA", "MODELS P100D"))
        buton.place(x=40,y=140)
        mouseImage.CreateToolTip(buton, 'car_images/models.png')

        buton=Button(self)
        buton.config(text="Modelx P100D",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("TESLA","MODELX P100D" ))
        buton.place(x=40,y=180)
        mouseImage.CreateToolTip(buton, 'car_images/modelx.png')

        label=Label(self)
        label.config(text="BMW",bg="pink",fg = "black",width=15,height=1,font=("Arial",20))
        label.place(x=20,y=270)

        buton=Button(self)
        buton.config(text="i3",bg="black",fg = "white",width=10,height=1,font=("Arial",15), command = lambda : self.master.AracSec("BMW", "I3"))
        buton.place(x=80,y=310)
        mouseImage.CreateToolTip(buton, 'car_images/i3.png')

        buton=Button(self)
        buton.config(text="i4 M50",bg="black",fg = "white",width=10,height=1,font=("Arial",15), command = lambda : self.master.AracSec("bmw", "i4 m50" ))
        buton.place(x=80,y=350)
        mouseImage.CreateToolTip(buton, 'car_images/i4m50.png')

        buton=Button(self)
        buton.config(text="iX3",bg="black",fg = "white",width=10,height=1,font=("Arial",15), command = lambda : self.master.AracSec("bmw", "ix3"))
        buton.place(x=80,y=390)
        mouseImage.CreateToolTip(buton, 'car_images/ix3.png')

        label=Label(self)
        label.config(text="PORSCHE",bg="pink",fg = "black",width=15,height=1,font=("Arial",20))
        label.place(x=310,y=100)

        buton=Button(self)
        buton.config(text="Taycan 4s",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("porsche", "taycan 4s"))
        buton.place(x=350,y=140)
        mouseImage.CreateToolTip(buton, 'car_images/taycan4s.png')

        buton=Button(self)
        buton.config(text="Taycan Turbo s",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("porsche","taycan turbo s"))
        buton.place(x=350,y=180)
        mouseImage.CreateToolTip(buton, 'car_images/taycanturbos.png')

        label=Label(self)
        label.config(text="Renault",bg="pink",fg = "black",width=15,height=1,font=("Arial",20))
        label.place(x=310,y=270)

        buton=Button(self)
        buton.config(text="Zoe ZE40",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("renault", "zoe ze40"))
        buton.place(x=350,y=310)
        mouseImage.CreateToolTip(buton, 'car_images/zoe.png')

        buton=Button(self)
        buton.config(text="Zoe ZE50",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("renault", "zoe ze50"))
        buton.place(x=350,y=350)
        mouseImage.CreateToolTip(buton, 'car_images/bmw.png')

        label=Label(self)
        label.config(text="Hyundai",bg="pink",fg = "black",width=15,height=1,font=("Arial",20))
        label.place(x=165,y=450)

        buton=Button(self)
        buton.config(text="Kona",bg="black",fg = "white",width=15,height=1,font=("Arial",15), command = lambda : self.master.AracSec("hyundai", "kona")) 
        buton.place(x=200,y=490)
        mouseImage.CreateToolTip(buton, 'car_images/kona.png')

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = Label(self)
        label.config(text='Aracınızın mevcut şarjını giriniz: ', bg="orange", fg="black", font=('Arial',10))
        label.place(x=100, y=78)


        self.giris = Entry(self)
        self.giris.pack()
        self.giris.place(x=300, y=80)

        label = Label(self)
        label.config(text='Mevcut yeri seçiniz: ',bg="violet", fg="black", font=('Arial',10))
        label.place(x=100, y=118)

        self.giris1 = Entry(self)
        self.giris1.pack()
        self.giris1.place(x=300, y=120)

        label = Label(self)
        label.config(text='Gitmek istediğiniz yeri seçiniz: ', bg="yellow", fg="black", font=('Arial',10))
        label.place(x=100, y=158)

        self.giris2 = Entry(self)
        self.giris2.pack()
        self.giris2.place(x=300, y=160)

        self.giris.bind('<Return>', self.ControlFocus)
        self.giris1.bind('<Return>', self.ControlFocus)
        self.giris2.bind('<Return>', self.ControlFocus)

        Buton = Button(self)
        Buton.config (text='HESAPLA', bg= 'black', fg= 'white', command = lambda : self.master.BilgiGir(self.giris.get(), self.giris1.get(), self.giris2.get()))
        self.bind('<Return>', self.ControlFocus)
        Buton.place(x=250, y=200)
        
        self.label1 =Label(self)
        # self.label1.pack()
        # self.label1.place(x=350, y=300)

        self.label2 =Label(self)
        # self.label2.pack()
        # self.label2.place(x=100, y=300)

        self.label3 =Label(self)
        # self.label3.pack()
        # self.label3.place(x=350, y=350)

        self.label4 =Label(self)
        # self.label4.pack()
        # self.label4.place(x=100, y=350)

        self.label5 =Label(self)
        self.label5.pack()
        self.label5.place(x=150, y=250)

    def ControlFocus(self, e):
        girisList = [ self.giris, self.giris1, self.giris2 ]

        for giris in girisList:
            if giris.get() == "":
                giris.focus_force()
                return

        self.master.BilgiGir(self.giris.get(), self.giris1.get(), self.giris2.get())

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.p1 = Page1(self)
        self.p2 = Page2(self)

        self.buttonframe = Frame(self)
        self.container = Frame(self)
        self.buttonframe.pack(side="bottom", fill="x", expand=False)
        self.container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.b1 = Button(self.buttonframe, text="ana ekran", bg="white", fg = "black", command = lambda page = self.p1 : self.ShowPage(page) )
        self.b2 = Button(self.buttonframe, text="hesap", bg="white", fg="black", command = lambda page = self.p2 : self.ShowPage(page) )

        self.b1.pack(side="bottom", fill="x")
        self.pack()
        self.b2.pack(side="bottom", fill="x")

        self.p1.show()
        self.p1.focus_force()

        self.marka = ""
        self.model = ""

    def ShowPage(self,page):
        page.lift()
        page.focus_force()

    def AracSec(self, marka, model):

        marka = marka.upper()
        model = model.upper()

        self.marka = marka
        self.model = model

        self.p2.lift()
        self.p2.focus_force()

    def BilgiGir(self, giris, giris1, giris2):

        if self.marka == "" or self.model == "":
            # self.p2.label5.pack()
            # self.p2.label5.place(x=220, y=250)
            # self.p2.label5.config(text = "Arac secilmedi.", bg="red", font=15)
            messagebox.showinfo("DİKKAT", "\tAraç Seçimi Yapmadınız\nLütfen Ana Sayfaya Dönüp Bir Araç Seçiniz")
            return
        else:
            self.p2.label5.pack_forget()
            self.p2.label5.place_forget()

        coords_0 = giris1
        coords_1 = giris2

        class AralıkException(Exception):
            def __init__(self):
                super().__init__()

        def err():
            if int(giris) < 0 or int(giris) > 100:
                raise AralıkException()
            else:
                return

        try:
            ilkSarj = int(giris)
            err()
        except ValueError:
            self.p2.label3.pack_forget()
            self.p2.label3.place_forget()
            self.p2.label4.pack_forget()
            self.p2.label4.place_forget()
            self.p2.label1.pack_forget()
            self.p2.label1.place_forget()
            self.p2.label2.pack_forget()
            self.p2.label2.place_forget()
            messagebox.showinfo("DİKKAT", "Lütfen Aracınızın İlk Şarjını Giriniz")
            return
        except AralıkException :
            self.p2.label3.pack_forget()
            self.p2.label3.place_forget()
            self.p2.label4.pack_forget()
            self.p2.label4.place_forget()
            self.p2.label1.pack_forget()
            self.p2.label1.place_forget()
            self.p2.label2.pack_forget()
            self.p2.label2.place_forget()
            messagebox.showinfo("DİKKAT", "Girdiğiniz Şarj Değeri Aralık Dışıdır")
            return

        sonuc = collection.find({'Model': self.model})
        for i in sonuc:
            ortTuketim = i["Ortalama Tüketim"] 
            pilKapasitesi = i["Pil Kapasitesi"]

        try:
            directions_result = gmaps.directions(coords_0, coords_1, mode="driving", departure_time=now, avoid='highway', language = 'tr')
            leg = directions_result[0].get("legs")[0]
            # self.p2.label5.pack_forget()
            # self.p2.label5.place_forget()
        except (googlemaps.exceptions.HTTPError, googlemaps.exceptions.ApiError):
            # self.p2.label5.pack()
            # self.p2.label5.place(x=200, y=250)
            # self.p2.label5.config(text = "Rota olusturulamadi", bg="red", font=15)
            self.p2.label3.pack_forget()
            self.p2.label3.place_forget()
            self.p2.label4.pack_forget()
            self.p2.label4.place_forget()
            self.p2.label1.pack_forget()
            self.p2.label1.place_forget()
            self.p2.label2.pack_forget()
            self.p2.label2.place_forget()
            messagebox.showinfo("DİKKAT", "ROTA OLUŞTURULAMADI\nLütfen Konum Bilgisi Giriniz")
            return
        except IndexError:
            messagebox.showinfo("DİKKAT", "\tROTA OLUŞTURULAMADI\nLütfen Girdiğiniz Konum Bilgilerini Kontrol Ediniz")
            self.p2.label3.pack_forget()
            self.p2.label3.place_forget()
            self.p2.label4.pack_forget()
            self.p2.label4.place_forget()
            self.p2.label1.pack_forget()
            self.p2.label1.place_forget()
            self.p2.label2.pack_forget()
            self.p2.label2.place_forget()
            return
        # print(directions_result[0])

        menzil = float(leg.get("distance").get("value"))/1000
        pilTuketimi = (menzil/100)* ortTuketim
        pilYuzdesi = ilkSarj-((pilTuketimi/pilKapasitesi)*100)

        def err(gelenDeger):
            if gelenDeger<5:
                raise ValueError ("Lütfen Yol Üstünde Şarj Ediniz")
            else:
                return gelenDeger

        try:
            self.p2.label1.pack()
            self.p2.label1.place(x=350, y=300)
            self.p2.label2.pack()
            self.p2.label2.place(x=100, y=300)
            self.p2.label3.pack()
            self.p2.label3.place(x=350, y=350)
            self.p2.label4.pack()
            self.p2.label4.place(x=100, y=350)
            self.p2.label1.config(text =str(round(menzil)) + "km")
            self.p2.label2.config(text="gitmek istediğiniz yere olan mesafeniz:", bg = "white")
            self.p2.label3.config(text ="%" + str(err(round(pilYuzdesi))))
            self.p2.label4.config(text ="varılacak noktada tahmini şarj:", bg = "white")
            self.p2.label5.pack_forget()
            self.p2.label5.place_forget()
        except ValueError as err:
            self.p2.label3.pack_forget()
            self.p2.label3.place_forget()
            self.p2.label4.pack_forget()
            self.p2.label4.place_forget()
            self.p2.label5.pack()
            self.p2.label5.place(x=150, y=250)
            self.p2.label5.config(text = err, bg="white", font=15)

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("ŞEK OTOMOTİV")
    root.wm_geometry("600x600")
    root.mainloop()