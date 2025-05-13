# DS&A Projekts: LEGO komplektu atlaižu apkopotājs
## Projekta uzdevums
Projekta mērķis ir ievākt datus no dažādiem interneta iepirkšanās veikaliem (m79.lv;1a.lv). Dati tiks ievākti no akciju/atlaižu katalogiem, kurus saglabās modificētā hashmap kam par atslēgu būs produkta cena, un tajā glabāsies pārējā komplekta informācija (Nosaukums,produkta bilde), ko pēc tam, apstrādājot ar cenas filtru, 
izvadīs excel formātā.

## Izmantotās Python bibliotēkas
* request - lai kods būtu spējīgs atvērt interneta saiti un noslasīt tās datus
* BeautifulSoup - nepieciešams lai iegūtu datus no html faila (mūsu gadījumā saites)
* openpyxl - lai izveidotu, formatētu un saglabātu Excel failu

## Projekta laikā lietotās datu struktūras
HashTable, ar modifikāciju vienai atslēgai pievienot papildus vērtības

## Programmas metodes
### search1(url,id)
Search1 funkcija sākumā pieprasa pieeju iepriekš norādītai saitei un izmanto gatavu user-agent, tad tā pārliecinās vai "page" status ir 200(lapa strādā normāli un no tās var ievākt datus). Izmantojot BeautifulSoup bibliotēku, tiek nolasīti dati no saites lapas, kā piemēram pēdējā lapas puse, kas ļauj ciklēt cauri visām lapām un nolasīt datus par visām precēm(šajā gadījumā LEGO komplektiem). Tiek izprintēts progresa teksts, kas rāda no cik daudz lapaspusēm dati jau ir "noskrāpēti" pret kopējo lapas pušu skaitu. Ievāktie dati tiek sadalīti: "name", "price", "img" mainīgajos, kurus visus pievieno HashTable, ko vēlāk izmatos sort_to_excel metodei.

### search2(url,id)
Search2 funkcijas rezultāts ir tāds pats kā Search1, bet kā līdz tam tika ir atšķirīgas, jo abiem interneta veikaliem bija atšķirīgas html sistēmas uzbūves un klašu nosaukumi, kā arī pat URL bija atšķirīgi, teiksim tā ja diviem interneta veikaliem ir atšķirīga html veidne, tad arī search funkcija ir jāpielāgo. Tātad, īss apkopojums, pieprasa pieeju saitei, izveido ciklu, kas iziet cauri visām lapaspusēm, ievācot trīs lietas par LEGO komplektiem, un šos datus noglabā HashTable.

### sort_to_excel(price_range)
Sort_to_Excel funkcija sāk ar Excel atvēršanu, izveido jaunu excel failu, kuram pievieno trīs tabulas "Nosaukums", "Cena", "Bilde" tad noformē kolonnu izmērus un tad ciklā kura garumu nosaka to cik daudz produkti ir saglabāti HashTable tiek sākti dalīt pēc iepriekš izvēlētas maksimālās cenas, un tikai tās cenas kuras ir zem vai vienādi ar norādīto vērtību tiks pievienotas Excel failam, automātiski tiek noformēta katra rinda, kad tajā ievieto datus. Excel failā arī ir redzamas bildes katram komplektam, bet tā kā  bildes ir URL links nevis reālas bildes Excel kopējais izmērs ir mazs, visbeidzot Excel failu saglabā kā: "Lego_akcijas.xlsx" 

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
