# DS&A Projekts par LEGO komplektiem :shipit:

## Projekta uzdevums
Projekta mērķis ir ievākt datus no dažādiem interneta iepirkšanās veikaliem (Amazon.de;1a.lv;Ksenukai.lv). Dati tiks ievākti no akciju/atlaižu katalogiem, kurus saglabās pēc LEGO Komplekta ID numura, kurā glabāsies pārējā komplekta informācija (Nosaukums,Cena,Links uz saiti), ko pēc tam izvadīs excel formātā.

## Izmantotās Python bibliotēkas
* request - lai kods būtu spējīgs atvērt interneta saiti un noslasīt tās datus
* BeautifulSoup - nepieciešams lai python kods būtu spējīgs pārtūlkot HTML uz pythona valodā lietojamu kodu
* openpyxl - lai strādātu ar Excel
* u.c. - tiks pievienotas vēlāk, kad tās pievienos 

## Projekta laikā lietotās datu struktūras
HashTable
     
## ko ievacam
Lego komplektu ID, Nosaukums, Cena, Links uz komplektu, ražošanas datums?

## ka tiek uzglabatas 
hashmap no 1alv ksenkuai un amazonde VAI lego

## Lietošanas pamācība
1. atver vaļā
2. nospied starts
3. Pārņem pasauli
4. Atvērsies vaļā excels ar datiem

## Papildus funkcijas kas ir plānošanas stadijā
Ņemt preču cenas bez klienta atlaides un atvēlēt logu ietaupījuma %
Saglabāt nevis csv bet excel failā uzreiz
vispārīga optimizācija(ja būs iespējama)