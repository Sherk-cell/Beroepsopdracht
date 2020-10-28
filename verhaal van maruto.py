import random
print("Dit is het verhaal van maruto (verzonnen naam/persoon)\nhij was een succesvolle man hij was een doctor een mooie vrouw een groot huis en heel aardig\nOp de dag dat hij terug van werk kwam vielen de bommen en toen hij uit eindelijk thuis kwam was zijn vrouw, kinderen, buurman en zijn dochter dood. Dit was het moment dat hij ging vluchten\n")
print("hij leerde een smokkelaar kennen van een oude vriend van werk. Hij was duur maar is verzekerd in zijn zaak,\nvoordat hij de deal deed om na te denken over zijn keuzen kwam er een tweede smokkelaar die goedkoper was maar niet verzekerd.")
smokkelaarvraag = input("Kies de smokkelaar\nA. de duurdere\nB. de goedkoppere.\n")
if smokkelaarvraag == "B":
    print("Je gaf je geld aan de goedkope smokkelaar. Hij vraagt dat je hem 2 dagen geeft om alles voor jouw klaar tezetten\n\nTwee dagen later\n\nJe hebt geen bericht meer van hem gekregen hij heeft je achtergelaten en je hebt geen geld meer.")
elif smokkelaarvraag == "A":
    print("Je gaf je geld aan de dure smokkelaar. Hij vraagt voor 5 dagen om alles klaar voor jouw tezetten.\n\n5 dagen later\n\nHij stuurt jouw een bericht van dat alles klaar is en je kan meekomen in een busje.")
    print("Je stapte in een busje van de wehkamp. Je zit 3 dagen lang in een busje je gaat door verschillende landen je ziet delen van Turkije, Oostenrijk en van Duitsland. maar tussen Duitsland en Nederland wordt je staan gehouden omdat ze hoorden je in de achterkant van het busje.")
    kledingsvraag = input("De smokkelaar zei dat je een outfit moest aantrekkenn en snel je leest wat erop staat welke kies je\nA. H&M\nB. Militair outfit\nC. Doctor outfit\nD. Wehkamp outfit\n")
    if kledingsvraag == "A":
        print("Je trekte de H&M outfit aan. De border security keek je aan met killende ogen. Je hebt een H&M outfit aan terwijl je in een wehkamp bus zit. De politie is gebeld je bent opgepakt smokkelen\nPRISON ENDING.")
    elif kledingsvraag == "B":
        print("Je trekte de de Soldaat uniform aan. De border security zag jouw niet goed. Hij ziet dat je in het leger zit, hij keek naar jouw van waar je vandaan kwam en zag dat je van Syrië komt. Hij denkt dat je een terrorist bent, hij schiet je gaat dood\nDEAD END")
    elif kledingsvraag == "C":
        print("Je trekte de Doctor outfit aan. De border security zag jouw zitten als een doctor. Hij denkt je bent een drugsdealer, je wordt aangehouden en je wordt onderzoekt als je drugs bij je hebt. Je wordt achtergelaten door de smokkelaar omdat hij wel drugs heeft hij zet de schuldt op jouw en rijdt weg. Hij wordt later ook opgepakt\nPRISON ENDING")
    elif kledingsvraag == "D":
        print("Je trekt de Wehkamp outfit aan. De border security zag jouw zitten in de achter kant van de bus. Hij laat jullie door aangezien de smokkelaar zei dat je je niet goed voelden en dus rustig ging liggen op de kleding.")
        print("Je komt uiteindelijk in Nederland het was Nederland een moeilijke en lange trip maar hij is er eindelijk de smokkelaar geeft hem €5000,- euro een paspoort, een id en een laat hem daar op straat achter")
        print("Je gaat nederlands proberen te leren je gaat naar school je zit 1 jaar op school en je gaat je examens doen")
        nederlandsevraag = input("de vraag is wat zet je na een zin:\nA. een punt\nB. een komma\nC. Niks\n")
        if nederlandsevraag == "A":
            print("Je hebt je nederlandse test gehaald")
            print("Sinds je je Nederlandse test heb gehaald ging hij een baan zoeken hij wou eerst voor doctor gaan maar realiseerde dat hij niet dat goed is in Nederlands\nDus hij ging naar iets zoeken dat hij kon doen om geld tekrijgen.")
            baan = input("Hij zat natedenken over zijn keuzes hij dacht aan deze baanen\nA. Werken bij een supermarkt\nB. Diefstal\nC. Gokken in een casino\nD. Taxichauffeur\nE. Soldaat\n vul in: ")
            if baan == "A":
                print("Hij koos om te gaan werken in een supermarkt je ging bij de alber heijn werken als schoonmaker. Je deedt het heel goed alleen je werdt soms gepest door je medewerkers door je slechte Nederlands.")
                print("5 JAAR LATER")
                print("Na 5 jaar werken in de appie is hij gepromoveerd naar teamleider en hij is best succsesvol \nGOOD ENDING")
            elif baan == "B":
                 print("je hebt er lang en goed erover nagedacht aangezien je aan je moraal zat tedenken maar uiteindelijk koos je om het toch tedoen je ging je aansluiten bij een paar andere vluchtelingen die je kende bij jouw school en jullie begonnen teplannen om een supermarkt te overvallen.")
                 print("3 MAANDEN LATER")
                 print("na 3 maanden heb je een planning gemaakt om een overvall teplegen")
                 r = random.randrange(1, 2)
                 if r == 2:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie maar je was allang weg")
                     print("\n\n5JAAR LATER\n\n")
                     print("Je zit rustig in je huis en opeens valt de politie in je probeert je zelf te verdedigen maar de recheter doet zijn finale uitspraak,je krijgt 3 jaar\nPRISON ENDING")
                 elif r == 1:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie de politie was in de buurt dus ze hebben je makkelijk gepakt\nPRISON ENDING")                                  
            elif baan == "C":
                print("aangezien je geloofig bent mag je niet gokken maar je had weinig tot geen keuze dus je ging naaar Holland casino en je besloot om te gaan gokken.")
                r1 = random.randrange(1, 2)
                if r1 == 1:
                    print("je gokte all je geld op zwart de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart je wint €50.000,-\n LUCKY ENDING")
                elif r1 == 2:
                    print("je gokte all je geld op rood de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart en je verloor al je geld. Je begint te huilen all jouw geld weg je loopt naar buiten en realiseert je bent blut\nZWERVER ENDING")
            elif baan == "D":
                print("je besloot om een taxichaffeur teworden want in syrië maakte die mensen veel geld dus hij vondt het een goede investering\nVERLOREN POTENTIEEL")
            elif baan == "E":
                print("Je voelde je moedig en je dacht eraan om soldaat teworden en je land terug tekrijgen")
                print("\n\n2 JAAR LATER\n\n")
                print("Na 2 jaar elke dag bootcamp werdt je gestuurt naar Syrië om terug tevechten en je land terug tekrijgen")
                r2 = random.randrange(1, 2)
                if r2 == 1:
                    print("Je vechten en bleef vechten en uiteindelijk won je de oorlog Syrië is vrij je kan nu terug naar je famillie in Syrië\nHERO ENDING")
                if r2 == 2:
                    print("Je vechten en bleef vechten maar opeens deden de syrië's tegenstanders een verrasings aanval en ze schoten iedereen neer al je collegas dood en je gaat nooit meer je famillie zien\nA HERO'S DEATH")  

            else: 
                print("Ik vroeg om een echte antwoord(als je a b c of d heb ingevulled doe het met een hoofdletter)")

        elif nederlandsevraag == "B":
            print("Je faalde de nederlandse test je doet er nog een jaar over")
            print("Sinds je je Nederlandse test heb gehaald ging hij een baan zoeken hij wou eerst voor doctor gaan maar realiseerde dat hij niet dat goed is in Nederlands\nDus hij ging naar iets zoeken dat hij kon doen om geld tekrijgen.")
            baan = input("Hij zat natedenken over zijn keuzes hij dacht aan deze baanen\nA. Werken bij een supermarkt\nB. Diefstal\nC. Gokken in een casino\nD. Taxichauffeur\nE. Soldaat\n vul in: ")
            if baan == "A":
                print("Hij koos om te gaan werken in een supermarkt je ging bij de alber heijn werken als schoonmaker. Je deedt het heel goed alleen je werdt soms gepest door je medewerkers door je slechte Nederlands.")
                print("5 JAAR LATER")
                print("Na 5 jaar werken in de appie is hij gepromoveerd naar teamleider en hij is best succsesvol \nGOOD ENDING")
            elif baan == "B":
                 print("je hebt er lang en goed erover nagedacht aangezien je aan je moraal zat tedenken maar uiteindelijk koos je om het toch tedoen je ging je aansluiten bij een paar andere vluchtelingen die je kende bij jouw school en jullie begonnen teplannen om een supermarkt te overvallen.")
                 print("3 MAANDEN LATER")
                 print("na 3 maanden heb je een planning gemaakt om een overvall teplegen")
                 r = random.randrange(1, 2)
                 if r == 2:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie maar je was allang weg")
                     print("\n\n5JAAR LATER\n\n")
                     print("Je zit rustig in je huis en opeens valt de politie in je probeert je zelf te verdedigen maar de recheter doet zijn finale uitspraak,je krijgt 3 jaar\nPRISON ENDING")
                 elif r == 1:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie de politie was in de buurt dus ze hebben je makkelijk gepakt\nPRISON ENDING")                                  
            elif baan == "C":
                print("aangezien je geloofig bent mag je niet gokken maar je had weinig tot geen keuze dus je ging naaar Holland casino en je besloot om te gaan gokken.")
                r1 = random.randrange(1, 2)
                if r1 == 1:
                    print("je gokte all je geld op zwart de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart je wint €50.000,-\n LUCKY ENDING")
                elif r1 == 2:
                    print("je gokte all je geld op rood de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart en je verloor al je geld. Je begint te huilen all jouw geld weg je loopt naar buiten en realiseert je bent blut\nZWERVER ENDING")
            elif baan == "D":
                print("je besloot om een taxichaffeur teworden want in syrië maakte die mensen veel geld dus hij vondt het een goede investering\nVERLOREN POTENTIEEL")
            elif baan == "E":
                print("Je voelde je moedig en je dacht eraan om soldaat teworden en je land terug tekrijgen")
                print("\n\n2 JAAR LATER\n\n")
                print("Na 2 jaar elke dag bootcamp werdt je gestuurt naar Syrië om terug tevechten en je land terug tekrijgen")
                r2 = random.randrange(1, 2)
                if r2 == 1:
                    print("Je vechten en bleef vechten en uiteindelijk won je de oorlog Syrië is vrij je kan nu terug naar je famillie in Syrië\nHERO ENDING")
                if r2 == 2:
                    print("Je vechten en bleef vechten maar opeens deden de syrië's tegenstanders een verrasings aanval en ze schoten iedereen neer al je collegas dood en je gaat nooit meer je famillie zien\nA HERO'S DEATH")  

            else: 
                print("Ik vroeg om een echte antwoord(als je a b c of d heb ingevulled doe het met een hoofdletter)")

        elif nederlandsevraag == "C":
            print("Je faalde de nederlandse test je doet er nog een jaar over")
            print("Sinds je je Nederlandse test heb gehaald ging hij een baan zoeken hij wou eerst voor doctor gaan maar realiseerde dat hij niet dat goed is in Nederlands\nDus hij ging naar iets zoeken dat hij kon doen om geld tekrijgen.")
            baan = input("Hij zat natedenken over zijn keuzes hij dacht aan deze baanen\nA. Werken bij een supermarkt\nB. Diefstal\nC. Gokken in een casino\nD. Taxichauffeur\nE. Soldaat\n vul in: ")
            if baan == "A":
                print("Hij koos om te gaan werken in een supermarkt je ging bij de alber heijn werken als schoonmaker. Je deedt het heel goed alleen je werdt soms gepest door je medewerkers door je slechte Nederlands.")
                print("5 JAAR LATER")
                print("Na 5 jaar werken in de appie is hij gepromoveerd naar teamleider en hij is best succsesvol \nGOOD ENDING")
            elif baan == "B":
                 print("je hebt er lang en goed erover nagedacht aangezien je aan je moraal zat tedenken maar uiteindelijk koos je om het toch tedoen je ging je aansluiten bij een paar andere vluchtelingen die je kende bij jouw school en jullie begonnen teplannen om een supermarkt te overvallen.")
                 print("3 MAANDEN LATER")
                 print("na 3 maanden heb je een planning gemaakt om een overvall teplegen")
                 r = random.randrange(1, 2)
                 if r == 2:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie maar je was allang weg")
                     print("\n\n5JAAR LATER\n\n")
                     print("Je zit rustig in je huis en opeens valt de politie in je probeert je zelf te verdedigen maar de recheter doet zijn finale uitspraak,je krijgt 3 jaar\nPRISON ENDING")
                 elif r == 1:
                     print("Je komt met 2 wapens in de gebouw toen zei hij 'geef me all jullie geld of ik maak jullie dood' ze gaven al hun geld en je schiet de camera kapot. Toen je ongeveer al het geld had pakte je de auto en reedt weg hun belden de politie de politie was in de buurt dus ze hebben je makkelijk gepakt\nPRISON ENDING")                                  
            elif baan == "C":
                print("aangezien je geloofig bent mag je niet gokken maar je had weinig tot geen keuze dus je ging naaar Holland casino en je besloot om te gaan gokken.")
                r1 = random.randrange(1, 2)
                if r1 == 1:
                    print("je gokte all je geld op zwart de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart je wint €50.000,-\n LUCKY ENDING")
                elif r1 == 2:
                    print("je gokte all je geld op rood de ball bleef rollen en rollen, je werd er bijna ziek door zo spannend. De bal stopt en het is op zwart en je verloor al je geld. Je begint te huilen all jouw geld weg je loopt naar buiten en realiseert je bent blut\nZWERVER ENDING")
            elif baan == "D":
                print("je besloot om een taxichaffeur teworden want in syrië maakte die mensen veel geld dus hij vondt het een goede investering\nVERLOREN POTENTIEEL")
            elif baan == "E":
                print("Je voelde je moedig en je dacht eraan om soldaat teworden en je land terug tekrijgen")
                print("\n\n2 JAAR LATER\n\n")
                print("Na 2 jaar elke dag bootcamp werdt je gestuurt naar Syrië om terug tevechten en je land terug tekrijgen")
                r2 = random.randrange(1, 2)
                if r2 == 1:
                    print("Je vechten en bleef vechten en uiteindelijk won je de oorlog Syrië is vrij je kan nu terug naar je famillie in Syrië\nHERO ENDING")
                if r2 == 2:
                    print("Je vechten en bleef vechten maar opeens deden de syrië's tegenstanders een verrasings aanval en ze schoten iedereen neer al je collegas dood en je gaat nooit meer je famillie zien\nA HERO'S DEATH")  

            else: 
                print("Ik vroeg om een echte antwoord(als je a b c of d heb ingevulled doe het met een hoofdletter)")
        else:
            print("Ik vroeg om een echte antwoord(als je a of b of c heb ingevulled doe het met een hoofdletter)")
    else: 
        print("Ik vroeg om een echte antwoord(als je a b c of d heb ingevulled doe het met een hoofdletter)")
else:
    print("Ik vroeg om een echte antwoord(als je a of b heb ingevulled doe het met een hoofdletter)")
