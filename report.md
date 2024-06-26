# PR24 - Končno poročilo za projektno nalogo
## ČLANI:
- Matevž Bizjak
-  Nina Kokalj
- Pika Žibert

## PODATKI:
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

## PRIDOBIVANJE PODATKOV:
Podatki so bili pridobljeni s spletne strani [zavetišča Horjul](https://www.zavetisce-horjul.net/spet_doma.php).
Za pridobivanje podatkov smo uporabljali Python skripto. Uporabljali smo knjižnico Requests, da smo pridobili html strukturo spletne strani, ter knjižnico BeautifulSoup za parsanje pridobljenih datotek. Podatke smo na koncu zapisali v .csv datoteko. Edini podatek na spletni strani katerega nismo uspešno pridbili je bila starost ob sprejemu. To se nam je sicer zdel zelo pomember podatek, ampak je bil na spletni strani podan za vsako žival ročno in po večini vedno v drugačnem formatu. Imeli smo tudi nekaj manjkajočioh podatkov katere smo pa kasneje samo ignorirali ter izbrisali, saj je v večini primerov šlo za žival skupaj z mladiči, oziroma za leglo mladičev.
Spletna stran je dokaj zastarela, tako da z kakršnokoli zaščito pred roboti nismo imeli problemov. Niso imeli tudi nikakršne captche oziroma blokade v primeru preveč zahtevkov, tako da smo uspeli pridobiti vse podatke iz strani iz enega računalnika samo z uporabo niti in brez proxy-jev v samo parih minutah.

## UGOTOVITVE:

### Osnovne statistike:
Nad podatki smo izvedli nekaj osnovne statistike.  V datoteki zivali.csv je zabeleženih 626 živali, med njimi pa je 222 mačk in 404 psov. Narisali smo histogram preživetih dni v zavetišču za mačke ter histogram preživetih dni v zavetišču za pse in ugotovili, da mačke povprečno v zavetišču preživijo 186 dni in psi povprečno 93 dni, torej mačke na posvojitev čakajo še enkrat toliko kot psi. Narisali smo tudi skupen histogram preživetih dni v zavetišču.

![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/16274ed8-fb4f-4ec1-9dac-602c86b9bacd)
Povprečno število dni preživetih v zavetiču: 125

Najmanjše število dni preživetih v zavetišču: 7

Največje število dni preživetih v zavetišču: 2170

V histogramu se je pokazalo par osamelcev. Obstajajo živali, ki so na posvojitev čakale več kot 1000 dni, torej 3 leta in več.
Največ časa je na posvojitev čakala psička Gumbka in to 2170 dni, kar je skoraj 6 let, a je na koncu vseeno našla dom:)

![gumbka02](https://github.com/matevzb03/PR24MBPZNK/assets/67975101/7415d721-fa33-42e4-b398-044d729185c0)

Psička Gumbka

Ugotavljali smo tudi, ali histogram preživetih dni v zavetišču spominja na katero od znanih porazdelitev. 

![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/5648bcfa-0e99-4bea-8ce6-0065cf18f8b6)

Najprej smo izračunali osnovne statistične parametre, kot so povprečje in nepristranska ocena variance. Potem smo ocenili tri različne verjetnostne porazdelitve - Gaussovo, Studentovo t- in beta-porazdelitev - ter njihove gostote verjetnosti prikazali na histogramu, ki prikazuje porazdelitev preživetih dni v zavetišču. Ta analiza nam omogoča boljše razumevanje časa živali v zavetišču in primerjavo med različnimi verjetnostnimi modeli. Ugotovili smo, da se naša porazdelitev najbolj ujema s Studentovo porazdelitvijo.

### Sezonska nihanja pri sprejemu in oddaji živali:
Analizirali smo datume sprejema v zavetišče in datume oddaje iz zavetišča. Prešteli smo število živali sprejetih v zavetišče na mesec in število živali oddanih iz zavetišča na mesec ter izrisali oba grafa.

![bl](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/e9cf59af-7a26-4845-b51f-af16f92b5bc5)

Iz grafov je lepo razvidno, da sta v večini mesecev obratno sorazmerna. To se da lepo videti v poletnih mesecih, kjer je število sprejetih živali največje in število oddanih najmanjše. Rezultat je logičen, saj ljudje odhajajo na dopuste in nimajo časa v družino uvajati novih družinskih članov. Oddaja živali se poveča že septembra, ko se zopet začneta šola in služba. Največ živali je oddanih od novembra do marca (z izjemo decembra). Sklepamo, da je to zato, ker takrat ljudje več časa preživijo v svojih domovih in si zaželijo družbe hišnega ljubljenčka. Čas praznikov ter hladna in temna zima lahko povzročita porast osamljenosti in depresije, morda se zato nekateri odločijo za bližino živali.

Oddajo živali smo analizirali tudi za vsak mesec vsakega leta. Zaradi boljše berljivost je na x-osi označen le januar vsakega leta.

![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/61c21bdb-9928-4b6b-8e36-b66097cb0063)

Največja porasta oddaje živali sta v januarju 2019 in januarju 2022. Porast leta 2019 ne znamo pojasniti, januar 2022 pa se nam je zdel bolj zanimiv. Takrat se je Slovenija spopadala s pandemijo COVID-19. Država je v tem mesecu zabeležila rekordno število novih primerov. Morda so se zaradi teh težkih časov ljudje zatekli k muckom in kužkom:)

### Veterinarska oskrba:
Zanimala nas je veterinarska oskrba živali v zavetišču Horjul. Z analizo datoteke "veterinarska_oskrba.csv" smo preštevali število primerov z določeno oskrbo. Atributi primera so kastracija/sterilizacija, cepljenje in čipiranje. Vrednost 1 označuje, da je primer oskrbljen, medtem ko vrednost 0 pomeni, da ni.

Nad veterinarsko oskrbo smo prijetno presenečeni. Ugotovili smo, da zavetišče večino svojih živali oskrbi v celoti ali pa jim ne nudi oskrbe v ničemer. Le nekaj živali je le delno oskrbljenih. Spodnji izpis prikazuje podrobno število živali glede na vrsto oskrbe.

![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/21f61013-4f80-427c-9100-7601dfc29f14)

Nato pa smo še narisali histogram, kjer kategorija polna oskrba tvorijo živali, ki so prejele vse od treh prej omenjenih oskrb, delna oskeba so živali, ki jim manjka vsaj ena od treh oskrb in brez oskrbe so živali, ki jim manjkajo vse tri oskrbe.

![image](https://github.com/matevzb03/PR24MBPZNK/assets/162151394/45b1ec34-7bb6-496f-985a-b9c40baa436f)



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
