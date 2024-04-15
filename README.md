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
