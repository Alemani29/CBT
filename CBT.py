#Import files
import intro
import time
import random
import pygame
from pygame.locals import *

#Pinya Colada Song
pygame.mixer.init()


#Variables
pinya = 0
pinyapelada = 0
poma = 0
money = 0
ganivet = 0
ganivetma = 0
zona = 1
CBT = False
Barra = False

#Zones
# ?.CBT
# 0.End
# 1.Bosc
# 2.Ciutat
# 3.Botiga
# 4.Cel·la
# 5.Presó
# 6.Taverna


intro.intro()
while True:

    #Basics
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
        print("Ets a la ciutat. Escriu >>mapa per veure els llocs que pots visitar")

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

    if inp == "menjar pinya pelada":
        if pinyapelada<=0:
            print("Que intentes fer?")
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

    #The End
    if zona == 0:
        print("La pinya estava en mal estat")
        time.sleep(2)
        print("Has mort")
        time.sleep (2)
        print("-Game Over-")
        print("Escriu restart per tornar a començar")


    #Bosc
    if zona == 1:
        
        if inp == "agafar poma":
            poma = poma+1
            print("tens", poma, "poma/es")

        if inp == "agafar pinya":
            pinya = pinya+1
            print("tens", pinya, "pinya/es")

        if inp == "agafar pinya pelada":
            print ("Que em prens per imbècil?!")

        if inp == "botiga":
            print("Estàs en un bosc, per comprar, vés a la ciutat")
            print("fes servir >>ciutat")


    #Ciutat
    if zona == 2:
        if inp == "agafar poma":
            print("D'on agafes les pomes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")

        if inp == "agafar pinya":
            print("D'on agafes les pinyes? Ets a la ciutat!")
            print("Has d'anar al bosc amb >>bosc")

        if inp == "mapa":
            print("pots anar a:")
            print(">>botiga")
            print(">>taverna")
            print(">>port")
            print(">>palau")
                    
        if inp == "botiga":
            zona = 3
            print("Benvingut a la botiga")
            print("pots comprar amb >>comprar+objecte")
            print("poma - 1$")
            print("ganivet - 50$")
            print("pinya - ?$")

        if inp == "taverna":
            print("Benvingut a la taverna de l'OGRE CRIDANER")
            time.sleep(1)
            print("Aqui pots trobar tot tipus de viatgers:")
            print("mercaders, trobadors, soldats i exploradors, entre altres")
            time.sleep(2)
            print("Si vas a la barra (>>barra) pots demanar tant menjar com begudes")
            print("Ara ets a la teva taula")
            zona = 6

        if inp == "port":
            print("Aquesta zona està en obres torna en un futur per poder-la visitar")

        if inp == "palau":
            print("Aquesta zona està en obres torna en un futur per poder-la visitar")

    
    #Botiga
    if zona == 3:
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

        if inp == "comprar pinya":
            if money<=0:
                print("Com vols pagar?!")
                print("No tens suficients $!")
                print("proba a vendre amb >>vendre+objecte")
            else:
                print("Però es pot saber que fas?!")
                print("Es que no saps el problema que hi ha amb les pinyes?!!!")
            
        if inp == "comprar ganivet":
            print("Costa 50$")
            if money<=49:
                print("Com vols pagar?!")
                print("No tens suficients $!")
                print("proba a vendre")
            else:
                ganivet = ganivet+1
                money = money-50
                print("Aquí tens")
                print("tens", ganivet, "ganivet/s")
                print("tens", money, "$")
        
        if inp == "vendre poma":
            if poma<=0:
                print("No pots tenir pomes negatives!")
                print("Pots agafar pomes al bosc")
            else:
                poma = poma-1
                money = money+1
                print("Has venut una poma, guanyes 1$")
                print ("tens", poma, "poma/es")
                print("tens", money, "$")

        if inp == "vendre pinya":
            if pinya<=0:
                print("No pots tenir pinyes negatives!")
                print("Pots agafar pinyes al bosc")
            else:
                if random.randint(0,100) <1:
                    pinya =pinya-1
                    money = money+100
                    print("Has venut una pinya, tot i que és il·legal, compte no t'atrapin. Guanyes 100$")
                    print ("tens", pinya, "pinya/es")
                    print("tens", money, "$")
                    
                else:
                    print("La venda de pinyes és il·legal")
                    time.sleep(2)
                    zona = 4
                    ganivet = 0
                    poma = 0
                    pinya = 0
                    money = 0
                    pinyapelada = 0
                    print("Has estat arrestat, ara ets a la presó")
                    print("Tots els teus objectes han estat requisats")
                    time.sleep(1)
                    print("Tot i així la porta de la cel·la sembla bastant antiga")


    #Cel·la      
    if zona == 4:
        ganivet = 0
        poma = 0
        pinya = 0
        money = 0
        pinyapelada = 0

        if inp == "obrir porta":
            print("La porta és antiga, però encara aguanta")
            print("Potser si fas molta força pots trencar la porta")

        if inp == "trencar porta":
            print("La porta ha cedit! Has aconseguit escapar!")
            time.sleep(2)
            print("Ets a una gran sala on hi ha alguns cofres")
            print("També hi ha una gran porta")
            zona = 5


    #Presó
    if zona == 5:

        if inp == "obrir cofre":
            if random.randint(0,3) <1:
                if random.randint(0,5) <1:
                    if random.randint(0,10) <1:
                        print("Un ganivet!")
                    else:
                        print("Has trobat 10 pomes i 10$")
                        poma = poma+10
                        money = money+10
                else:
                    print("Has trobat 5 pomes")
                    poma = poma+5                        
            else:
                print("No hi ha res")

        if inp == "obrir porta":
            print("Ets a la ciutat")
            zona = 2


    #Taverna
    if zona == 6:

        if inp == "barra":
            print("Ets a la barra. Pots prendre:")
            time.sleep(1)
            print(">>Aigua")
            print(">>Cervesa")
            print(">>Pinya Colada")
            time.sleep(2)
            print("Que vols demanar?")
            Barra = True

        if Barra == True:

            if inp == "aigua":
                print("Costa 5$")
                if money<=4:
                    print("Com vols pagar?!")
                    print("No tens suficients $!")
                    print("proba a vendre a la botiga")
                else:
                    money = money-5
                    print("Aquí tens")
                    time.sleep(1)
                    print("glup")
                    time.sleep(1)
                    print("glup")
                    time.sleep(2)
                    print("Es nota que tenies sed")
                    time.sleep(1)
                    print("Has tornat a la teva taula")
                    Barra = False
                        
            if inp == "pinya colada":
                pygame.mixer.music.load("songs\pinyacolada.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.clock()
                    
                print("Has pres una Pinya Colada! No cal que paguis, convida la casa")
                time.sleep(2)
                print("Has tornat a la teva taula")
                Barra = False
                


     #CBT
    if CBT == False:
        
        if random.randint(0,1000000) <1:
            time.sleep(2)
            print("Ha aparegut un CBT! Una Cabra Boja Tridimensional!!!")
            time.sleep(1)
            print("Això és un event únic!")
            time.sleep(1)
            print("Ràpid atrapa-la abans que escapi! Fes servir >>atrapar CBT")
            CBT = True

    #Atrapa CBT
    if CBT == True:

        if inp == "atrapar CBT":
            print("Però a que jugues?!")
            time.sleep(1)
            print("És un CBT serà molt més difícil que escriure atrapar CBT!")
            time.sleep(1)
            print("Proba a agafar una pakeball!")
            time.sleep(1)
            print("Sí! El CBT és un Pakemun interdimensional")

        if inp == "agafar pakeball":
            print("Evidentment tens una pakeball! Has atarpat el CBT")
            time.sleep(4)
            print("Era sarcasme")
            time.sleep(1)
            print("El CBT ha creat un vòrtex interdimensional")
            time.sleep(2)
            print("El CBT t'ha teletransportat al bosc. Tens sort de no haver mort")
            CBT = False
            zona = 1
            
        
