# DS&A Projekts: LEGO komplektu atlaižu apkopotājs
## Projekta uzdevums
Projekta mērķis ir ievākt datus no dažādiem interneta iepirkšanās veikaliem (220.lv;1a.lv). Dati tiks ievākti no akciju/atlaižu katalogiem, kurus saglabās modificētā hashmap kam par atslēgu būs produkta cena, un tajā glabāsies pārējā komplekta informācija (Nosaukums,produkta bilde), ko pēc tam, apstrādājot ar cenas filtru, 
izvadīs excel formātā.

## Izmantotās Python bibliotēkas
* request - lai kods būtu spējīgs atvērt interneta saiti un noslasīt tās datus
* BeautifulSoup - nepieciešams lai iegūtu datus no html faila (mūsu gadījumā saites)
* openpyxl - lai izveidotu, formatētu un saglabātu Excel failu

## Projekta laikā lietotās datu struktūras
HashTable, ar modifikāciju vienai atslēgai pievienot papildus vērtības

## Programmas metodes
### search1(url,id)

### search2(url,id)

### sort_to_excel(price_range)

## Kad izmantot programmu
Programma galvenokārt domāta lego komplektu atlaižu meklēšanai, bet ar minimālām modifikācijām to var izmantot projekta mērķa mājaslapās citām precēm(1a.lv gadījumā arī ksenukai.lv)

## Lietošanas pamācība
1. novieto python failu mapē kurā vēlas dabūt excel failu.
2. palaži Legosort.py
3. Terminālī parādīsies norāde, ka meklē produktus, jāgaida kāmēr visas mājaslapas tiek izskatītas.
4. Kad tiks prasīts ievadīt maksimālo cenu vai exit, ievadīt cenu vai vārdu "exit" (exit paskaidrojums 7.punktā)
5. kad tiks ievadīta cena tiks izveidots excel fails, kurā atrodas preces ar cenu zem ievadītās cenas.
6. Kodu var atstāt ejošu, apskatīties datus, aizvērt exceli un ievadīt citu cenu(ja vēlas)
7. Kad kods vairs nav nepieciešams, to var aizvērt ierakstot exit(aizver termināli) vai aizvērt termināli ar "X" augšā labajā stūrī
