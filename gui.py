import customtkinter
import mushroomsdt as mdt
import numpy as np
import pandas as pd
import os
import webbrowser

from PIL import Image

# App Init

user_entry = np.zeros((1,22))
customtkinter.set_appearance_mode("dark")

# Window Init

app = customtkinter.CTk()
app.title("Klasifikasi Jamur")
app.resizable(width=False, height=False)

XWidgetPadding = 12
YWidgetPadding = 12
ScreenWidth = app.winfo_screenwidth()
ScreenHeight = app.winfo_screenheight()
XCenterPos = (ScreenWidth // 2) - (965 // 2)
YCenterPos = (ScreenHeight // 2) - (500 // 2)

app.geometry(f"{965}x{500}+{XCenterPos}+{YCenterPos}")

# Tab Menu

tab = customtkinter.CTkTabview(master=app, width=965, height=500)
tab.pack(padx=XWidgetPadding, pady=YWidgetPadding)

tab.add("Klasifikasi")
tab.add("Panduan")
tab.add("Tentang")
tab.set("Klasifikasi")

# Cap Shape
def ComboCapShape_Callback(choice):
    if choice == "Lonceng":
        user_entry[0,0] = 4
    elif choice == "Kerucut":
        user_entry[0,0] = 6
    elif choice == "Cembung":
        user_entry[0,0] = 1
    elif choice == "Datar":
        user_entry[0,0] = 2
    elif choice == "Cekung":
        user_entry[0,0] = 5
    elif choice == "Benjol":
        user_entry[0,0] = 3

labelCapShape = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Bentuk Tudung")
ComboCapShape = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Lonceng", "Kerucut", "Cembung", "Datar", "Cekung", "Benjol"],
                                     command=ComboCapShape_Callback)
ComboCapShape.set("Lonceng")

labelCapShape.grid(row=0, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboCapShape.grid(row=0, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Cap Surface
def ComboCapSurface_Callback(choice):
    if choice == "Berserat":
        user_entry[0,1] = 2
    elif choice == "Melekuk":
        user_entry[0,1] = 4
    elif choice == "Bersisik":
        user_entry[0,1] = 1
    elif choice == "Halus":
        user_entry[0,1] = 3

labelCapSurface = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Permukaan Tudung")
ComboCapSurface = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Berserat", "Melekuk", "Bersisik", "Halus"],
                                     command=ComboCapSurface_Callback)
ComboCapSurface.set("Berserat")

labelCapSurface.grid(row=1, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboCapSurface.grid(row=1, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Cap Color
def ComboCapColor_Callback(choice):
    if choice == "Coklat":
        user_entry[0,2] = 4
    elif choice == "Kuning Muda":
        user_entry[0,2] = 6
    elif choice == "Kayu Manis":
        user_entry[0,2] = 8
    elif choice == "Abu-Abu":
        user_entry[0,2] = 2
    elif choice == "Hijau":
        user_entry[0,2] = 10
    elif choice == "Merah Muda":
        user_entry[0,2] = 7
    elif choice == "Ungu":
        user_entry[0,2] = 9
    elif choice == "Merah":
        user_entry[0,2] = 5
    elif choice == "Putih":
        user_entry[0,2] = 3
    elif choice == "Kuning":
        user_entry[0,2] = 1

labelCapColor = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Tudung")
ComboCapColor = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Coklat", "Kuning Muda", "Kayu Manis", "Abu-Abu", "Hijau", "Merah Muda", "Ungu", "Merah", "Putih", "Kuning"],
                                     command=ComboCapColor_Callback)
ComboCapColor.set("Coklat")

labelCapColor.grid(row=2, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboCapColor.grid(row=2, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Bruises
def ComboBruises_Callback(choice):
    if choice == "Ada":
        user_entry[0,3] = 2
    elif choice == "Tidak Ada":
        user_entry[0,3] = 1

LabelBruises = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Memar")
ComboBruises = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Ada", "Tidak Ada"],
                                     command=ComboBruises_Callback)
ComboBruises.set("Ada")

LabelBruises.grid(row=3, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboBruises.grid(row=3, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Odor
def ComboOdor_Callback(choice):
    if choice == "Busuk":
        user_entry[0,4] = 1
    elif choice == "Tidak Berbau":
        user_entry[0,4] = 2
    elif choice == "Pedas":
        user_entry[0,4] = 3
    elif choice == "Kayu Bakar":
        user_entry[0,4] = 4
    elif choice == "Amis":
        user_entry[0,4] = 5
    elif choice == "Menusuk":
        user_entry[0,4] = 6
    elif choice == "Almond":
        user_entry[0,4] = 7
    elif choice == "Adas Manis":
        user_entry[0,4] = 8
    elif choice == "Debu Lembab":
        user_entry[0,4] = 9

LabelOdor = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Bau")
ComboOdor = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Busuk", "Tidak Berbau", "Pedas", "Kayu Bakar", "Amis", "Menusuk", "Almond", "Adas Manis", "Debu Lembab"],
                                     command=ComboOdor_Callback)
ComboOdor.set("Tidak Berbau")

LabelOdor.grid(row=4, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboOdor.grid(row=4, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Gill Attachment
def ComboGillAttachment_Callback(choice):
    if choice == "Terlepas":
        user_entry[0,5] = 1
    elif choice == "Tersambung":
        user_entry[0,5] = 2

LabelGillAttachment = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Sambungan Bilah")
ComboGillAttachment = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Terlepas", "Tersambung"],
                                     command=ComboGillAttachment_Callback)
ComboGillAttachment.set("Terlepas")

LabelGillAttachment.grid(row=5, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboGillAttachment.grid(row=5, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Gill Spacing
def ComboGillSpacing_Callback(choice):
    if choice == "Rapat Rapih":
        user_entry[0,6] = 1
    elif choice == "Tumpang Tindih":
        user_entry[0,6] = 2

LabelGillSpacing = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Jarak Bilah")
ComboGillSpacing = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Rapat Rapih", "Tumpang Tindih"],
                                     command=ComboGillSpacing_Callback)
ComboGillSpacing.set("Tumpang Tindih")

LabelGillSpacing.grid(row=6, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboGillSpacing.grid(row=6, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Gill Size
def ComboGillSize_Callback(choice):
    if choice == "Lebar":
        user_entry[0,7] = 1
    elif choice == "Sempit":
        user_entry[0,7] = 2

LabelGillSize = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Ukuran Bilah")
ComboGillSize = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Lebar", "Sempit"],
                                     command=ComboGillSize_Callback)
ComboGillSize.set("Lebar")

LabelGillSize.grid(row=7, column=0, padx=XWidgetPadding, pady=YWidgetPadding)
ComboGillSize.grid(row=7, column=1, padx=XWidgetPadding, pady=YWidgetPadding)

# Gill Color
def ComboGillColor_Callback(choice):
    if choice == "Merah Muda":
        user_entry[0,8] = 1
    elif choice == "Coklat Tua":
        user_entry[0,8] = 2
    elif choice == "Kuning Muda":
        user_entry[0,8] = 3
    elif choice == "Kecoklatan":
        user_entry[0,8] = 4
    elif choice == "Abu-Abu":
        user_entry[0,8] = 5
    elif choice == "Ungu":
        user_entry[0,8] = 6
    elif choice == "Jingga":
        user_entry[0,8] = 7
    elif choice == "Kuning":
        user_entry[0,8] = 8
    elif choice == "Putih":
        user_entry[0,8] = 9
    elif choice == "Hitam":
        user_entry[0,8] = 10
    elif choice == "Merah":
        user_entry[0,8] = 11
    elif choice == "Hijau":
        user_entry[0,8] = 12

LabelGillColor = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Bilah")
ComboGillColor = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Merah Muda", "Coklat Tua", "Kuning Muda", "Kecoklatan", "Abu-Abu", "Ungu", "Jingga", "Kuning", "Putih", "Hitam", "Merah", "Hijau"],
                                     command=ComboGillColor_Callback)
ComboGillColor.set("Hijau")

LabelGillColor.grid(row=0, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboGillColor.grid(row=0, column=3, padx=XWidgetPadding, pady=YWidgetPadding)


# Stalk Shape
def ComboStalkShape_Callback(choice):
    if choice == "Membesar":
        user_entry[0,9] = 1
    elif choice == "Mengecil":
        user_entry[0,9] = 2

LabelStalkShape = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Bentuk Batang")
ComboStalkShape = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Membesar", "Mengecil"],
                                     command=ComboStalkShape_Callback)
ComboStalkShape.set("Membesar")

LabelStalkShape.grid(row=1, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkShape.grid(row=1, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Stalk Root
def ComboStalkRoot_Callback(choice):
    if choice == "Bonggol":
        user_entry[0,10] = 1
    elif choice == "Rata":
        user_entry[0,10] = 2
    elif choice == "Hilang":
        user_entry[0,10] = 3
    elif choice == "Menjulur":
        user_entry[0,10] = 4
    elif choice == "Akar Gada":
        user_entry[0,10] = 5

LabelStalkRoot = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Akar Batang")
ComboStalkRoot = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Bonggol", "Rata", "Hilang", "Menjulur", "Akar Gada"],
                                     command=ComboStalkRoot_Callback)
ComboStalkRoot.set("Menjulur")

LabelStalkRoot.grid(row=2, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkRoot.grid(row=2, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Stalk Surface Above Ring
def ComboStalkSurfaceAboveRing_Callback(choice):
    if choice == "Halus Berbulu":
        user_entry[0,11] = 1
    elif choice == "Halus":
        user_entry[0,11] = 2
    elif choice == "Berserat":
        user_entry[0,11] = 3
    elif choice == "Bersisik":
        user_entry[0,11] = 4

LabelStalkSurfaceAboveRing = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Permukaan Batang Atas")
ComboStalkSurfaceAboveRing = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Halus Berbulu", "Halus", "Berserat", "Bersisik"],
                                     command=ComboStalkSurfaceAboveRing_Callback)
ComboStalkSurfaceAboveRing.set("Halus Berbulu")

LabelStalkSurfaceAboveRing.grid(row=3, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkSurfaceAboveRing.grid(row=3, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Stalk Surface Below Ring
def ComboStalkSurfaceBelowRing_Callback(choice):
    if choice == "Halus Berbulu":
        user_entry[0,12] = 1
    elif choice == "Halus":
        user_entry[0,12] = 2
    elif choice == "Berserat":
        user_entry[0,12] = 3
    elif choice == "Bersisik":
        user_entry[0,12] = 4

LabelStalkSurfaceBelowRing = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Permukaan Batang Bawah")
ComboStalkSurfaceBelowRing = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Halus Berbulu", "Halus", "Berserat", "Bersisik"],
                                     command=ComboStalkSurfaceBelowRing_Callback)
ComboStalkSurfaceBelowRing.set("Bersisik")

LabelStalkSurfaceBelowRing.grid(row=4, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkSurfaceBelowRing.grid(row=4, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Stalk Color Above Ring
def ComboStalkColorAboveRing_Callback(choice):
    if choice == "Merah Muda":
        user_entry[0,13] = 1
    elif choice == "Abu-Abu":
        user_entry[0,13] = 2
    elif choice == "Putih":
        user_entry[0,13] = 3
    elif choice == "Jingga":
        user_entry[0,13] = 4
    elif choice == "Kuning Muda":
        user_entry[0,13] = 5
    elif choice == "Merah":
        user_entry[0,13] = 6
    elif choice == "Coklat":
        user_entry[0,13] = 7
    elif choice == "Kayu Manis":
        user_entry[0,13] = 8
    elif choice == "Kuning":
        user_entry[0,13] = 9

LabelStalkColorAboveRing = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Batang Atas")
ComboStalkColorAboveRing = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Merah Muda", "Abu-Abu", "Putih", "Jingga", "Kuning Muda", "Merah", "Coklat", "Kayu Manis", "Kuning"],
                                     command=ComboStalkColorAboveRing_Callback)
ComboStalkColorAboveRing.set("Putih")

LabelStalkColorAboveRing.grid(row=5, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkColorAboveRing.grid(row=5, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Stalk Color Below Ring
def ComboStalkColorBelowRing_Callback(choice):
    if choice == "Merah Muda":
        user_entry[0,14] = 1
    elif choice == "Abu-Abu":
        user_entry[0,14] = 2
    elif choice == "Putih":
        user_entry[0,14] = 3
    elif choice == "Jingga":
        user_entry[0,14] = 4
    elif choice == "Kuning Muda":
        user_entry[0,14] = 5
    elif choice == "Merah":
        user_entry[0,14] = 6
    elif choice == "Coklat":
        user_entry[0,14] = 7
    elif choice == "Kayu Manis":
        user_entry[0,14] = 8
    elif choice == "Kuning":
        user_entry[0,14] = 9

LabelStalkColorBelowRing = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Batang Bawah")
ComboStalkColorBelowRing = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Merah Muda", "Abu-Abu", "Putih", "Jingga", "Kuning Muda", "Merah", "Coklat", "Kayu Manis", "Kuning"],
                                     command=ComboStalkColorBelowRing_Callback)
ComboStalkColorBelowRing.set("Merah Muda")

LabelStalkColorBelowRing.grid(row=6, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboStalkColorBelowRing.grid(row=6, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Veil Type
def ComboVeilType_Callback(choice):
    if choice == "Sebagian":
        user_entry[0,15] = 1

LabelVeilType = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Jenis Kelubung")
ComboVeilType = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Sebagian"],
                                     command=ComboVeilType_Callback)
ComboVeilType.set("Sebagian")

LabelVeilType.grid(row=7, column=2, padx=XWidgetPadding, pady=YWidgetPadding)
ComboVeilType.grid(row=7, column=3, padx=XWidgetPadding, pady=YWidgetPadding)

# Veil Color
def ComboVeilColor_Callback(choice):
    if choice == "Putih":
        user_entry[0,16] = 1
    elif choice == "Coklat":
        user_entry[0,16] = 2
    elif choice == "Jingga":
        user_entry[0,16] = 3
    elif choice == "Kuning":
        user_entry[0,16] = 4

LabelVeilColor = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Kelubung")
ComboVeilColor = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Putih", "Coklat", "Jingga", "Kuning"],
                                     command=ComboVeilColor_Callback)
ComboVeilColor.set("Kuning")

LabelVeilColor.grid(row=0, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboVeilColor.grid(row=0, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Ring Number
def ComboRingNumber_Callback(choice):
    if choice == "1":
        user_entry[0,17] = 1
    elif choice == "2":
        user_entry[0,17] = 2
    elif choice == "Tidk Ada":
        user_entry[0,17] = 3

LabelRingNumber = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Jumlah Cincin")
ComboRingNumber = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["1", "2", "Tidak Ada"],
                                     command=ComboRingNumber_Callback)
ComboRingNumber.set("Tidak Ada")

LabelRingNumber.grid(row=1, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboRingNumber.grid(row=1, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Ring Type
def ComboRingType_Callback(choice):
    if choice == "Besar":
        user_entry[0,18] = 1
    elif choice == "Menggantung":
        user_entry[0,18] = 2
    elif choice == "Menghilang":
        user_entry[0,18] = 3
    elif choice == "Melengkung Keluar":
        user_entry[0,18] = 4
    elif choice == "Tidak Ada":
        user_entry[0,18] = 5

LabelRingType = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Jenis Cincin")
ComboRingType = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Besar", "Menggantung", "Menghilang", "Melengkung Keluar", "Tidak Ada"],
                                     command=ComboRingType_Callback)
ComboRingType.set("Menggantung")

LabelRingType.grid(row=2, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboRingType.grid(row=2, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Spore Print Color
def ComboSporePrintColor_Callback(choice):
    if choice == "Coklat Tua":
        user_entry[0,19] = 1
    elif choice == "Kecoklatan":
        user_entry[0,19] = 2
    elif choice == "Hitam":
        user_entry[0,19] = 3
    elif choice == "Putih":
        user_entry[0,19] = 4
    elif choice == "Kuning":
        user_entry[0,19] = 5
    elif choice == "Kuning Muda":
        user_entry[0,19] = 6
    elif choice == "Hijau":
        user_entry[0,19] = 7
    elif choice == "Ungu":
        user_entry[0,19] = 8
    elif choice == "Jingga":
        user_entry[0,19] = 9

LabelSporePrintColor = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Warna Spora")
ComboSporePrintColor = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Coklat Tua", "Kecoklatan", "Hitam", "Putih", "Kuning", "Kuning Muda", "Hijau", "Ungu", "Jingga"],
                                     command=ComboSporePrintColor_Callback)
ComboSporePrintColor.set("Coklat Tua")

LabelSporePrintColor.grid(row=3, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboSporePrintColor.grid(row=3, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Population
def ComboPopulation_Callback(choice):
    if choice == "Tunggal":
        user_entry[0,20] = 1
    elif choice == "Berkelompok Kecil":
        user_entry[0,20] = 2
    elif choice == "Berkelompok Besar":
        user_entry[0,20] = 3
    elif choice == "Tersebar":
        user_entry[0,20] = 4
    elif choice == "Berkelompok Terklasterisasi":
        user_entry[0,20] = 5
    elif choice == "Bercampuran":
        user_entry[0,20] = 6

LabelPopulation = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Populasi")
ComboPopulation = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Tunggal", "Berkelompok Kecil", "Berkelompok Besar", "Tersebar", "Berkelompok Terklasterisasi", "Bercampuran"],
                                     command=ComboPopulation_Callback)
ComboPopulation.set("Berkelompok Kecil")

LabelPopulation.grid(row=4, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboPopulation.grid(row=4, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Habitat
def ComboHabitat_Callback(choice):
    if choice == "Rerumputan":
        user_entry[0,21] = 1
    elif choice == "Kayu-Kayuan":
        user_entry[0,21] = 2
    elif choice == "Dedaunan":
        user_entry[0,21] = 3
    elif choice == "Jalanan":
        user_entry[0,21] = 4
    elif choice == "Sampah":
        user_entry[0,21] = 5
    elif choice == "Perkotaan":
        user_entry[0,21] = 6
    elif choice == "Padang Rumput":
        user_entry[0,21] = 7

LabelHabitat = customtkinter.CTkLabel(master=tab.tab("Klasifikasi"), text="Habitat")
ComboHabitat = customtkinter.CTkComboBox(master=tab.tab("Klasifikasi"), values=["Rerumputan", "Kayu-Kayuan", "Dedaunan", "Jalanan", "Sampah", "Perkotaan", "Padang Rumput"],
                                     command=ComboHabitat_Callback)
ComboHabitat.set("Kayu-Kayuan")

LabelHabitat.grid(row=5, column=4, padx=XWidgetPadding, pady=YWidgetPadding)
ComboHabitat.grid(row=5, column=5, padx=XWidgetPadding, pady=YWidgetPadding)

# Predict Button
def ButtonPredict_Pressed():
    df_user_entry = pd.DataFrame(user_entry, columns=['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'])
    user_pred = mdt.clf_gini.predict(df_user_entry)
    if user_pred == "p":
        user_pred = "Jamur Terindikasi Beracun"
    elif user_pred == "e":
        user_pred = "Jamur Terindikasi Dapat Dimakan"

    # Predict Dialog

    TopResult = customtkinter.CTkToplevel(app)
    TopResult.title("Hasil Identifikasi")
    TopResultWidth = TopResult.winfo_screenwidth()
    TopResultHeight = TopResult.winfo_screenheight()
    TopResultXCenterPos = (TopResultWidth // 2) - (300 // 2)
    TopResultYCenterPos = (TopResultHeight // 2) - (125 // 2)
    TopResult.geometry(f"{300}x{125}+{TopResultXCenterPos}+{TopResultYCenterPos}")
    TopResult.resizable(width=False, height=False)
    TopResult.grab_set()

    LabelResult = customtkinter.CTkLabel(master=TopResult, text=user_pred)
    LabelResult.pack(padx=XWidgetPadding, pady=YWidgetPadding)

    def ButtonBackMain_Pressed():
        TopResult.destroy()

    ButtonBackMain = customtkinter.CTkButton(master=TopResult, text="Tutup", command=ButtonBackMain_Pressed)
    ButtonBackMain.pack(padx=XWidgetPadding, pady=YWidgetPadding)

ButtonPredict = customtkinter.CTkButton(master=tab.tab("Klasifikasi"), text="Identifikasi", command=ButtonPredict_Pressed, width=255, height=80)

ButtonPredict.grid(row=6, rowspan=7, column=4, columnspan=5, padx=XWidgetPadding, pady=YWidgetPadding)

# How To

def ButtonMushroomAnatomy_Pressed():
    try:
        os.startfile("mushroomanatomybybuggbuzz.jpg")
    except:
        print("Tidak dapat membuka image viewer")

ButtonMushroomAnatomy = customtkinter.CTkButton(master=tab.tab("Panduan"), text="Buka Gambar Anatomi Jamur", command=ButtonMushroomAnatomy_Pressed)

TextHowTo = customtkinter.CTkTextbox(master=tab.tab("Panduan"), width=965, height=350)

TextHowTo.insert("0.0", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at tincidunt tellus. Aliquam faucibus libero dapibus dui sodales, posuere pharetra ligula ultricies. Ut eget convallis mauris. Etiam vitae diam placerat, ornare nibh eu, semper elit. Donec venenatis congue elit, sed eleifend mi dignissim eu. Maecenas finibus lacus magna, sed facilisis risus elementum quis. In in ipsum ut diam vehicula luctus. Maecenas nisi lacus, efficitur at metus a, congue accumsan dui.")
TextHowTo.configure(state="disabled")
TextHowTo.pack(padx=XWidgetPadding, pady=YWidgetPadding)
ButtonMushroomAnatomy.pack(padx=XWidgetPadding, pady=YWidgetPadding)

# About

def ButtonDataset_Pressed():
    webbrowser.open("https://www.kaggle.com/datasets/uciml/mushroom-classification")

ButtonDataset = customtkinter.CTkButton(master=tab.tab("Tentang"), text="Buka Sumber Dataset", command=ButtonDataset_Pressed)

TextAbout = customtkinter.CTkTextbox(master=tab.tab("Tentang"), width=965, height=350)

TextAbout.insert("0.0", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at tincidunt tellus. Aliquam faucibus libero dapibus dui sodales, posuere pharetra ligula ultricies. Ut eget convallis mauris. Etiam vitae diam placerat, ornare nibh eu, semper elit. Donec venenatis congue elit, sed eleifend mi dignissim eu. Maecenas finibus lacus magna, sed facilisis risus elementum quis. In in ipsum ut diam vehicula luctus. Maecenas nisi lacus, efficitur at metus a, congue accumsan dui.")
TextAbout.configure(state="disabled")
TextAbout.pack(padx=XWidgetPadding, pady=YWidgetPadding)
ButtonDataset.pack(padx=XWidgetPadding, pady=YWidgetPadding)

app.mainloop()