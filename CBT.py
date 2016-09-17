#import files
import intro
import time

#variables
pinya = 0
pinyapelada = 0
poma = 0
money = 0
ganivet = 0
ganivetma = 0
zona = 1

intro.intro()
while True:    
    inp = input(">>")

    if inp == "motxilla":
        print ("tens", poma, "poma/es")
        print ("tens", pinya, "pinya/es")
        print ("tens", pinyapelada, "pinya/es pelada/es")
        print ("tens", money, "$")

    if inp == "bosc":
        zona = 1
        print("Ets al bosc. Aquí pots collir fruita")

    if inp == "ciutat":
        zona = 2
        print("Ets a la ciutat. Aquí pots accedir a la botiga")

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
            if pinyapelada<=0:
                print("Tros de ruc! No has pelat la pinya!")
            else:
                zona = 0


    if inp == "restart":
        pinya = 0
        pinyapelada = 0
        poma = 0
        money = 0
        ganivet = 0
        ganivetma = 0
        zona = 1
    
        intro.intro()


    if zona == 0:
        print("La pinya estava en mal estat")
        time.sleep(2)
        print("Has mort")
        print("-Game Over-")
        print("Escriu restart per tornar a començar")


    if zona == 1:
        if inp == "agafar poma":
            poma = poma+1
            print("tens", poma, "poma/es")

        if inp == "agafar pinya":
            pinya = pinya+1
            print("tens", pinya, "pinya/es")

        if inp == "agafar pinya pelada":
            print ("Que em prens per imbècil?!")            
          
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
        if inp == "agafar poma":
            print("D'on agafes les pomes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")

        if inp == "agafar pinya":
            print("D'on agafes les pinyes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")
                    
        if inp == "botiga":
            zona = 4
            print("Benvingut a la botiga")
            print("pots comprar amb >>comprar+objecte")
            print("poma - 1$")
            print("ganivet - 10$")
            print("pinya - ?$")               

        
    if zona == 3:
        ganivet = 0
        poma = 0
        pinya = 0
        money = 0
        pinyapelada = 0



    if zona == 4:
        if inp == "comprar poma":
            print("Costa 1$")
            if money<=0:
                print("Com vols pagar?!")
                print("No tens suficients $!")
                print("proba a vendre amb >>vendre+objecte")
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
                print("Pots agafar pomes al bosc")
                print("per anar al bosc utilitza >>bosc")
            else:
                poma = poma-1
                money = money+1
                print("Has venut una poma, guanyes 1$")
                print ("tens", poma, "poma/es")

        if inp == "comprar pinya":
            if money<=0:
                print("Com vols pagar?!")
                print("No tens suficients $!")
                print("proba a vendre amb >>vendre+objecte")
            else:
                print("La compra de pinyes és il·legal")
                time.sleep(2)
                zona = 3
                ganivet = 0
                poma = 0
                pinya = 0
                money = 0
                pinyapelada = 0
                print("Has estat arrestat, ara ets a la presó")
                print("Tots els teus objectes han estat requisats")

        if inp == "vendre pinya":
            if pinya<=0:
                print("No pots tenir pinyes negatives!")
                print("Pots agafar pinyes al bosc")
                print("per anar al bosc utilitza >>bosc")
            else:
                print("La venda de pinyes és il·legal")
                time.sleep(2)
                zona = 3
                ganivet = 0
                poma = 0
                pinya = 0
                money = 0
                pinyapelada = 0
                print("Has estat arrestat, ara ets a la presó")
                print("Tots els teus objectes han estat requisats")
        
