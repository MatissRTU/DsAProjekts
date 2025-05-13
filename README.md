# DS&A Projekts: LEGO komplektu atlaižu apkopotājs
## Projekta uzdevums
Projekta mērķis ir ievākt datus no dažādiem interneta iepirkšanās veikaliem (220.lv;1a.lv;Ksenukai.lv). Dati tiks ievākti no akciju/atlaižu katalogiem, kurus saglabās modificētā hashmap kam par atslēgu būs produkta cena, un tajā glabāsies pārējā komplekta informācija (Nosaukums,produkta bilde), ko pēc tam izvadīs excel formātā.

## Izmantotās Python bibliotēkas
* request - lai kods būtu spējīgs atvērt interneta saiti un noslasīt tās datus
* BeautifulSoup - nepieciešams lai python kods būtu spējīgs pārtūlkot HTML uz pythona valodā lietojamu kodu
* openpyxl - lai strādātu ar Excel

## Projekta laikā lietotās datu struktūras
HashTable, ar modifikāciju vienai atslēgai pievienot papildus vērtības
     
## Kā izmantot programmu
Lego komplektu ID, Nosaukums, Cena, Links uz komplektu, ražošanas datums?

## Lietošanas pamācība
1. novieto python failu mapē kurā vēlas dabūt excel failu.
2. palaži Legosort.py
3. Terminālī parādīsies norāde, ka meklē produktus, jāgaida kāmēr visas mājaslapas tiek izskatītas.
4. 
5. Atvērsies vaļā excels ar datiem
