# PR24 - Končno poročilo za projektno nalogo
## ČLANI:
- Matevž Bizjak
-  Nina Kokalj
- Pika Žibert

## PODATKI:
Podatki so bili pridobljeni s spletne strani [zavetišča Horjul](https://www.zavetisce-horjul.net/spet_doma.php).
Podatki o živalih so shranjeni v treh ločenih CSV datotekah, kjer so primeri povezani preko identifikacijske številke posamezne živali (id). Prva datoteka, 'zivali.csv', vsebuje podatke o živalih, kot so ime, datum sprejema v zavetišče, itd. Druga datoteka, 'veterinarska_oskrba.csv',  vsebuje podatke o veterinarski oskrbi živali, kot so informacije o sterilizaciji/kastraciji, cepljenju in čipiranju. Datoteki sta povezani z identifikacijsko številko živali. Tretja datoteka 'embedded-slike.csv' je bila ustvarjena z uporabo Orangea in funkcije Image Embedding. Ta funkcija izkoristi predhodno naučeno nevronsko mrežo za pretvorbo slik v obsežno matriko števil. Nato smo to matriko uporabili za izvajanje hierarhičnega gručenja. Ključni atributi v tej datoteki vključujejo 'image name', ki se ujema z id-ji v drugih dveh datotekah, ter 'Clusters', kar predstavlja gruče, ki so bile določene za vsako žival.

### zivali.csv:
| Atribut  | Opis |  
| ------------- | ------------- |
| id  | Identifikaciska oz. zaporedna številka živali  |
| ime | Ime živali  |
| datum_sprejema | Datum sprejema živali v zavetišče (x, če manjka)  |
| datum_oddaje | Datum oddaje živali iz zavezišča v večni dom (x, če manjka)  |
| cas_v_zavetiscu | Število dni, ki je žival preživela v zavetišču |
| spol | Spol živali - Ženski/Moški  |
| felvfiv | Pozitivnost ali negativnost na FeLV ali FIV virus pri mačkah  |
| tip | Maček ali pes  |

### veterinarska_oskrba.csv:
| Atribut  | Opis |
| ------------- | ------------- |
| id | Identifikaciska oz. zaporedna številka živali  |
| sterilizirana_kastrirana | Ali je žival sterilizirana oz. kastrirana (0/1) |
| cepljena | Ali je žival cepljena (0/1)  |
| cipirana | Ali je žival čipirana (0/1)  |

### embedded-slike.csv:
| Atribut  | Opis |
| ------------- | ------------- |
| image name | Identifikaciska oz. zaporedna številka živali  |
| Clusters | Gruča, v katero pripada žival |

## UGOTOVITVE:

### Nina statistika:

### Hierarhično gručenje:
Gručenje je bilo izvedeno s pomočjo matrike, dobljene po Image Embedding v Orange. Uporabili smo Wardov povezovalni način, katere cilj je zmanjšati varianco znotraj gruč.
![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151447/f478e55c-20da-419f-b350-3d3f25c46300)

Dobljene gruče smo uporabili, da bi ugotovili kakšno je povprečno število dni, ki jih živali v gruči preživijo v zavetišču. Z drugimi besedami nas je zanimalo, kakšne živali prej najdejo dom in kakšne nanj čakajo dlje časa.

Ugotovili smo, da  črne mačke (gruča C13) največ časa preživijo v zavetišču - v povprečju kar 239,92 dni. Predvidevamo, da ljudje vrjamejo v praznoverje, da črne mačke prinašajo nesrečo.
![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151447/a2d31f95-5f65-4a2f-a804-721e2d4cd227)

Najmanj časa pa preživijo psi, ki nas spominjajo na labradorce (gruča C10) - v povprečju 67,37 dni.
![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151447/977773f5-8e8b-4994-a7cb-7aeec10f2b9b)



### Napoved števila dni:
Želeli smo tudi napovedati število dni, ki jih bodo živali preživele v zavetišču, glede na naslednje atribute:
| Atribut  | Vrednost v matriki |  
| ------------- | ------------- |
| Čas v zavetišču (y) - napovedujemo | Število dni |
| Tip | mačka (0) / pes (1) |
| Spol | moški (0) / ženski (1) |
| Kastriran | ne (0) / da (1) |
| Cepljen | ne (0) / da (1) |
| Čipiran | ne (0) / da (1) |
| Gruča | 0-15 |
Kategorične atribute, ki so bili originalno, na primer tip in spol smo jih prevedli v binarno vrednost 0 ali 1. Veterinska oskrba je bila že pripravljena v obliki one-hot encoding pri pridobivanju podatkov iz spleta, prav tako število dni v zavetišču. Gruče so bile originalno nizi C1-C15, te nize smo preoblikovali v števila, tako da smo odstranili črko 'C' in dobili številke od 1 do 15.
