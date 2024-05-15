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

### Osnovne statistike:
Nad podatki smo izvedli nekaj osnovne statistike.  V datoteki zivali.csv je zabeleženih 626 živali, med njimi pa je 222 mačk in 404 psov. Narisali smo histogram preživetih dni v zavetišču za mačke ter histogram preživetih dni v zavetišču za pse in ugotovili, da mačke povprečno v zavetišču preživijo 186 dni in psi povprečno 93 dni, torej mačke na posvojitev čakajo še enkrat toliko kot psi. Narisali smo tudi skupen histogram preživetih dni v zavetišču.
![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/16274ed8-fb4f-4ec1-9dac-602c86b9bacd)
Povprečno število dni preživetih v zavetiču: 125
Najmanjše število dni preživetih v zavetišču: 7
Največje število dni preživetih v zavetišču: 2170
V histogramu se je pokazalo par osamelcev. Obstajajo živali, ki so na posvojitev čakale več kot 1000 dni, torej 3 leta in več.
Največ časa je na posvijtev čakala psička Gumbka in to 2170 dni, kar je skoraj 6 let.
![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/6d6a9de5-30d7-4134-a39b-b885f55c77e4)


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

Kategorične atribute, ki so bili originalno, na primer tip in spol smo prevedli v binarno vrednost 0 ali 1. Veterinska oskrba je bila že pripravljena v obliki one-hot encoding pri pridobivanju podatkov iz spleta. število dni v zavetišču je bilo prav tako zračunano pri pridobivanju podatkov iz spleta. Gruče so bile originalno nizi C1-C15, te nize smo preoblikovali v števila, tako da smo odstranili črko 'C' in dobili številke od 1 do 15.


Iz teh pretvorb je nastala matrika, ki smo jo uporabili za učenje modela za napovedovanje števila dni v zavetišču. Pri izbiri modelov smo se odločili uporabiti linearno regresijo in ansamble z metodo naključnega gozda (Random Forest). Linearno regresijo smo izbrali, ker je preprosta in enostavna za razumevanje ter lahko zajame linearno povezavo med atributi in ciljno spremenljivko. Za bolj kompleksne odnose med atributi in ciljno spremenljivko pa smo uporabili ansambelski model naključnega gozda.

Pri linearni regresiji smo dobili MAE 68.66 dni, torej se model v povprečju zmoti za približno 69 dni. Ko smo ga preizkusili na živali, ki še ni posvojena je model napovedal 196.55 dni do posvojitve, v resnici pa je maček že 211 dni v zavetišču, torej več kot je bilo predvideno.

Pri ansamblih pa smo dobili MAE 60.76 dni, kar je nekoliko bolje kot pri linearni regresiji. Za isti primer je napovedal 333 dni, torej naj bi ta maček našel svoj dom čez 122 dni. 
