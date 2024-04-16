# PR24 - Projektna naloga
## ČLANI:
- Matevž Bizjak
-  Nina Kokalj
- Pika Žibert

## PODATKI:
Podatki so bili pridobljeni s spletne strani [zavetišča Horjul](https://www.zavetisce-horjul.net/spet_doma.php).
Podatki o živalih so shranjeni v dveh ločenih CSV datotekah, kjer so primeri povezani preko identifikacijske številke posamezne živali (id). Prva datoteka, 'zivali.csv', vsebuje podatke o živalih, kot so ime, datum sprejema v zavetišče, itd. Druga datoteka, 'veterinarska_oskrba.csv', pa vsebuje podatke o veterinarski oskrbi živali, kot so informacije o sterilizaciji/kastraciji, cepljenju in čipiranju. Datoteki sta povezani z identifikacijsko številko živali.
### zivali.csv:
| Atribut  | Opis |  
| ------------- | ------------- |
| id  | Identifikaciska oz. zaporedna številka živali  |
| ime | Ime živali  |
| datum_sprejema | Datum sprejema živali v zavetišče (x, če manjka)  |
| datum_oddaje | Datum oddaje živali iz zavezišča v večni dom (x, če manjka)  |
| spol | Spol živali - Ženski/Moški  |
| fevfiv | Pozitivnost ali negativnost na FEV ali FIV virus pri mačkah  |
| tip | Maček ali pes  |

### veterinska_oskrba.csv:
| Atribut  | Opis |
| ------------- | ------------- |
| id | Identifikaciska oz. zaporedna številka živali  |
| sterilizirana_kastrirana | Ali je žival sterilizirana oz. kastrirana (0/1) |
| cepljena | Ali je žival cepljena (0/1)  |
| cipirana | Ali je žival čipirana (0/1)  |

## UGOTOVITVE:
Z atributoma datum_sprejema in datum_oddaje smo izračunali število dni, ki jih je posamezna žival preživela v zavetišču. Ugotovili smo, da je povprečno število dni preživetih v zavetišču 125,17825311942958 in narisali graf.

![bar](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/e7c32963-90c0-4a04-9aaa-6eca52d8bf8a)
Iz grafa je vidno, da je večina živali v zavetišču preživela manj kot 300 dni. Imamo pa par zanimiv osamelcev, ki močno odstopajo od ostalih in presegajo celo 1000 dni, kar pomeni, da so bili v zavetišču več let. V povprečju pa žival v zavetišču Horjul biva 4 mesece preden je posvojena.

S pomočjo števila dni preživetih v zavetišču smo narisali tudi histogram:

![histogram](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/2763c35a-d033-4883-a02d-9f563e05eed3)
Histogram potrjuje zgornje ugotovitve. 
V nadaljevanju bomo ugotavljali, kateri dejavniki vplivajo na število dni, ki jih žival preživi v zavetišču Horjul, oziroma na to, kako hitro bo posvojena.


