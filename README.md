# Data Anonymization Tool

## Yleiskatsaus

Tämä työkalu on suunniteltu anonymisoimaan arkaluonteista dataa GDPR-vaatimusten mukaisesti. Se soveltuu erityisesti henkilötietojen, kuten nimien, sähköpostien, puhelinnumeroiden, osoitteiden ja syntymäaikojen, anonymisointiin. Työkalu varmistaa, että data säilyy anonymisoituna ja silti analyysikelpoisena. Se on kehitetty Pythonilla ja noudattaa PEP 8 -koodaustyyliä.

## Käytetyt työkalut

- **Python**: Pääkieli skriptien kirjoittamiseen.
- **Faker**: Synteettisen datan generointiin.
- **Pandas**: Datankäsittelyyn ja analysointiin.
- **Logging**: Tapahtumien lokitukseen.
- **ChatGPT**: Suunnitteluun ja toteutuksen tukemiseen, sekä kehityksen nopeuttamiseen ja dokumentoinnin tuottamiseen.

## Skriptit ja niiden toiminnallisuus

### 1. **generate\_synthetic\_data.py**

- **Tarkoitus**: Generoi synteettistä dataa henkilötiedoilla, kuten nimet, sähköpostit, puhelinnumerot, osoitteet ja syntymäajat.
- **Tulos**: CSV-tiedosto, jossa on 100 tietuetta synteettistä henkilötietoa.

### 2. **anonymize\_data.py**

- **Tarkoitus**: Anonymisoi synteettisen datan GDPR-vaatimusten mukaisesti.
- **Anonymisointimenetelmät**:
  - **Nimet**: Hajautetaan SHA-256\:lla.
  - **Sähköpostit**: Maskataan piilottamalla osa osoitteesta.
  - **Puhelinnumerot**: Maskataan korvaamalla osa numerosta tähdillä.
  - **Osoitteet**: Generalisoidaan kaupunkitasolle.
  - **Syntymäajat**: Generalisoidaan pelkkään vuoteen.
- **Tulos**: CSV-tiedosto, jossa on anonymisoidut tiedot.

### 3. **validate\_anonymization.py**

- **Tarkoitus**: Varmistaa anonymisoinnin onnistuminen ja datan analyysikelpoisuus.
- **Validointiosiot**:
  - **Anonymisoinnin validointi**: Tarkistaa, että kaikki kentät on anonymisoitu oikein.
  - **Data utility -tarkistus**: Arvioi anonymisoidun datan hyödyllisyyttä analytiikkaan.
- **Tulosraportti**: Tallennetaan tiedostoon `3_results/validation_report.txt`.

## Tulosten tulkinta

### Anonymization Validation Results

- **Name\_Anonymized: Passed**: Kaikki nimet on hajautettu onnistuneesti.
- **Email\_Masked: Passed**: Kaikki sähköpostit on maskattu.
- **Phone\_Masked: Passed**: Kaikki puhelinnumerot on maskattu.
- **Address\_Generalized: Passed**: Kaikki osoitteet on yleistetty kaupunkitasolle.
- **Birthdate\_Generalized: Passed**: Kaikki syntymäajat on yleistetty vuositasolle.

### Data Utility Results

- **Record\_Count: 100**: Datassa on odotetut 100 tietuetta.
- **Unique\_Names: 100**: Kaikki nimet ovat uniikkeja, vaikka ne on hajautettu.
- **Unique\_Emails: 86**: Joissakin tapauksissa maskaus on tuottanut samoja tuloksia eri riveille, mutta data säilyy hyödyllisenä. Tämä johtuu siitä, että maskatussa sähköpostissa säilytetään vain kaksi ensimmäistä kirjainta, ja täten saman alkukirjaimen omaavat saavat saman maskatun sähköpostin.

Tulokset osoittavat, että anonymisointi on onnistunut ja data on edelleen analyysikelpoista.

## Lisenssi

Tämä projekti on julkaistu MIT-lisenssillä.
