print("Hello you!, ik ben Byron")
username = input("Wie ben jij ")
print("Hello " + username)
print("ik ben een nieuwkomer op het mediacollege Amsterdam\n door een aantal vragen over mij te beantwoorden leer je mij beter kennen.")
antwoord = input("voor ik naar het MBO mediacollege Amsterdam kwam, zat ik op het \n A. Cburg college \n B. Mediacollege dintelstraat \n C. Obs \nWat is het correcte antwoord? a, b of c????\n ")
A = antwoord
if antwoord == "B" or antwoord == "C":
	print("fout") 
else:
    print("Goedzo ik zat op cburg")
    print("Oke volgende vraag")
    antwoord2 = input ("wat is mijn favoriete kleur\nA. Blauw\nB. Geel\nC. Rood\n ")
    if antwoord2 == "B":
        print("Goedzo")
        antwoord3 = input ("Wat is mijn favoriete anime \n A. Sword art online \n.B Rent-a-girlfriend \n.C Jojo's bizzare adventure \n")
        C = antwoord3
        if antwoord3 == "C":
                print("goedzo mijn favorieten anime is jojo's wow je veelt over mij jij stalker")
        else:
            print("fout")
    else:
        print("Fout")
        
