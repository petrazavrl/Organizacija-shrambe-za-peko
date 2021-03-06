SHRAMBA = "V-shrambi.txt"
RECEPTI = "Recepti"
import os

class Program:

    def __init__(self):
        self.shramba = Shramba()
        self.recepti = []
        
        self.nalozi_shrambo()
        self.nalozi_recepte()
        
    def nalozi_shrambo(self):
        self.shramba.preberi_iz_datoteke()

    def nalozi_recepte(self):
        for datoteka in os.listdir(RECEPTI):
            r = Recept()
            r.preberi_iz_datoteke(RECEPTI + "\\" + datoteka)
            self.recepti.append(r)
            
        return self.recepti
        
    # def nalozi_listek

    
    def nalozi_recepte2(self, recept):
        print('Za recept potrebujemo:')
        with open(recept) as f:
            ali_smo_v_sestavinah = False
            for vrstica in f:
                # print(vrstica)
                if "Sestavine" in vrstica:
                    ali_smo_v_sestavinah = True

                if "Postopek" in vrstica:
                    ali_smo_v_sestavinah = False

                if ali_smo_v_sestavinah and vrstica.strip() != "" and vrstica.strip() != "Sestavine":
                    vse_besede = vrstica.split()
                    kolicina = vse_besede[0]
                    sestavina = ' '.join(vse_besede[1:])
                    print(kolicina, sestavina)

    def nalozi_listek(self, listek):
        with open(listek) as f:
            for vrstica in f:
                print(vrstica)
                vse_besede = vrstica.split()
                kolicina = int(vse_besede[0])
                sestavina = ' '.join(vse_besede[1:])
                self.listek.dodaj(kolicina, sestavina)

class Recept:


    def __init__(self, naslov="", sestavine={}, postopek=""):
        self.naslov = naslov
        self.sestavine = sestavine
        self.postopek = postopek

    def preberi_iz_datoteke(self, datoteka):
        with open(datoteka) as f:
            self.naslov = f.readline()
            ali_smo_v_sestavinah = False
            ali_smo_v_postopku = False
            for vrstica in f:
                # print(vrstica)
                if "Sestavine" in vrstica:
                    ali_smo_v_sestavinah = True

                if "Postopek" in vrstica:
                    ali_smo_v_sestavinah = False
                    ali_smo_v_postopku = True
                    self.postopek = f.readlines(ali_smo_v_postopku)

                if ali_smo_v_sestavinah and vrstica.strip() != "" and vrstica.strip() != "Sestavine":
                    vse_besede = vrstica.split()
                    kolicina = vse_besede[0]
                    sestavina = ' '.join(vse_besede[1:])
                    self.sestavine[sestavina] = kolicina
            

                # TODO: preberi in shrani postopek

class Shramba:
    
    def __init__(self):
        self.slovar_sestavin = {}

    def dodaj(self, kolicina, sestavina):
        self.slovar_sestavin[sestavina] = self.slovar_sestavin.get(sestavina,0) + kolicina


    def shrani_v_datoteko(self, kolicina, sestavina):        
        with open(SHRAMBA, 'a') as f:
            print('{} {}'.format(kolicina, sestavina), file=f)

    def preberi_iz_datoteke(self):
        with open(SHRAMBA) as f:
            for vrstica in f:
                print(vrstica)
                vse_besede = vrstica.split()
                kolicina = int(vse_besede[0])
                sestavina = ' '.join(vse_besede[1:])
                self.dodaj(kolicina, sestavina)


    def odstrani(self, nakupovalni_seznam):
        l = Listek()
        with open(datoteka) as f:
            for vrstica in f:
                vse_besede = vrstica.split()
                kolicina = vse_besede[0]
                sestavina = ' '.join(vse_besede[1:])
                self.slovar_sestavin[sestavina] = self.slovar_sestavin.get(sestavina, 0) - kolicina
        
#s = Shramba()
#s.dodaj("jajca", 4)
#s.dodaj("jajca", 3)
#s.slovar_sestavin["jajca"]

class Listek:

    def __init__(self, kolicina, sestavina):
        self.kolicina = kolicina
        self.sestavina = sestavina

    def dodaj(self, kolicina, sestavina):
        self.kolicina[sestavina] += kolicina

    def pocisti(self, nakupovalni_listek):
        with open(nakupovalni_listek):
            pass

    


#DODAJ RECEPT


                
            
            
def nakupovalni_listek(datoteka):
    print("Kupiti je potrebno:")
    with open(datoteka) as f:
        for vrstica in f:
            vse_besede = vrstica.split()
            kolicina = vse_besede[0]
            sestavina = ' '.join(vse_besede[1:])
            print(kolicina, sestavina)

    
def kar_kupim(nakupovalni_seznam, shramba):
    with open(shramba, 'w') as g:
        with open(nakupovalni_seznam) as f:
            for vrstica in f:
                vse_besede = vrstica.split()
                kolicina = vse_besede[0]
                sestavina = ' '.join(vse_besede[1:])
                print('{} {}'.format(kolicina, sestavina), file=g)
            

    
#def spečem(recept, shramba):
    #iz shrambe odstranim kar je v receptu

#def nakupovalni_seznam(recept, shramba):
    #kar potrebujem pa ni v shrambi
