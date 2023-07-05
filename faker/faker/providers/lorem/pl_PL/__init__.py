from typing import Dict

from .. import Provider as LoremProvider


class Provider(LoremProvider):
    """Implement lorem provider for ``pl_PL`` locale.

    Source: https://pl.wiktionary.org/wiki/Indeks%3APolski_-_Najpopularniejsze_s%C5%82owa_1-2000
    """

    word_list = (
        "w",
        "z",
        "być",
        "na",
        "i",
        "do",
        "nie",
        "który",
        "lub",
        "to",
        "się",
        "o",
        "mieć",
        "coś",
        "ten",
        "dotyczyć",
        "on",
        "od",
        "co",
        "język",
        "po",
        "że",
        "ktoś",
        "przez",
        "osoba",
        "miasto",
        "jeden",
        "jak",
        "za",
        "ja",
        "rok",
        "a",
        "bardzo",
        "swój",
        "dla",
        "taki",
        "człowiek",
        "cecha",
        "kobieta",
        "mój",
        "część",
        "związany",
        "móc",
        "dwa",
        "ona",
        "związać",
        "ze",
        "mały",
        "jakiś",
        "miejsce",
        "inny",
        "duży",
        "bez",
        "czas",
        "ale",
        "czy",
        "jako",
        "sposób",
        "rodzaj",
        "Polska",
        "rodzina",
        "tylko",
        "mieszkaniec",
        "dzień",
        "praca",
        "przed",
        "dom",
        "dziecko",
        "ty",
        "pod",
        "tak",
        "woda",
        "np.",
        "już",
        "rzeka",
        "zostać",
        "dobry",
        "życie",
        "państwo",
        "mówić",
        "pierwszy",
        "nasz",
        "cały",
        "nad",
        "wiele",
        "zwierzę",
        "przy",
        "roślina",
        "ta",
        "u",
        "jego",
        "gatunek",
        "nowy",
        "chcieć",
        "sobie",
        "wielki",
        "często",
        "trzy",
        "kolor",
        "używać",
        "musieć",
        "kraj",
        "robić",
        "strona",
        "każdy",
        "wysoki",
        "nazwa",
        "mężczyzna",
        "grupa",
        "my",
        "stary",
        "sam",
        "stan",
        "drugi",
        "zrobić",
        "iść",
        "oraz",
        "polski",
        "litera",
        "kto",
        "prawo",
        "drzewo",
        "ptak",
        "książka",
        "świat",
        "samochód",
        "rzecz",
        "stolica",
        "między",
        "droga",
        "należeć",
        "mieszkanka",
        "słowo",
        "gdy",
        "głowa",
        "pies",
        "młody",
        "symbol",
        "oni",
        "bo",
        "ziemia",
        "aby",
        "owoc",
        "liczba",
        "wiek",
        "nie-",
        "kilka",
        "zły",
        "środek",
        "znajdować się",
        "raz",
        "dobrze",
        "pan",
        "kiedy",
        "okres",
        "pochodzić",
        "ojciec",
        "długi",
        "ręka",
        "itp.",
        "odnosić się",
        "dużo",
        "podczas",
        "biały",
        "albo",
        "ruch",
        "jaki",
        "przedmiot",
        "służyć",
        "matka",
        "we",
        "znak",
        "ci",
        "siebie",
        "liczba atomowa",
        "jeszcze",
        "niż",
        "cztery",
        "wszystko",
        "widzieć",
        "żona",
        "koń",
        "szkoła",
        "ciało",
        "stać",
        "kupić",
        "zawsze",
        "forma",
        "sprawa",
        "Rosja",
        "wieś",
        "góra",
        "wyspa",
        "oko",
        "działanie",
        "twój",
        "występować",
        "koniec",
        "rząd",
        "pięć",
        "pokój",
        "nauka",
        "gdzie",
        "kwiat",
        "choroba",
        "zwykle",
        "powiedzieć",
        "mieszkać",
        "wiedzieć",
        "imię",
        "prowadzić",
        "element",
        "dać",
        "godzina",
        "żyć",
        "ryba",
        "wszyscy",
        "zawierać",
        "pracować",
        "by",
        "alfabet",
        "członek",
        "syn",
        "jednostka",
        "herb",
        "brat",
        "las",
        "urządzenie",
        "miesiąc",
        "dziewczyna",
        "obszar",
        "grać",
        "różny",
        "teren",
        "piękny",
        "jeść",
        "nic",
        "brak",
        "żeby",
        "lubić",
        "dany",
        "budynek",
        "położyć",
        "czerwony",
        "cel",
        "stopień",
        "siła",
        "światło",
        "leżeć",
        "dawać",
        "gra",
        "sztuka",
        "czarny",
        "one",
        "jej",
        "wino",
        "chodzić",
        "statek",
        "krótki",
        "śmierć",
        "wartość",
        "dźwięk",
        "sytuacja",
        "teraz",
        "główny",
        "zajmować się",
        "wykonywać",
        "związek",
        "ważny",
        "ostatni",
        "1000",
        "tam",
        "noc",
        "dziś",
        "pierwiastek chemiczny",
        "wojna",
        "noga",
        "sklep",
        "skóra",
        "pani",
        "własny",
        "materiał",
        "niektóry",
        "tworzyć",
        "system",
        "znany",
        "także",
        "wykonać",
        "niebo",
        "święty",
        "władza",
        "wczoraj",
        "film",
        "twarz",
        "flaga",
        "morze",
        "nawet",
        "mięso",
        "głos",
        "Europa",
        "?",
        "pieniądz",
        "powierzchnia",
        "proces",
        "tydzień",
        "posiadać",
        "ilość",
        "obwód",
        "działać",
        "północny",
        "region",
        "jeśli",
        "trwać",
        "szybko",
        "Bóg",
        "silny",
        "!",
        "lecz",
        "zielony",
        "określony",
        "król",
        "pole",
        "przyjaciel",
        "1",
        "dwadzieścia",
        "serce",
        "sześć",
        "słońce",
        "pisać",
        "kot",
        "drzwi",
        "znać",
        "początek",
        "tysiąc",
        "mleko",
        "południowy",
        "obraz",
        "nosić",
        "wiatr",
        "niski",
        "tekst",
        "pić",
        "zmiana",
        "dawny",
        "ulica",
        "kierunek",
        "linia",
        "jechać",
        "wyraz",
        "stanowić",
        "charakterystyczny",
        "składać się",
        "tu",
        "uważać",
        "siedem",
        "miłość",
        "podobny",
        "więc",
        "żołnierz",
        "siostra",
        "córka",
        "też",
        "chleb",
        "zacząć",
        "koło",
        "granica",
        "powietrze",
        "pewien",
        "włos",
        "charakter",
        "punkt",
        "dzisiaj",
        "ludzie",
        "mało",
        "liść",
        "(…)",
        "znaleźć",
        "kościół",
        "badanie",
        "niewielki",
        "wziąć",
        "prosty",
        "krew",
        "mąż",
        "–",
        "wolny",
        "kawa",
        "problem",
        "pójść",
        "powodować",
        "czyjś",
        "drewno",
        "kształt",
        "stać się",
        "właściwy",
        "trzeci",
        "znaczenie",
        "brzeg",
        "historia",
        "ich",
        "zasada",
        "brać",
        "dziesięć",
        "powinien",
        "żaden",
        "jezioro",
        "okno",
        "kultura",
        "niemiecki",
        "ostry",
        "but",
        "stosować",
        "ogień",
        "nigdy",
        "zbiór",
        "samolot",
        "ból",
        "osiem",
        "można",
        "gwiazda",
        "walka",
        "Ukraina",
        "prawdziwy",
        "ciężki",
        "zespół",
        "drogi",
        "pracownik",
        "Francja",
        "myśleć",
        "zachowanie",
        "polegać",
        "uwaga",
        "pomoc",
        "przypominać",
        "grecki",
        "Niemcy",
        "ząb",
        "ile",
        "informacja",
        "chwila",
        "deszcz",
        "istnieć",
        "nauczyciel",
        "żółty",
        "chory",
        "piwo",
        "według",
        "dostać",
        "uczeń",
        "jedzenie",
        "śnieg",
        "jednak",
        "również",
        "ani",
        "zwłaszcza",
        "utwór",
        "czysty",
        "firma",
        "siedzieć",
        "francuski",
        "łączyć",
        "południe",
        "zbyt",
        "trudny",
        "urząd",
        "stół",
        "lekarz",
        "muzyka",
        "czynność",
        "układ okresowy",
        "pociąg",
        "jasny",
        "klasa",
        "męski",
        "kamień",
        "pierwiastek",
        "ubranie",
        "ściana",
        "postać",
        "pełny",
        "organizm",
        "5",
        "księżyc",
        "gmina",
        "rosnąć",
        "w celu",
        "wydawać",
        "źródło",
        "funkcja",
        "położenie",
        "typ",
        "starożytny",
        "jutro",
        "dziewięć",
        "trzeba",
        "społeczny",
        "prawy",
        "program",
        "pojazd",
        "może",
        "historyczny",
        "2",
        "substancja",
        "wszystkie",
        "piec",
        "układ",
        "bóg",
        "polityczny",
        "chłopiec",
        "cena",
        "słaby",
        "głupi",
        "ludzki",
        "trzymać",
        "zupa",
        "około",
        "mieszkanie",
        "zdanie",
        "naczynie",
        "uprawiać",
        "północ",
        "kraina",
        "numer",
        "para",
        "dokument",
        "uczucie",
        "prawda",
        "złoty",
        "za pomocą",
        "elektryczny",
        "dziedzina",
        "zachodni",
        "alkohol",
        "trochę",
        "prowincja",
        "prosić",
        "list",
        "bliski",
        "komputer",
        "towar",
        "szybki",
        "spać",
        "niebieski",
        "aż",
        "przypadek",
        "organizacja",
        "herbata",
        "szeroki",
        "kawałek",
        "czytać",
        "obejmować",
        "wojskowy",
        "narzędzie",
        "przyjść",
        "myśl",
        "ogród",
        "Włochy",
        "całość",
        "wieczór",
        "lód",
        "wiedza",
        "powiat",
        "połowa",
        "angielski",
        "głównie",
        "zjawisko",
        "chłopak",
        "wpływ",
        "mowa",
        "naturalny",
        "morski",
        "produkt",
        "lewy",
        "prawie",
        "lek",
        "miejscowość",
        "napój",
        "wschodni",
        "księga",
        "stopa",
        "drobny",
        "ciasto",
        "kuchnia",
        "plan",
        "powstać",
        "pełen",
        "wokół",
        "kochać",
        "palec",
        "zobaczyć",
        "poprzez",
        "maszyna",
        "dziadek",
        "wielkość",
        "nos",
        "złoto",
        "pewny",
        "partia",
        "większość",
        "obiekt",
        "publiczny",
        "pismo",
        "wybitny",
        "wszystek",
        "błąd",
        "broń",
        "sen",
        "trzydzieści",
        "gruby",
        "spotkanie",
        "tkanina",
        "smak",
        "gość",
        "potrawa",
        "pytanie",
        "produkcja",
        "wy",
        "razem",
        "obywatel",
        "jajko",
        "3",
        "zima",
        "nazywać",
        "policja",
        "nikt",
        "słodki",
        "dopływ",
        "butelka",
        "energia",
        "składać",
        "łóżko",
        "urodzenie",
        "zdrowie",
        "odmiana",
        "zdjęcie",
        "mocny",
        "poza",
        "4",
        "lekki",
        "czynić",
        "przeciwny",
        "duch",
        "sąd",
        "przeznaczyć",
        "zapach",
        "stały",
        "Afryka",
        "styl",
        "karta",
        "wypadek",
        "babcia",
        "wojsko",
        "wodny",
        "równy",
        "rola",
        "rejon",
        "wybrzeże",
        "naród",
        "wiadomość",
        "kość",
        "tytuł",
        "cukier",
        "barwa",
        "żywy",
        "szczyt",
        "rozwój",
        "sieć",
        "30",
        "ponad",
        "lato",
        "warstwa",
        "jabłko",
        "wyrażać",
        "bogaty",
        "odbywać się",
        "podstawowy",
        "cześć",
        "z powodu",
        "ponieważ",
        "wyjść",
        "poziom",
        "wyglądać",
        "śpiewać",
        "oznaczać",
        "rozmowa",
        "ciemny",
        "papier",
        "900",
        "palić",
        "lud",
        "długość",
        "usta",
        "ucho",
        "urodzić",
        "wewnątrz",
        "wśród",
        "przedstawiciel",
        "środkowy",
        "obok",
        "dzieło",
        "arabski",
        "krowa",
        "taniec",
        "rano",
        "grzyb",
        "długo",
        "wydarzenie",
        "pięćdziesiąt",
        "włoski",
        "słuchać",
        "ser",
        "właśnie",
        "stanowisko",
        "odpowiedni",
        "korona",
        "rower",
        "święto",
        "czekać",
        "szukać",
        "100",
        "religia",
        "piłka",
        "opinia",
        "wynik",
        "pozycja",
        "pochodzenie",
        "metoda",
        "ciepły",
        "potem",
        "udział",
        "Hiszpania",
        "rozumieć",
        "6",
        "wspólny",
        "środowisko",
        "całkowicie",
        "budowa",
        "ramię",
        "gazeta",
        "zabawa",
        "nie ma",
        "szczęście",
        "pomieszczenie",
        "strach",
        "fala",
        "patrzeć",
        "odcień",
        "temperatura",
        "warunek",
        "zdolność",
        "sól",
        "rosyjski",
        "podróż",
        "wykorzystywać",
        "Ziemia",
        "religijny",
        "centrum",
        "zbierać",
        "zupełnie",
        "przestrzeń",
        "pas",
        "połączenie",
        "wobec",
        "stawać się",
        "potrzeba",
        "narodowy",
        "liczyć",
        "otwarty",
        "wejść",
        "pozbawić",
        "masa",
        "głęboki",
        "ono",
        "wywoływać",
        "zachód",
        "wschód",
        "powód",
        "Azja",
        "administracyjny",
        "temat",
        "odpowiadać",
        "szpital",
        "zajmować",
        "czterdzieści",
        "sto",
        "sobą",
        "pogląd",
        "chronić",
        "wysokość",
        "słownik",
        "rodzic",
        "świnia",
        "zaczynać",
        "moneta",
        "możliwość",
        "mama",
        "gdzieś",
        "egzamin",
        "pogoda",
        "chemiczny",
        "gorący",
        "zadanie",
        "więzienie",
        "zakład",
        "ofiara",
        "obiad",
        "wąski",
        "zamek",
        "moc",
        "stosunek",
        "natura",
        "8",
        "zazwyczaj",
        "założyć",
        "skrzydło",
        "otrzymać",
        "oficjalny",
        "chmura",
        "ten sam",
        "złożyć",
        "wewnętrzny",
        "wspaniały",
        "przyczyna",
        "miły",
        "dziki",
        "kara",
        "listopad",
        "komórka",
        "instytucja",
        "skała",
        "ogromny",
        "wygląd",
        "sześćdziesiąt",
        "możliwy",
        "wąż",
        "umrzeć",
        "określać",
        "amerykański",
        "płynąć",
        "walczyć",
        "nóż",
        "nagle",
        "instrument",
        "20",
        "rynek",
        "Grecja",
        "umowa",
        "niedziela",
        "szczęśliwy",
        "tutaj",
        "zmieniać",
        "węgiel",
        "sylaba",
        "Warszawa",
        "ładny",
        "europejski",
        "czwarty",
        "styczeń",
        "hiszpański",
        "posługiwać się",
        "papieros",
        "fizyczny",
        "dach",
        "zimny",
        "ogon",
        "trawa",
        "telefon",
        "płyn",
        "przedstawiać",
        "metal",
        "dlaczego",
        "próbować",
        "10",
        "7",
        "sportowy",
        "oddział",
        "obecnie",
        "9",
        "miara",
        "prezydent",
        "pierś",
        "rodowity",
        "stworzyć",
        "dział",
        "dusza",
        "wierzyć",
        "domowy",
        "właściciel",
        "wyrób",
        "autobus",
        "ponownie",
        "gaz",
        "właściwość",
        "rada",
        "rzymski",
        "bieg",
        "zgoda",
        "obowiązek",
        "owca",
        "zamieszkiwać",
        "przyjąć",
        "muzyczny",
        "przyrząd",
        "piąty",
        "szczególnie",
        "kupować",
        "istota",
        "stracić",
        "artykuł",
        "ochrona",
        "te",
        "napisać",
        "specjalista",
        "ku",
        "górski",
        "należy",
        "określenie",
        "pomiędzy",
        "Rzym",
        "ssak",
        "zwolennik",
        "odpowiedź",
        "działalność",
        "miejski",
        "wcześnie",
        "zdobyć",
        "górny",
        "uniwersytet",
        "bić",
        "wymagać",
        "miękki",
        "źle",
        "40",
        "państwowy",
        "ludność",
        "minuta",
        "cierpieć",
        "ogół",
        "naprawdę",
        "blisko",
        "surowy",
        "dodatek",
        "radość",
        "akcja",
        "w kształcie",
        "polityka",
        "obcy",
        "ziemniak",
        "podstawa",
        "przemysł",
        "udać się",
        "brzuch",
        "suchy",
        "krzew",
        "terytorium",
        "wolność",
        "czyli",
        "klucz",
        "Jan",
        "kolejny",
        "uczyć się",
        "postępowanie",
        "sok",
        "50",
        "łatwo",
        "jeździć",
        "decyzja",
        "naukowy",
        "szanowny",
        "warzywo",
        "nadzieja",
        "wrzesień",
        "kierować",
        "student",
        "kąt",
        "seksualny",
        "piasek",
        "drewniany",
        "obchodzić",
        "wróg",
        "przeciwko",
        "żeński",
        "potrafić",
        "pamięć",
        "teatr",
        "dwudziesty",
        "znowu",
        "potrzebować",
        "owad",
        "cienki",
        "ziarno",
        "moment",
        "wiosna",
        "wydać",
        "literatura",
        "tradycyjny",
        "leczenie",
        "poważny",
        "siedemdziesiąt",
        "silnik",
        "spokój",
        "luty",
        "biedny",
        "czuć",
        "drużyna",
        "dialekt",
        "dzięki",
        "grudzień",
        "jedyny",
        "pragnienie",
        "siedziba",
        "służba",
        "wiara",
        "pióro",
        "wzrost",
        "proszę",
        "osiemdziesiąt",
        "społeczeństwo",
        "dokładnie",
        "przykład",
        "szacunek",
        "marzec",
        "róg",
        "połączyć",
        "uderzenie",
        "zwyczaj",
        "podawać",
        "mocno",
        "zwykły",
        "kolega",
        "międzynarodowy",
        "sala",
        "nadawać",
        "tamten",
        "szósty",
        "lekcja",
        "pomagać",
        "republika",
        "zjeść",
        "typowy",
        "modlitwa",
        "dół",
        "dlatego",
        "rasa",
        "użycie",
        "dziewięćdziesiąt",
        "bok",
        "zatoka",
        "wiersz",
        "Szwecja",
        "japoński",
        "gałąź",
        "wrogi",
        "przyjmować",
        "więcej",
        "łatwy",
        "atak",
        "wychodzić",
        "wtedy",
        "płyta",
        "milion",
        "padać",
        "kanał",
        "poniedziałek",
        "wzór",
        "twardy",
        "podatek",
        "rzucać",
        "świeży",
        "bilet",
        "zakładać",
        "złapać",
        "przyszłość",
        "przyjęcie",
        "zewnętrzny",
        "zamknąć",
        "przynosić",
        "obecny",
        "strój",
        "popularny",
        "późno",
        "płaski",
        "struktura",
        "pieniądze",
        "projekt",
        "doświadczenie",
        "szyja",
        "rozmawiać",
        "literacki",
        "okolica",
        "mur",
        "małżeństwo",
        "bitwa",
        "kwiecień",
        "maj",
        "specjalny",
        "poruszać się",
        "sąsiad",
        "organ",
        "pamiętać",
        "uczyć",
        "termin",
        "bank",
        "pusty",
        "pół",
        "wchodzić",
        "czyn",
        "Japonia",
        "przeciw",
        "wczesny",
        "wejście",
        "ciągle",
        "bać się",
        "Stany Zjednoczone",
        "delikatny",
        "wilk",
        "kula",
        "r.",
        "wnętrze",
        "prąd",
        "sprzedawać",
        "port",
        "spokojny",
        "waga",
        "sztuczny",
        "Polak",
        "jajo",
        "dym",
        "pszczoła",
        "technika",
        "współczesny",
        "widoczny",
        "krok",
        "próba",
        "gęsty",
        "miód",
        "ciepło",
        "mapa",
        "kapelusz",
        "otwór",
        "lew",
        "osioł",
        "gwałtowny",
        "siódmy",
        "budować",
        "los",
        "telewizja",
        "spowodować",
        "dłoń",
        "akt",
        "mysz",
        "jesień",
        "składnik",
        "słyszeć",
        "zgodnie",
        "zdrowy",
        "masło",
        "gwiazdozbiór",
        "kino",
        "podać",
        "zmienić",
        "przechodzić",
        "fabryka",
        "dość",
        "daleko",
        "z krwi i kości",
        "płeć",
        "chiński",
        "sędzia",
        "pokryć",
        "lotniczy",
        "nazwisko",
        "bądź",
        "Słowacja",
        "umieć",
        "majątek",
        "ocena",
        "pływać",
        "komputerowy",
        "dziać się",
        "ósmy",
        "autor",
        "sierpień",
        "łagodny",
        "zakres",
        "wybrać",
        "następny",
        "odległość",
        "most",
        "policjant",
        "panować",
        "zawód",
        "zwrot",
        "wybór",
        "Chiny",
        "internetowy",
        "wytwarzać",
        "lipiec",
        "bohater",
        "prasa",
        "penis",
        "Czechy",
        "80",
        "fakt",
        "piosenka",
        "mąka",
        "badać",
        "sobota",
        "piątek",
        "znajdować",
        "straszny",
        "waluta",
        "pojechać",
        "otwierać",
        "umiejętność",
        "ślub",
        "restauracja",
        "przedsiębiorstwo",
        "towarzystwo",
        "model",
        "no",
        "prywatny",
        "reakcja",
        "okazja",
        "porządek",
        "opowiadać",
        "przeciwnik",
        "mięsień",
        "zysk",
        "sprzedaż",
        "zabić",
        "różnica",
        "klasztor",
        "osiągnąć",
        "niebezpieczny",
        "pisarz",
        "wrócić",
        "skład",
        "m.in.",
        "sprawiać",
        "chrześcijański",
        "zapomnieć",
        "gniew",
        "planeta",
        "postawić",
        "przejść",
        "kurs",
        "przygotować",
        "dzielić",
        "dzielnica",
        "kierowca",
        "własność",
        "królowa",
        "korzeń",
        "artysta",
        "stawiać",
        "jakość",
        "przyjemność",
        "średni",
        "ludowy",
        "całkowity",
        "Dania",
        "biblioteka",
        "dopiero",
        "zero",
        "gniazdo",
        "pieśń",
        "urzędnik",
        "przestać",
        "dziura",
        "Anglia",
        "mózg",
        "liczny",
        "uderzać",
        "efekt",
        "rozmiar",
        "przyjemny",
        "norma",
        "pozwalać",
        "rana",
        "korzyść",
        "tańczyć",
        "kosztować",
        "Słońce",
        "podział",
        "samica",
        "przepis",
        "hotel",
        "rzadko",
        "wykonanie",
        "brzydki",
        "otworzyć",
        "armia",
        "kiedyś",
        "brązowy",
        "rzeczywistość",
        "prędkość",
        "szef",
        "ciecz",
        "kaczka",
        "szkolny",
        "dokonywać",
        "fałszywy",
        "koszula",
        "tyle",
        "rzeczownik",
        "złożony",
        "zawodnik",
        "-",
        "tradycja",
        "śniadanie",
        "usługa",
        "skończyć",
        "Białoruś",
        "znów",
        "handel",
        "mieć na imię",
        "królestwo",
        "jądro",
        "powstawać",
        "okrągły",
        "spodnie",
        "powoli",
        "godny",
        "jeżeli",
        "ślad",
        "przedstawienie",
        "olej",
        "jazda",
        "dyskusja",
        "wyrażenie",
        "daleki",
        "sądzić",
        "Ameryka",
        "tracić",
        "znosić",
        "profesor",
        "świątynia",
        "szary",
        "piłka nożna",
        "zboże",
        "uderzyć",
        "wola",
        "srebro",
        "dolina",
        "w postaci",
        "różowy",
        "zamykać",
        "wrogość",
        "Indie",
        "dziwny",
        "czasem",
        "temu",
        "wtorek",
        "oglądać",
        "sport",
        "małpa",
        "spotkać",
        "zdarzenie",
        "wódka",
        "wrażenie",
        "kalendarz",
        "pomysł",
        "odczuwać",
        "koszt",
        "plemię",
        "bydło",
        "strumień",
        "skutek",
        "książę",
        "całkiem",
        "papież",
        "dodawać",
        "brudny",
        "przyszły",
        "mecz",
        "scena",
        "wolno",
        "klient",
        "opisać",
        "szereg",
        "ciąża",
        "coraz",
        "złodziej",
        "Izrael",
        "głód",
        "otaczać",
        "władca",
        "transport",
        "w formie",
        "niebezpieczeństwo",
        "słoneczny",
        "figura",
        "wszelki",
        "wysiłek",
        "kolano",
        "niech",
        "tłuszcz",
        "zakończenie",
        "mi",
        "ksiądz",
        "żelazo",
        "łuk",
        "mebel",
        "Afganistan",
        "nieszczęście",
        "wskazywać",
        "plaża",
        "fragment",
        "zaś",
        "metr",
        "kościelny",
        "samochodowy",
        "zachowywać się",
        "obrona",
        "danie",
        "wierny",
        "amharski",
        "lista",
        "żart",
        "ogólny",
        "kontrola",
        "budzić",
        "90",
        "tłum",
        "naj-",
        "kontakt",
        "czasownik",
        "gotowy",
        "Jezus",
        "koza",
        "zbiornik",
        "obserwować",
        "grób",
        "stacja",
        "robotnik",
        "czerwiec",
        "październik",
        "konstrukcja",
        "choć",
        "wyjście",
        "minerał",
        "kosz",
        "60",
        "cebula",
        "samiec",
        "sos",
        "zmarły",
        "ojczyzna",
        "bycie",
        "szkoda",
        "niszczyć",
        "majuskuła",
        "przejaw",
        "zniszczyć",
        "niedźwiedź",
        "pokazywać",
        "gospodarka",
        "zbudować",
        "dodatkowy",
        "park",
        "opłata",
        "wysoko",
        "Egipt",
        "zegar",
        "wujek",
        "dawno",
        "studia",
        "cesarz",
        "wizyta",
        "przyprawa",
        "łódź",
        "powszechny",
        "robota",
        "metalowy",
        "biec",
        "dobro",
        "dzisiejszy",
        "obóz",
        "żydowski",
        "USA",
        "Chrystus",
        "oddawać",
        "widok",
        "marka",
        "pojęcie",
        "miecz",
        "krzyż",
        "tajemnica",
        "chłop",
        "Austria",
        "lecieć",
        "bezpieczeństwo",
        "królewski",
        "śmiech",
        "postawa",
        "sukces",
        "zgodny",
        "płaszcz",
        "Turcja",
        "przeszkoda",
        "prostytutka",
        "operacja",
        "wywołać",
        "narząd",
        "futro",
        "świeca",
        "Australia",
        "prawny",
        "wciąż",
        "Szwajcaria",
        "powieść",
        "gotować",
        "szczególny",
        "rozwiązanie",
        "relacja",
        "studiować",
        "stado",
        "w czasie",
        "kontynent",
        "przychodzić",
        "lis",
        "strefa",
        "70",
        "wypowiedź",
        "dziewiąty",
        "idea",
        "kura",
        "grunt",
        "farba",
        "wóz",
        "epoka",
        "lęk",
        "smutny",
        "kolejowy",
        "dodać",
        "uchodzić",
        "przygotowywać",
        "przynieść",
        "umysł",
        "suma",
        "interes",
        "produkować",
        "Boże Narodzenie",
        "wieża",
        "handlowy",
        "gdyby",
        "Kraków",
        "utrzymywać",
        "urodziny",
        "natychmiast",
        "uciekać",
        "chociaż",
        "słoń",
        "prezent",
        "odwaga",
        "ciężar",
        "płacić",
        "podłoga",
        "atmosfera",
        "wspólnota",
        "zwycięstwo",
        "treść",
        "zainteresowanie",
        "zamiast",
        "tor",
        "artystyczny",
        "dwanaście",
        "zdolny",
        "pojedynczy",
        "przejście",
        "moralny",
        "reguła",
        "naukowiec",
        "osobisty",
        "mnóstwo",
        "wybory",
        "jedynie",
        "wada",
        "sygnał",
        "wykonywanie",
        "wybierać",
        "umieszczać",
        "mistrz",
        "nagły",
        "dno",
        "pomarańczowy",
        "telewizyjny",
        "radio",
        "przerwa",
        "matematyka",
        "klub",
        "środa",
        "muzeum",
        "finansowy",
        "malować",
        "opieka",
        "Żyd",
        "ośrodek",
        "krzesło",
        "ukraiński",
        "kolej",
        "kłopot",
        "ryż",
        "cień",
        "szwedzki",
        "usuwać",
        "katolicki",
        "cierpienie",
        "znaczny",
        "umożliwiać",
        "Rumunia",
        "poznać",
        "wynosić",
        "pijany",
        "zakończyć",
        "intensywny",
        "kostka",
        "świadczyć",
        "wydawać się",
        "godność",
        "Unia Europejska",
        "orzeł",
        "burza",
        "chrześcijaństwo",
        "błoto",
        "biskup",
        "gardło",
        "szkło",
        "polityk",
        "umieścić",
        "pozostać",
        "czwartek",
        "piętro",
        "odkryć",
        "powstanie",
        "zakon",
        "oddech",
        "nastrój",
        "teoria",
        "doskonały",
        "dolny",
        "spadek",
        "zawartość",
        "zatrzymać",
        "aktor",
        "grzech",
        "otrzymywać",
        "anioł",
        "szklanka",
        "ciekawy",
        "pomóc",
        "pomidor",
        "smutek",
        "Wielka Brytania",
        "pora",
        "śmiać się",
        "abugida",
        "odcinek",
        "nasiono",
        "pokarm",
        "zimno",
        "wieczorem",
        "wracać",
        "azjatycki",
        "wysłać",
        "sprzęt",
        "posiłek",
        "ozdobny",
        "impreza",
        "potrzebny",
        "znaczyć",
        "łyżka",
        "narkotyk",
        "biuro",
        "parlament",
        "obywatelka",
        "babka",
        "zabawka",
        "dorosły",
        "ćwiczenie",
        "ocean",
        "nadmierny",
        "niezwykły",
        "bieda",
        "użytkownik",
        "polować",
        "dyrektor",
        "procent",
        "ziemski",
        "spór",
        "żaba",
        "starać się",
        "w wyniku",
        "pacjent",
        "Litwa",
        "wycieczka",
        "istotny",
        "lampa",
        "mgła",
        "Węgry",
        "późny",
        "dziewczynka",
        "lina",
        "w ciągu",
        "mocz",
        "motyl",
        "półwysep",
        "staw",
        "przybyć",
        "duński",
        "nieprzyjemny",
        "wakacje",
        "przestępstwo",
        "centralny",
        "odzież",
        "głośny",
        "wysyłać",
        "wina",
        "pożar",
        "pasek",
        "przyjaźń",
        "koncert",
        "zarówno",
        "turecki",
        "na zewnątrz",
        "kilometr",
        "zapalenie",
        "tani",
        "pytać",
        "św.",
        "dane",
        "poeta",
        "łąka",
        "trudność",
        "ciotka",
        "seks",
        "bar",
        "pasmo",
        "zaraz",
        "ubogi",
        "po prostu",
        "igła",
        "cmentarz",
        "dziób",
        "róża",
        "pozostawać",
        "zawodowy",
        "tablica",
        "klimat",
        "cisza",
        "okropny",
        "włosy",
        "wzdłuż",
        "medycyna",
        "bawić się",
        "wzrok",
        "w.",
        "bogini",
        "wioska",
        "letni",
        "chyba",
        "poczta",
        "deska",
        "hodować",
        "wreszcie",
        "przyjechać",
        "filmowy",
        "kończyć",
        "psychiczny",
        "uzyskać",
        "rachunek",
        "minister",
        "dowód",
        "lata",
        "mrówka",
        "radiowy",
        "średniowieczny",
        "mądry",
        "przeprowadzać",
        "kolacja",
        "jakby",
        "pragnąć",
        "sądowy",
        "ustawa",
        "zaufanie",
        "wojenny",
        "obowiązywać",
        "promień",
        "Kościół",
        "dać się",
        "kult",
        "traktować",
        "czapka",
        "ciągnąć",
        "paliwo",
        "—",
        "diabeł",
        "Holandia",
        "broda",
        "w końcu",
        "powolny",
        "muzyk",
        "korzystać",
        "sowa",
        "dokładny",
        "czoło",
        "zając",
        "na przykład",
        "płakać",
        "podnieść",
        "wybuch",
        "spaść",
        "byk",
        "budowla",
        "zgromadzenie",
        "odważny",
        "czynnik",
        "zeszły",
        "wesoły",
        "pająk",
        "opuścić",
        "ciemność",
        "kij",
        "pałac",
        "archipelag",
        "pojawiać się",
        "panna",
        "gęś",
        "nauczycielka",
        "zajęcie",
        "trudno",
        "pustynia",
        "kieszeń",
        "fotografia",
        "tytoń",
        "upadek",
        "wyrok",
        "istnienie",
        "zanim",
        "wyścig",
        "chęć",
        "świecić",
        "częściowo",
        "dokonać",
        "żywność",
        "sukienka",
        "obrót",
        "toponim",
        "wpaść",
        "podróżować",
        "kolumna",
        "rodzinny",
        "poprzedni",
        "Niemiec",
        "pisanie",
        "oddać",
        "rzadki",
        "bułgarski",
        "otoczenie",
        "kobiecy",
        "kolorowy",
        "kartka",
        "urodzić się",
        "piętnaście",
        "uznawać",
        "okręt",
        "trzydziesty",
        "wniosek",
        "głupiec",
        "strata",
        "większy",
        "podnosić",
        "nocny",
        "wywodzić się",
        "filozofia",
        "inaczej",
        "Pan",
        "ozdoba",
        "uciec",
        "martwy",
        "hałas",
        "lotnisko",
        "tył",
        "łaciński",
        "położony",
        "pełnić",
        "kwestia",
        "tarcza",
        "0",
        "skłonność",
        "go",
        "talerz",
        "wygrać",
        "Morze Śródziemne",
        "minuskuła",
        "szlachetny",
        "poruszać",
        "jadalny",
        "jedenaście",
        "nieść",
        "szkodliwy",
        "użyć",
        "lot",
        "wystawa",
        "pokonać",
        "przebywać",
        "przeszłość",
        "adres",
        "wisieć",
        "oś",
        "zmęczony",
        "katastrofa",
        "zamiar",
        "bogactwo",
        "niechęć",
        "poduszka",
        "rak",
        "jednocześnie",
        "dziecięcy",
        "wstyd",
        "białoruski",
        "rozpocząć",
        "rzucić",
        "ulegać",
        "policzek",
        "wzgórze",
        "hasło",
        "lustro",
        "wkrótce",
        "narodowość",
        "pojawić się",
        "skala",
        "zapis",
        "stowarzyszenie",
        "zgadzać się",
        "rezultat",
        "oba",
        "przecież",
        "czeski",
        "tłumaczyć",
        "rysunek",
        "kłaść",
        "aktywny",
        "gołąb",
        "praktyka",
        "okoliczność",
        "trwały",
        "oczekiwać",
        "ryzyko",
        "dostęp",
        "wyłącznie",
        "czekolada",
        "oczywiście",
        "dalej",
        "dar",
        "włożyć",
        "zrozumieć",
        "postępować",
        "srebrny",
        "doprowadzić",
        "analiza",
        "mierzyć",
        "banknot",
        "głupota",
        "głupek",
        "słowacki",
        "plama",
        "uśmiech",
        "konflikt",
        "gleba",
        "gospodarczy",
        "plecy",
        "następować",
        "zaburzenie",
        "blady",
        "spadać",
        "plac",
        "cichy",
        "alkoholowy",
        "pomarańcza",
        "bajka",
        "wprowadzać",
        "żołądek",
        "latać",
        "niewolnik",
        "rolnik",
        "wspomnienie",
        "zająć",
        "nasienie",
        "Belgia",
        "wątpliwość",
        "bezpośrednio",
        "graniczyć",
        "gorączka",
        "bronić",
        "rządzić",
        "drapieżny",
        "pojemnik",
        "Piotr",
    )

    parts_of_speech: Dict[str, tuple] = {}