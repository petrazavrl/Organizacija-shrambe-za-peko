def sestavine_za_recept(recept):
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
                #print(kolicina)
                #print(sestavina)
                for kolicina, sestavina in f:
                    print('Potrebujete {} {}'.format(kolicina, sestavina))

def kar_kupim(nakupovalni_listek, shramba):
    shramba.append(nakupovalni_listek)

    
#def spečem(recept, shramba):
    #iz shrambe odstranim kar je v receptu

#def nakupovalni_seznam(recept, shramba):
    #kar potrebujem pa ni v shrambi
#def shramba(datoteka): 
#    with open(datoteka) as f:
#        for vrstica in f:
#            
#            for kolicina, sestavina in f:
