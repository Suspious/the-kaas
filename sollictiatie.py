#Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiekja
#In bezit van een Diploma MBO-4 ondernemen
#In bezit van een geldig Vrachtwagen rijbewijs
#In bezit van een hoge hoed
#Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
#Is langer dan 150 cm
#Is zwaarder dan 90 kg
#Heeft Certificaat “Overleven met gevaarlijk personeel”
ongeschikt ="u bent ongeschikt voor deze baan"
dierendressuur = int(input("hoeveel jaar heb je ervaring in dierendressuur? (0)is ook mogelijk? " ))
jongleren = int(input("hoeveel jaar heb je ervaring met jongleren? "))
acrobatiek = int(input("hoeveel jaar heb je ervaring in acrobatiek? "))

if dierendressuur > 3 or jongleren > 4 or acrobatiek > 5:
        diploma = input("heb jij een mbo 4 diploma ?\n ")
        if diploma == "nee":
            print(ongeschikt)
        else:
            bezit = input("ben je in een bezit van een vrachtwagenrijbewijs ?\n ")
            if bezit =="nee":
                print(ongeschikt)
            else:
                hoed =input("heeft een hoge hoed?\n  ")
                if hoed =="nee":
                    print(ongeschikt)
                else:
                    haar = input("ben je man of heb je een snor of ben je een vrouw met rood haar?\n ")
                    if haar =="nee":
                        print(ongeschikt)
                    else:
                        lengte = (input("hoe lang ben je? "))
                        if int(lengte) > (150):
                            zwaar = (input("hoeveel weeg je? "))
                            if int(zwaar) > (90):
                                certificaat =input("heb je een certificaat overleven met gevaarlijk personeel?\n ")
                                if certificaat =="ja":
                                    print("je komt overeen,je wordt binnekort gemaild!!!!!")
                                else:
                                    print(ongeschikt)
                            else:
                                print(ongeschikt)
                        else:
                            print(ongeschikt)
else:
    print(ongeschikt)