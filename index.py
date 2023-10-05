# pip install pillow 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox 
import math, random, os 


class Facture:
    def __init__(self, root):
        self.root = root
        self.root.title("Facture")
        self.root.geometry("1600x900")
        
        title = Label(self.root, text="RESTAURANT ESSA", bd=20, relief=RAISED, font=("Algerian", 40), bg="cyan", fg="black")
        title.place(x=550, y=0)
        
        self.logo = ImageTk.PhotoImage(Image.open("C:/Users/AZIZ-CISSE/ProjetPython/gestion_platet_facture_resto/image/loga.jpg"))
        self.logopo = Label(image=self.logo)
        self.logopo.place(x=60, y=0)
        
    ###########Variable######
     ######Variable Petit Dejeuner#####
        self.petitdj1 = IntVar()
        self.petitdj2 = IntVar()
        self.petitdj3 = IntVar()
        self.petitdj4 = IntVar()
        self.petitdj5 = IntVar()
        self.petitdj6 = IntVar()
        self.petitdj7 = IntVar()
        
      ######Variable Repas#####
        self.repas1 = IntVar()
        self.repas2 = IntVar()
        self.repas3 = IntVar()
        self.repas4 = IntVar()
        self.repas5 = IntVar()
        self.repas6 = IntVar()
        self.repas7 = IntVar()
        
    #######Variable Diner######
        self.diner1 = IntVar()
        self.diner2 = IntVar()
        self.diner3 = IntVar()
        self.diner4 = IntVar()
        self.diner5 = IntVar()
        self.diner6 = IntVar()
        self.diner7 = IntVar()
        
    #######Somme à Payer#######
        self.prix_total_petit_dej = StringVar()
        self.prix_total_repas = StringVar()
        self.prix_total_diner = StringVar()
        
        self.taxe_petit_dej = StringVar()
        self.taxe_repas = StringVar()
        self.taxe_diner = StringVar()
        
    ########Détails du Client######
        self.nom_client = StringVar()
        self.tel_client = StringVar()
        
        self.numero_facture = StringVar()
        x = random.randint(1000,9999)
        self.numero_facture.set(str(x))
        
        self.recherche_facture = StringVar()
        
    
    
    ##########Les Détails du Client#######   
        Frame1 = LabelFrame(self.root, text="Details du Client", font=("times new roman", 18, "bold"), fg="gold", bg="gray")
        Frame1.place(x=0, y=100, relwidth=1)
        
        dnom = Label(Frame1, text="Nom du Client", bg="gray", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=20, pady=5)
        enom = Entry(Frame1, width=24, textvariable=self.nom_client, font=("times new roman", 15), bd=10, relief=SUNKEN).grid(row=0, column=1,  padx=10, pady=5)
    
    
        dphone = Label(Frame1, text="Numero Telephone", bg="gray", font=("times new roman", 16, "bold")).grid(row=0, column=2, padx=20, pady=5)
        ephone= Entry(Frame1, width=24, textvariable=self.tel_client, font=("times new roman", 15), bd=10, relief=SUNKEN).grid(row=0, column=3,  padx=10, pady=5)
        
        dfacture = Label(Frame1, text="Numero Facture", bg="gray", font=("times new roman", 16, "bold")).grid(row=0, column=4, padx=20, pady=5)
        efacture = Entry(Frame1, width=24, textvariable=self.recherche_facture, font=("times new roman", 15), bd=10, relief=SUNKEN).grid(row=0, column=5,  padx=10, pady=5)
    
        bill_btn = Button(Frame1, text="Rechercher", width=12, bd=7, command=self.recherche, relief=GROOVE, font=("times new roman", 12, "bold")).grid(row=0, column=6, padx=10, pady=5)
        
        
    ##############Menu du Petit Déjeuner#######
        Frame2 = LabelFrame(self.root, text="Petit Dejeuner", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"), fg="lightgreen", bg="gray")
        Frame2.place(x=5, y=205, width=370, height=420)

        platDej1 = Label(Frame2, text="Cafe ak Mew", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        platDej1_txt = Entry(Frame2, width=16, textvariable=self.petitdj1, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)
        
        platDej2 = Label(Frame2, text="Lakh", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        platDej2_txt = Entry(Frame2, width=16, textvariable=self.petitdj2, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)
        
        platDej3 = Label(Frame2, text="Douté", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        platDej3_txt = Entry(Frame2, width=16, textvariable=self.petitdj3, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)
        
        platDej4 = Label(Frame2, text="Mbourok Ton", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        platDej4_txt = Entry(Frame2, width=16, textvariable=self.petitdj4, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)
        
        platDej5 = Label(Frame2, text="Omellete", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        platDej5_txt = Entry(Frame2, width=16, textvariable=self.petitdj5, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)
 
        platDej6 = Label(Frame2, text="Nen Bakhal", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        platDej6_txt = Entry(Frame2, width=16, textvariable=self.petitdj6, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=5, column=1, padx=10, pady=10)
        
        platDej7 = Label(Frame2, text="Cafe Touba", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        platDej7_txt = Entry(Frame2, width=16, textvariable=self.petitdj7, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)


    ############Menu du Repas#######
        Frame3 = LabelFrame(self.root, text="Repas", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"), fg="lightgreen", bg="gray")
        Frame3.place(x=390, y=205, width=370, height=420)
   
        repas1 = Label(Frame3, text="Maffe", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        repas1_txt = Entry(Frame3, width=16, textvariable=self.repas1, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)

        repas2 = Label(Frame3, text="Soupou-Kandia", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        repas2_txt = Entry(Frame3, width=16, textvariable=self.repas2,font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)

        repas3 = Label(Frame3, text="Thieb-Yapp", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        repas3_txt = Entry(Frame3, width=16, textvariable=self.repas3,font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)  

        repas4 = Label(Frame3, text="Mbakhal", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        repas4_txt = Entry(Frame3, width=16, textvariable=self.repas4, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)

        repas5 = Label(Frame3, text="Yassa", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        repas5_txt = Entry(Frame3, width=16, textvariable=self.repas5, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)

        repas6 = Label(Frame3, text="Dakhine", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        repas6_txt = Entry(Frame3, width=16, textvariable=self.repas6, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=5, column=1, padx=10, pady=10)
        
        repas7 = Label(Frame3, text="Thiebou-Djeun", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        repas7_txt = Entry(Frame3, width=16, textvariable=self.repas7, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)


    ##########Menu du Diner#######
        Frame4 = LabelFrame(self.root, text="Diner", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"), fg="lightgreen", bg="gray")
        Frame4.place(x=775, y=205, width=370, height=420)
   
        diner1 = Label(Frame4, text="Thiere", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        diner1_txt = Entry(Frame4, width=16, textvariable=self.diner1, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)

        diner2 = Label(Frame4, text="Sauce", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        diner2_txt = Entry(Frame4, width=16, textvariable=self.diner2, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)

        diner3 = Label(Frame4, text="Couscous", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        diner3_txt = Entry(Frame4, width=16, textvariable=self.diner3, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)  

        diner4 = Label(Frame4, text="Raggo", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        diner4_txt = Entry(Frame4, width=16, textvariable=self.diner4, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)

        diner5 = Label(Frame4, text="Ndambe", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        diner5_txt = Entry(Frame4, width=16, textvariable=self.diner5, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)

        diner6 = Label(Frame4, text="Soupou", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        diner6_txt = Entry(Frame4, width=16, textvariable=self.diner6, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=5, column=1, padx=10, pady=10)
        
        diner7 = Label(Frame4, text="Petit-Poid", font=("times new roman", 16, "bold"), fg="cyan", bg="gray").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        diner7_txt = Entry(Frame4, width=16, textvariable=self.diner7, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN, justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)


    ###########Facture########
        Frame5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        Frame5.place(x=1160, y=205, width=430, height=420)
        
        facture_lbl = Label(Frame5, text="Facturation", font=("arial", 20, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Frame5, orient=VERTICAL)
        self.text = Text(Frame5, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.text.yview)
        self.text.pack(fill=BOTH, expand=1)
        
        
    #########Montant A Payer#########
        Frame6 = LabelFrame(self.root, text="Somme à Payer", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"), fg="lightgreen", bg="gray")
        Frame6.place(x=0, y=630, relwidth=1, height=450)
        
    #######Prix Normal######
        prixPDJ = Label(Frame6, text="Prix Petit Dejeuner Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        prixPDJ_txt = Entry(Frame6, width=15, textvariable=self.prix_total_petit_dej, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)
        
        prixRep = Label(Frame6, text="Prix Repas Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        prixRep_txt = Entry(Frame6, width=15, textvariable=self.prix_total_repas, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)

        prixDiner = Label(Frame6, text="Prix Diner Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        prixDiner_txt = Entry(Frame6, width=15, textvariable=self.prix_total_diner, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)


    #######Taxe########
        taxePDJ = Label(Frame6, text="Taxe Petit Dejeuner Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        taxePDJ_txt = Entry(Frame6, width=15, textvariable=self.taxe_petit_dej, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=1, column=3, padx=10, pady=10)
        
        taxeRep = Label(Frame6, text="Taxe Repas Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        taxeRep_txt = Entry(Frame6, width=15, textvariable=self.taxe_repas, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=2, column=3, padx=10, pady=10)

        taxeDiner = Label(Frame6, text="Taxe Diner Total", font=("times new roman", 16, "bold"), fg="orange", bg="gray").grid(row=3, column=2, padx=10, pady=10, sticky="w")
        taxeDiner_txt = Entry(Frame6, width=15, textvariable=self.taxe_diner, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN, justify=RIGHT).grid(row=3, column=3, padx=10, pady=10)


    #######Button####
        Frame7 = LabelFrame(Frame6, bd=10, relief=GROOVE)
        Frame7.place(x=920, width=640, height=160)

        Total_btn = Button(Frame7, text="Prix Total", command=self.total, width=18, bd=7, relief=GROOVE, font=("times new roman", 18, "bold"), bg="green").grid(row=1, column=0, padx=20, pady=10)
        generer_fact_btn = Button(Frame7, text="Générer Facture", command=self.generer_facture, width=18, bd=7, relief=GROOVE, font=("times new roman", 18, "bold"), bg="yellow").grid(row=1, column=2, padx=20, pady=10)
        reinit_btn = Button(Frame7, text="Réinitialiser", command=self.reinitialiser, width=18, bd=7, relief=GROOVE, font=("times new roman", 18, "bold"), bg="gray").grid(row=2, column=0, padx=20, pady=10)
        quit_btn = Button(Frame7, text="Quitter", command=self.quitter, width=18, bd=7, relief=GROOVE, font=("times new roman", 18, "bold"), bg="red").grid(row=2, column=2, padx=20, pady=10)
        self.afficher_facture()

    def total(self):
        #####Petit Déjeuner##
        self.ptdj1 = self.petitdj1.get() * 300
        self.ptdj2 = self.petitdj2.get() * 400
        self.ptdj3 = self.petitdj3.get() * 100
        self.ptdj4 = self.petitdj4.get() * 200
        self.ptdj5 = self.petitdj5.get() * 250
        self.ptdj6 = self.petitdj6.get() * 150
        self.ptdj7 = self.petitdj7.get() * 50
        
        self.total_petit_Dej = int(self.ptdj1 + self.ptdj2 + self.ptdj3 + self.ptdj4 + self.ptdj5 + self.ptdj6 + self.ptdj7)
        self.prix_total_petit_dej.set(str(self.total_petit_Dej))
        
        self.taxe_petit_dj = round((self.total_petit_Dej * 0.05),2)
        self.taxe_petit_dej.set(str(self.taxe_petit_dj))


        #####Repas#####
        self.rep1 = self.repas1.get() * 700
        self.rep2 = self.repas2.get() * 600
        self.rep3 = self.repas3.get() * 800
        self.rep4 = self.repas4.get() * 500
        self.rep5 = self.repas5.get() * 650
        self.rep6 = self.repas6.get() * 500
        self.rep7 = self.repas7.get() * 700

        self.total_Repa = int(self.rep1 + self.rep2 + self.rep3 + self.rep4 + self.rep5 + self.rep6 + self.rep7)
        self.prix_total_repas.set(str(self.total_Repa))
        
        self.taxe_repa = round((self.total_Repa * 0.05),2)
        self.taxe_repas.set(str(self.taxe_repa))
        
        
        #########Diner######
        self.dine1 = self.diner1.get() * 500
        self.dine2 = self.diner2.get() * 600
        self.dine3 = self.diner3.get() * 700
        self.dine4 = self.diner4.get() * 800
        self.dine5 = self.diner5.get() * 1000
        self.dine6 = self.diner6.get() * 1100
        self.dine7 = self.diner7.get() * 1200
        
        self.total_Din = int(self.dine1 + self.dine2 + self.dine3 + self.dine4 + self.dine5 + self.dine6 + self.dine7)
        self.prix_total_diner.set(str(self.total_Din))
        
        self.taxe_din = round((self.total_Din * 0.05),2)
        self.taxe_diner.set(str(self.taxe_din))

        
        self.Total_facture = float(self.total_petit_Dej + self.total_Repa + self.total_Din + self.taxe_petit_dj + self.taxe_repa + self.taxe_din)
        
    
    def afficher_facture(self):
        self.text.delete("1.0", END)
        self.text.insert(END, "**************BIENVENUE CHEZ ESSA***************")
        
        self.text.insert(END, "\n Numero Facture : "+self.numero_facture.get())
        
        self.text.insert(END, "\n Nom Client : "+self.nom_client.get())
        
        self.text.insert(END, "\n Numero Telephone : "+self.tel_client.get())
        
        self.text.insert(END, "\n================================================")
        self.text.insert(END, "\n Produits \t\t Quantite \t\t Prix \t\t")
        self.text.insert(END, "\n================================================")
        
        
    def generer_facture(self):
        if self.nom_client.get()=="" or self.tel_client.get()=="":
            messagebox.showerror("Erreur", "Le nom du client ou le numero de telephone est obligatoire")
        elif self.prix_total_petit_dej.get()=="0" and self.prix_total_repas.get()=="0" and self.prix_total_diner.get()=="0":
            messagebox.showerror("Erreur", "Veuiller Selectionner vos Plats")
        else:
            self.afficher_facture()
            #Petit Déjeuner
            if self.petitdj1.get()!=0:
                self.text.insert(END, f"\nCafe ak Mew \t\t {self.petitdj1.get()} \t\t {self.ptdj1} FCFA")
            
            if self.petitdj2.get()!=0:
                self.text.insert(END, f"\nLakh \t\t {self.petitdj2.get()} \t\t {self.ptdj2} FCFA")

            if self.petitdj3.get()!=0:
                self.text.insert(END, f"\nDouté \t\t {self.petitdj3.get()} \t\t {self.ptdj3} FCFA")

            if self.petitdj4.get()!=0:
                self.text.insert(END, f"\nMbourok Ton \t\t {self.petitdj4.get()} \t\t {self.ptdj4} FCFA")
                
            if self.petitdj5.get()!=0:
                self.text.insert(END, f"\nOmellete \t\t {self.petitdj5.get()} \t\t {self.ptdj5} FCFA")
                
            if self.petitdj6.get()!=0:
                self.text.insert(END, f"\nNen Bakhal \t\t {self.petitdj6.get()} \t\t {self.ptdj6} FCFA")
                
            if self.petitdj7.get()!=0:
                self.text.insert(END, f"\nCafe Touba \t\t {self.petitdj7.get()} \t\t {self.ptdj7} FCFA")
                
        #Repas
            if self.repas1.get()!=0:
                self.text.insert(END, f"\nMaffe \t\t {self.repas1.get()} \t\t {self.rep1} FCFA")
            
            if self.repas2.get()!=0:
                self.text.insert(END, f"\nSoupou-Kandia \t\t {self.repas2.get()} \t\t {self.rep2} FCFA")

            if self.repas3.get()!=0:
                self.text.insert(END, f"\nThieb-Yapp \t\t {self.repas3.get()} \t\t {self.rep3} FCFA")

            if self.repas4.get()!=0:
                self.text.insert(END, f"\nMbakhal \t\t {self.repas4.get()} \t\t {self.rep4} FCFA")
                
            if self.repas5.get()!=0:
                self.text.insert(END, f"\nYassa \t\t {self.repas5.get()} \t\t {self.rep5} FCFA")
                
            if self.repas6.get()!=0:
                self.text.insert(END, f"\nDakhine \t\t {self.repas6.get()} \t\t {self.rep6} FCFA")
                
            if self.repas7.get()!=0:
                self.text.insert(END, f"\nThiebou-Djeun \t\t {self.repas7.get()} \t\t {self.rep7} FCFA")
                
                        
        #Diner
            if self.diner1.get()!=0:
                self.text.insert(END, f"\nThiere \t\t {self.diner1.get()} \t\t {self.dine1} FCFA")
            
            if self.diner2.get()!=0:
                self.text.insert(END, f"\nSauce\t\t {self.diner2.get()} \t\t {self.dine2} FCFA")

            if self.diner3.get()!=0:
                self.text.insert(END, f"\nCouscous \t\t {self.diner3.get()} \t\t {self.dine3} FCFA")

            if self.diner4.get()!=0:
                self.text.insert(END, f"\nRaggo \t\t {self.diner4.get()} \t\t {self.dine4} FCFA")
                
            if self.diner5.get()!=0:
                self.text.insert(END, f"\nNdambe \t\t {self.diner5.get()} \t\t {self.dine5} FCFA")
                
            if self.diner6.get()!=0:
                self.text.insert(END, f"\nSoupou \t\t {self.diner6.get()} \t\t {self.dine6} FCFA")
                
            if self.diner7.get()!=0:
                self.text.insert(END, f"\nPetit-Poid \t\t {self.diner7.get()} \t\t {self.dine7} FCFA")
                
            self.text.insert(END, "\n================================================")
            self.text.insert(END, f"\n\n Somme Totale : \t\t\t\t {self.Total_facture}")
            self.text.insert(END, "\n================================================")
            
            self.sauvegarder()
            
            
            
     #######Fonction pour sauvegarder la facture#########       
    def sauvegarder(self):
        op = messagebox.askyesno("Sauvegarder La Facture", "Voulez-Vous Sauvegarder La Facture?")
        if op > 0:
            self.donner_facture = self.text.get("1.0", END)
            fhandle = open("C:/Users/AZIZ-CISSE/ProjetPython/gestion_platet_facture_resto/facture/"+self.numero_facture.get()+".txt","w")
            fhandle.write(self.donner_facture)
            fhandle.close()
            messagebox.showinfo("Sauvegarder", f"Facture N° : {self.numero_facture.get()} a ete sauvegardée")
        else:
            return
        
    
    #######Fonction pour Rechercher facture#########    
    def recherche(self):
        present = "non"            
        for i in os.listdir("C:/Users/AZIZ-CISSE/ProjetPython/gestion_platet_facture_resto/facture/"):
            if i.split(".")[0]==self.recherche_facture.get():
                fhandle = open("C:/Users/AZIZ-CISSE/ProjetPython/gestion_platet_facture_resto/facture/"+i, "r")
                self.text.delete("1.0", END)
                for d in fhandle:
                    self.text.insert(END, d)
                fhandle.close()
                present = "oui"
                
        if present=="non":
            messagebox.showerror("Erreur", "Numero Facture Invalide")
        
    
    #######Fonction pour Reinitialiser facture#########    
    def reinitialiser(self):
        op = messagebox.askyesno("Reinitialiser", "Voulez-Vous Reinitialiser?")
        if op > 0:
            ######Variable Petit Dejeuner#####
            self.petitdj1.set(0)
            self.petitdj2.set(0)
            self.petitdj3.set(0)
            self.petitdj4.set(0)
            self.petitdj5.set(0)
            self.petitdj6.set(0)
            self.petitdj7.set(0)
            
        ######Variable Repas#####
            self.repas1.set(0)
            self.repas2.set(0)
            self.repas3.set(0)
            self.repas4.set(0)
            self.repas5.set(0)
            self.repas6.set(0)
            self.repas7.set(0)
            
        #######Variable Diner######
            self.diner1.set(0)
            self.diner2.set(0)
            self.diner3.set(0)
            self.diner4.set(0)
            self.diner5.set(0)
            self.diner6.set(0)
            self.diner7.set(0)
            
        #######Somme à Payer#######
            self.prix_total_petit_dej.set("")
            self.prix_total_repas.set("")
            self.prix_total_diner.set("")
            
            self.taxe_petit_dej.set("")
            self.taxe_repas.set("")
            self.taxe_diner.set("")
            
        ########Détails du Client######
            self.nom_client.set("")
            self.tel_client.set("")
            
            self.numero_facture.set("")
            x = random.randint(1000,9999)
            self.numero_facture.set(str(x))
            
            self.recherche_facture.set("")
            
            self.text.delete("1.0", END)
            
            self.afficher_facture()
            
                       
    #####Fonction Quitter#######
    def quitter(self):
        op = messagebox.askyesno("Quitter", "Voulez-Vous Quitter?")
        if op > 0:
            self.root.destroy()
        



root = Tk()
obj = Facture(root)
root.mainloop()