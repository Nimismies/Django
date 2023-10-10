# Django
Pajan Django -projekti

Projekti on toteutettu Djangolla, pythonilla ja Bootstrap5. 

Käytin virtuaalista ympäristöä: .\venv\Scripts\activate

Koodin voi pyöräyttää käyntiin seuraavalla tavalla, kunhan olet vain oikeassa paikassa eli Django/website kansiossa: python manage.py runserver 

Verkkosivu pyörii osoitteessa: http://127.0.0.1:8000/

Rekisteröitymistiedot tallentuvat MongoAtlas tietokantaan, tällähetkellä sinne ei tallennu mitään muuta

Sivuston toimintoja on etusivu, jossa näkyy sää ja se myös sisältää yksinkertaisen chatbotin, johon voi "hard koodata" vastauksia kysymyksiin. Tähän voisi myös soveltaa AI:ta, mutta katsotaan sitä sitten myöhemmin

Post -lehteä ei näy kirjautumatta/rekisteröitymättä, jos kirjaudut, voit jättää jotain kirjoituksia etusivulle muiden kirjautuneiden nähtäväksi

Login -välilehti on yksiselitteinen eli kirjaudut jo luomillasi tunnuksilla

Create account lehdellä luot tunnukset

Contact lehdellä voit ottaa yhteyttä minuun, menee testi mailiin, tähän ei ole vielä mitään suojausta jotain hyökkäyksiä vastaan

Sivulla on myös dropdown valikko jossa on Home, Login ja Contact näin yksinkertaisuudessaan.

