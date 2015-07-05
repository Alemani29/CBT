import time
pinya = 0
pinyapelada = 0
poma = 0
money = 0
ganivet = 0
ganivetma = 0
zona = 1
    
print("---CBT---")
time.sleep(1)
print("Benvingut a CBT, un joc de text.")
time.sleep(2)
print("Hauràs d'escriure de manera simple: acció+objecte")
time.sleep(3)
print("Per el moment et dono les quatre frases bàsiques del joc:")
time.sleep(3)
print("agafar poma")
time.sleep(1)
print("agafar pinya")
time.sleep(1)
print("menjar poma")
time.sleep(1)
print("menjar pinya")
time.sleep(1)
print("També pots veure el que portes a sobre amb: motxilla")
time.sleep(2)
print("En aquests moments ets al bosc")
time.sleep(2)
print("Bona sort!")
time.sleep(1)

while True:
    inp = input(">>")
    
    if inp == "motxilla":
            print("tens", poma, "poma/es")
            print("tens", pinya, "pinya/es")
            print("tens", pinyapelada, "pinya/es pelada/es")
            print("tens", money, "$")

    if inp == "bosc":
        zona = 1

    if inp == "ciutat":
        zona = 2

    if zona == 0:
        print("La pinya estava en mal estat")
        time.sleep(1)
        print("Has mort")
        print("-Game Over-")
        print("Escriu restart per tornar a començar")

    if zona == 1:
        print("Ets al bosc")

        if inp == "agafar poma":
            poma = poma+1
            print("tens", poma, "poma/es")

        if inp == "agafar pinya":
            pinya = pinya+1
            print("tens", pinya, "pinya/es")

        if inp == "agafar pinya pelada":
            print ("Que em prens per imbècil?!")

        if inp == "menjar poma":
            if poma<=0:
                print("No pots tenir pomes negatives!")
            else:
                poma-=1
                print ("tens", poma, "poma/es")

        if inp == "menjar pinya":
            if pinya<=0:
                print("No pots tenir pinyes negatives!")
            else:
                print("Tros de ruc! No has pelat la pinya!")

        if inp == "menjar pinya pelada":
            if pinyapelada<=0:
                print("Tros de ruc! No has pelat la pinya!")
            else:
                zona = 0
             
        if inp == "pelar pinya":
            if pinya<=0:
                print("Com pots pelar una cosa que no tens?!")
            else:
                if ganivetma>=1:
                    pinyapelada = pinyapelada+1
                    pinya = pinya-1
                    print("Has pelat la pinya")
                    print ("tens", pinyapelada, "pinya/es pelada/es")
                else:
                    print("Mare meva! Però en què estàs pensant!")
                    time.sleep(1)
                    print("No has agafat ganivet!")

        if inp == "agafar ganivet":
            if ganivet>=1:
                ganivetma = ganivetma+1
                print("Ara si!")
                time.sleep(1)
                print("Ja pots pelar la pinya")
            else:            
                print("No tens ganivet")
                time.sleep(1)
                print("pots comprar un anant a la botiga")
                print("proba amb >>botiga per veure el preu")

        if inp == "botiga":
            print("Estàs en un bosc, per comprar, vés a la ciutat")
            print("fes servir >>ciutat")

    
    if zona == 2:
        print("Ets a la ciutat")

        if inp == "agafar poma":
            print("D'on agafes les pomes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")

        if inp == "agafar pinya":
            print("D'on agafes les pinyes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")
                    
        if inp == "botiga":
            print("Benvingut a la botiga")
            print("pots comprar amb >>comprar i el que vols comprar")
            print("poma - 1$")
            print("ganivet - 10$")

            if inp == "comprar poma":
                print("Costa 1$")
                if money<=0:
                    print("Com vols pagar?!")
                    print("No tens suficients $!")
                    print("proba a vendre")
                else:
                    poma = poma+1
                    money = money-1
                    print("Aquí tens")
                    print("tens", poma, "poma/es")
                    print("tens", money, "$")
            
            if inp == "comprar ganivet":
                print("Costa 10$")
                if money<=9:
                    print("Com vols pagar?!")
                    print("No tens suficients $!")
                    print("proba a vendre")
                else:
                    ganivet = ganivet+1
                    money = money-10
                    print("Aquí tens")
                    print("tens", ganivet, "ganivet/s")
                    print("tens", money, "$")

            if inp == "vendre poma":
                if poma<=0:
                    print("No pots tenir pomes negatives!")
                else:
                    poma = poma-1
                    money = money+1
                    print("Has venut una poma, guanyes 1$")
                    print ("tens", poma, "poma/es")

            if inp == "vendre pinya":
                if pinya<=0:
                    print("No pots tenir pinyes negatives!")
                else:
                    print("La venda de pinyes és il·legal")
                    zona = 3   
        
    if zona == 3:
        print("Has sigut arrestat, ara ets a la presó")
        ganivet = 0
        poma = 0
        pinya = 0
        money = 0
        pinyapelada = 0
