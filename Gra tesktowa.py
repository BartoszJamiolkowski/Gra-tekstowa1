import random
def gra():
    lista = ["samuraj", "wojownik"]
    
    print("         O                     O")
    print("        /|\\                   /|\\")
    print("       / | \\                 / | \\")
    print("        | |                   | |")
    print("       /   \\                 /   \\")
    print("      |     |               |     |")
    print("     /|_____|\\             /|_____|\\")
    print("    /         \\           /         \\")
    print("   |           |         |           |")
    print("  /|           |\\       /|           |\\")
    print(" /_|___________|_\\     /_|___________|_\\")
    print("   |   |   |   |         |   |   |   |")
    print("   |   |   |   |         |   |   |   |")
    print("   |   |   |   |         |   |   |   |")
    print("  /    |   |    \\       /    |   |    \\")
    print(" /_____|___|_____\\     /_____|___|_____\\")
    print("       /   \\                 /   \\")
    print("      |     |               |     |")
    print("     /       \\             /       \\")
    print("    |         |           |         |")
    print("    |  MIECZ  |           |  TARCZA |")
    print(" ")
    print("      Samuraj                Wojownik")
    print("")
    
    
    print("Witaj w grze tekstowej!")
    print("Twoim zadaniem będzie udzielanie odpowiedzi tak/nie.")
    print("Miasto Denver od stuleci symbolizuje spokój i dobrobyt.")
    print("Od pewnego czasu miasto jest w wielkim niebezpieczeństwie.")
    print("Tajemniczy i dotąd nieznany Klan Umb chce zatruć miasto i je okraść. Jesteś wybawcą miasta Denver.")
   
    print("Wybierz klasę swojej postaci:", ", ".join(lista))
    while True:
        klasa_postaci = input("Wpisz nazwę klasy: ").lower()
        if klasa_postaci in lista:
            print(f"Wybrałeś klasę: {klasa_postaci.capitalize()}. Powodzenia w grze!")
            break  
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


    def zla_odpowiedz():
        while True:
            odpowiedz = input("Niepoprawna odpowiedź. Odpowiedz tak/nie: ").strip().lower()
            if odpowiedz in ["tak", "nie"]:
                return odpowiedz
   
    def zla_wybror():
        while True:
            odpowiedz=input("Niepoprawna odpowiedź. Odpowiedz snajperzy/strażnicy:").strip().lower()
            if odpowiedz in ["snajperzy","strażnicy"]:
                return odpowiedz


    def samuraj():
        print("Wchodzisz do wioski przed miastem Denver, która została zaatakowana przez Klan Umb.")
        print("Mieszkańcy proszą Cię o pomoc w odnalezieniu porwanych dzieci.Czy im pomożesz?")
        odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
        while odpowiedz not in ["tak","nie"]:
            odpowiedz=zla_odpowiedz()
        if odpowiedz=="tak":
            print("Podążasz za tropami do lasu. Udaje Ci się uratować dzieci, ale zostałeś ranny.")
            print("Mieszkańcy oferują Ci pomoc w regeneracji zdrowia. Czy przyjmujesz ich ofertę?")
            odpowiedz = input("Odpowiedz tak/nie: ").strip().lower()
            while odpowiedz not in ["tak", "nie"]:
                odpowiedz = zla_odpowiedz()
            if odpowiedz=="tak":
                print("Regenerujesz siły i wyruszasz w dalszą podróż.")
                print("Znajdujesz tajemniczy tunel prowadzący do bazy Klanu Umb. Czy wejdziesz?")
                odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                while odpowiedz not in ["tak", "nie"]:
                    odpowiedz = zla_odpowiedz()
                if odpowiedz=="tak":
                    print("Docierasz do bazy wroga, ale zostajesz pokonany w pojedynku. Giniesz!")
                    zakonczenie()
                   
                elif odpowiedz=="nie":
                    print("Decydujesz się wrócić do miasta, ale jest już za późno. Denver zostaje zniszczone.")
                    zakonczenie()
   
            elif odpowiedz=="nie":
                print("Pomijasz regenerację i ruszasz w dalszą drogę, ale Twoje obrażenia okazują się zbyt poważne.")
                print("Upadasz po drodze, a Klan Umb zdobywa miasto.Giniesz!")
                zakonczenie()
               


        elif odpowiedz=="nie":
            print("Nie pomagasz mieszkańcom wioski. Wyruszasz sam do miasta.")
            print("Przed wejściem do miasta widzisz strażników. Kryjesz się?")
            odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
            while odpowiedz not in ["tak", "nie"]:
                odpowiedz=zla_odpowiedz()
            if odpowiedz=="tak":
                print("Ukrywasz się w piwnicy.Gdzie spotykasz tajemniczego starca, który oferuje ci pomoc. ")
                print("Starzec zna tajemnicze przejście do miasta. Zaufasz mu?")
                odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                while odpowiedz not in ["tak", "nie"]:
                    odpowiedz=zla_odpowiedz()
                if odpowiedz=="tak":
                    print("Starzec prowadzi Cię przez tajemnicze przejście do miasta.")
                    print("Docierasz bezpiecznie do centrum Denver i odkrywasz siedzibę Klanu Umb.")
                    print("Czy chcesz zaatakować siedzibę wroga?")
                    odpowiedz=input("Opdowiedz tak/nie:").strip().lower()
                    while odpowiedz not in ["tak","nie"]:
                        odpowiedz=zla_odpowiedz()
                    if odpowiedz=="tak":
                        print("Decydujesz się zaatakować siedzibę Klanu Umb frontalnie.")
                        print("Wchodzisz do środka, ale strażnicy zauważają Cię i rozpoczyna się walka.")
                        print("Udaje Ci się pokonać pierwszą grupę strażników, ale zostajesz ranny.")
                        print("Docierasz do głównej sali, gdzie spotykasz lidera Klanu Umb.")
                        print("Czy chcesz od razu zaatakować lidera?")
                        odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                        while odpowiedz not in ["tak","nie"]:
                            odpowiedz=zla_odpowiedz()
                        if odpowiedz=="tak":
                            print("Postanawiasz zaatakować lidera, zabijasz go i sam giniesz.")
                            print("Zostajesz bohaterem Denver!")
                            zakonczenie()
                        elif odpowiedz=="nie":
                            print("Po długi godzinach rozmów dochodzi do porzumienia.")
                            print("Klan Umb opuszcza miasto,mieszkańcy zaczynają żyć spokojnie w mieście.")
                            zakonczenie()
                    elif odpowiedz=="nie":
                        print("Decydujesz się nie atakować siedziby wroga. Wracasz do miasta, ale tracisz okazję, by pokonać Klan Umb.")
                        print("Denver zostaje zniszczone. Gra kończy się porażką.")
                        zakonczenie()
                elif odpowiedz=="nie":
                    print("Nie ufasz starcu. Postanawiasz zabić go.")
                    print("Przez krzyki starca ujawniasz swoje miejsce.")
                    print("Strażnicy Cię znajdują i zabiają. Denver zostaje przejęte przez Klan Umb.")
                    zakonczenie()
            elif odpowiedz=="nie":
                print("Spotykasz swojego kolegę Talona jako strażnika Umb.")
                print("Udaję Ci się zdobyć informację o miejscu spotania klanu Umb.")
                print("Udajesz się na nie?")
                odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                while odpowiedz not in ["tak","nie"]:
                    odpowiedz=zla_odpowiedz()
                if odpowiedz=="tak":
                    print("Podążasz na miejsce spotkania Klanu Umb, kryjąc się w cieniu.")
                    print("Widząc zgromenie wroga, postanawiasz podsłuchać ich rozmowy.")
                    print("Dowiadujesz się, że planują zaatakować miasto o świcie.")
                    print("Czy chcesz wrócić do miasta, by ostrzec mieszkańców?")
                    odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                    while odpowiedz not in ["tak","nie"]:
                        odpowiedz=zla_odpowiedz()
                    if odpowiedz=="tak":
                        print("Wracasz do miasta, by ostrzec mieszkańców.")
                        print("Razem z lokalną strażą przygotowujecie się do obrony.")
                        print("Udaje się odeprzeć atak Klanu Umb, a Ty zostajesz bohaterem Denver!")  
                        zakonczenie()
                    elif odpowiedz=="nie":
                        print("Nie ostrzegasz mieszkańców i miasto zostaje zaskoczone przez wroga.")    
                        print("Denver zostaje zniszczone.")
                        zakonczenie()
                elif odpowiedz=="nie":
                    print("Postanawiasz zignorować spotkanie Klanu Umb. Wracasz do miasta, ale nie wiesz o planowanym ataku.")
                    print("Niestety, Denver zostaje zaatakowane i zniszczone.")
                    zakonczenie()
   
    def wojownik():
        postac=["wieśniacy","inteligenci"]
        print("Przechadzając się po ruinach starego zamku w Denver. Napotykasz lidera klanu Umb.")
        print("Świątynia jest wypełniona pułapkami.Przywołujesz pomoc?")
        odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
        while odpowiedz not in ["tak","nie"]:
            odpowiedz=zla_odpowiedz()
        if odpowiedz=="tak":
            wylosowana_postac=random.choice(postac)
            print(f"Postanawiasz wziąć ze sobą {wylosowana_postac}. Razem wyruszacie na niebezpieczną wyprawę przez świątnię.")
            print("W pewnym momencie znajdujecie ukrytą dźwignię. Decydujesz się ją uruchomić?")
            odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
            while odpowiedz not in ["tak","nie"]:
                odpowiedz=zla_odpowiedz()
            if odpowiedz=="tak":
                print("Uruchamiacie wspólnie dźwignię lecz okazuję się to być pułapka, która wypełnia całą salę wodą.")
                print("Udaje wam się uciec przed wodą.Docieracie do następnej komnaty, w której stoją snajperzy z trucizną.")
                if wylosowana_postac=="wieśniacy":
                    print("Wieśniacy wpadają w szał. Przyciąga to uwagę snajperów.")
                    print("Udaję Ci się pokonać snajperów z twoją nadludzką mocą lecz tracisz większość zapasów i towarzyszy.")
                    print("Docierasz do głównej komanty wraz z dwoma wieśniakami.Czeka was ostateczna próba.")
                    print("Widzicie przed sobą lidera Klanu Umb. Próbujecie porozmwiać z nim?")
                    odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                    while odpowiedz not in ["tak","nie"]:
                        odpowiedz=zla_odpowiedz()
                    if odpowiedz=="tak":
                        print("Jest to podstęp.Z ukrycia atakują was Strażnicy Klanu Umb.")
                        print("Denver zostaje przejęte przez Klan Umb.")
                        zakonczenie()
                    elif odpowiedz=="nie":
                        print("Nikt was nie wierzył.")
                        print("Udaje się wam przezwyciężyć całą armię Klanu Umb.")
                        print("Zostajecie okryci chwałą, a miasto Denver jest uwolnione od cięmiężcy.")
                        zakonczenie()
                elif wylosowana_postac=="inteligenci":
                    print("Inteligenci szybko znajdują sposób na obejście pułapki, dzięki czemu unikasz walki.")  
                    print("Docieracie do dalszej części świątyni, gdzie czeka was ostatnia próba.")
                    print("W komnacie głównej spotykacie karła, który okazuje się być wysłanikiem Klanu Umb.")
                    print("Zaczyna was atakować magiczną różdżką. Odpowiedzicie atakiem?")
                    odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                    while odpowiedz not in ["tak","nie"]:
                        odpowiedz=zla_odpowiedz()
                    if odpowiedz=="tak":
                        print("Postanawiacie zaatakować. Po zaciętej walce udaje się wam unieszkodliwić przeciwnika.")
                        print("Pokonując wyslanika Klanu Umb, udaje się wam wyzowlić miasto od zagłady.")
                        zakonczenie()
                    elif odpowiedz=="nie":
                        print("Decydujecie się nie atakować. Wysłannik klanu Umb wykorzystuje to, by was pokonać.")
                        print("Przegrywacie walkę, a miasto Denver zostaje przejęte przez klan Umb.")
                        zakonczenie()
            elif odpowiedz=="nie":
                print("Omijacie dźwignię, ale droga staje się coraz bardziej niebezpieczna.")
                print("Docieracie do komnaty glównej, zostajesz sam, gdyż twoi komapani polegli.")
                print("Czeka Cię ostateczna próba.")
                print("Postanawiasz zaatkaować snajperów czy strażników?")
                odpowiedz=input("Odpowiedz snajperzy/strażnicy:").strip().lower()
                while odpowiedz not in ["snajperzy", "strażnicy"]:
                    odpowiedz=zla_wybror()
                if odpowiedz=="snajperzy":
                    print("Walka ze snajpera okazuje się prostsza niż się wydawała.")
                    print("Udaje Ci się pokonać snajperów.Czeka na Ciebie lider Klanu Umb.")
                    print("Postanawiasz pójść na kompromis z liderem Klanu Umb?")
                    odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                    while odpowiedz not in ["tak","nie"]:
                        odpowiedz=zla_odpowiedz()
                    if odpowiedz=="tak":
                        print("Dochodzicie do rozwiązania, w którym miasto zostaje uwolnione.")
                        print("Natomiast część miasta zostaje przeznaczone Klanowi Umb.")
                        zakonczenie()
                    elif odpowiedz=="nie":
                        print("Walczysz z całym Klanem Umb. Twoja nadludzka moc przezywcięża wroga.")
                        print("Miasto Denver zosatje uwolnione.")
                        zakonczenie()
                elif odpowiedz=="strażnicy":
                    print(" Atakujesz strażników. Jest ich za dużo. Giniesz w chwale i bólu.")
                    print("Miasto zostaje pod władzą Klanu Umb.")
                    zakonczenie()
        elif odpowiedz=="nie":
            print("Postanawiasz wyruszyć sam.")
            print("Po długich godzinach podróży spotykasz karła, który oferuje ci pomoc. Przyjmujesz ją?")
            odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
            while odpowiedz not in ["tak","nie"]:
                odpowiedz=zla_odpowiedz()
            if odpowiedz=="tak":
                print("Karzeł okazuje się dobry przewodnikiem.")
                print("Prowadzi Cię do komnaty głównej.")
                print("W komnacie głównej spotykasz się z liderem Klanu Umb.")
                print("Jednak karzeł cię zdradza. Próbujesz go pokonać?")
                odpowiedz=input("Odpowiedz tak/nie:").strip().lower()
                while odpowiedz not in ["tak","nie"]:
                    odpowiedz=zla_odpowiedz()
                if odpowiedz=="tak":
                    print("Udaje Ci się pokonać karła swoją nadludzką siła.")
                    print("Zostaje jednakże pokonany przez lidera Klanu Umb.")
                    print("Miasto zostaje otrute.")
                    zakonczenie()
                elif odpowiedz=="nie":
                    print("Karzeł zdradza Cię, a ty giniesz w pułapcę.")
                    print("Miasto Denver zostje przejęte przez Klanu Umb.")
                    zakonczenie()
            elif odpowiedz=="nie":
                print("Odmawiasz pomocy karła. Rozwcieczony karzeł zastawia na ciebie pułapkę, której nie przeżywasz.")
                print("Powoduje to przejęcie władzy przez Klan Umb.")
                print("Miasto zostaje otrurtę i mieszkańcy giną.")
                zakonczenie()        
   
    def zakonczenie():
        print("Gra się kończy. Dziękuje za grę!")
        exit()
    
    if klasa_postaci=="samuraj":
        samuraj()
    elif klasa_postaci=="wojownik":
        wojownik()
gra()
