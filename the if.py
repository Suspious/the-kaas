kaas_duur = "emmerthaler"
kaas_nietduur = "leerdammer"
steenja = "pammigiano regiano"
steennee = "goudsekaas"
korstja ="camembert"
korstnee ="mozzarella"
korst2ja ="blue de rochbaron"
korst2nee ="foume d'ambert"

geel = input("is de kaas geel? ")
if geel == ("ja"):
        gaten = input("zitten er gaten in? ")
        if gaten == "ja":
                duur = input("is de kaas belachelijk duur? ")
                if duur =="ja":
                        print(kaas_duur)
                else:
                        print(kaas_nietduur)
        else:
                steen = input("is de kaas zo hard als steen")
                if steen =="ja":
                        print(steenja)
                else:
                        print(steennee)
else: 
        schimmel = input("heeft de kaas blauwe schimmel? ")
        if schimmel == "ja":
                korst =input("heeft de kaas een korst? ")
                if korst =="ja":
                        print(korst2ja)
                else:
                        print(korst2nee)
        else:
                korst2 =("heeft de kaas een korst")
                if korst2 == ("ja"):
                        print(korstja)
                else:
                        print(korstnee)
                
        