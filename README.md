# Web Scrapping -- WhoScored.me

Aquest repositori conté codi per a realitzar data scraping a la pàgina web www.whoscored.me mitjançant scripts de Python. Per defecte, el codi genera un fitxer csv amb tots els partits de les lligues Big 5 de la temporada 2022/23 amb estadístiques detallades de cada jornada. 

## Autors
El present repositori ha estat realitzat per Ferran Castel Turégano i David Trepat Segura en el marc de l'assignatura Tipologia i Cicle de Vida de Dades del Màster en Ciència de Dades de la UOC

## Estructura del projecte

El repositori té la següent estructura:

  - `source`: Aquest directori conté el codi font per la descàrrega.
  - `main.py`: conté l’script que acaba executant tot el webscraping
  - `browser.py`: conté el codi necessari per aixecar un browser amb la llibreria Selenium
  - `whoscored_parser.py`: conté el codi necessari per parsejar la web whoscored.com, és a dir per extreure aquells elements que volem.
  - `scraper.py`: conté el codi que fa possible scrapejar la web, a partir dels dos fitxers anteriors. És a dir, conté el codi que navega per la web (a partir de les classes de browser.py) i que extreu les dades (amb funcions que criden les dades al fitxer whoscored_parser.py).
- `dataset`: Aquest directori contindrà el csv generat.
- `requirements.txt`: El fitxer de text amb les llibreries de Python necessàries per aquest projecte.
- `README.md`: L'arxiu actual, que proporciona un resum del projecte.

## Passos per a executar el projecte

Per començar amb el projecte, segueix els següents passos.

0. Webdriver:

És necessari que el lloc des d'on s'executi tingui un navegador instal·lat

1. Clona el repositori a la teva màquina local:

```bash
git clone https://github.com/trepi93/Tipologia-PRA-1.git
```

2. Navega fins al directori del projecte:

```bash
cd Tipologia-PRA-1
```

3. Instala les llibreries necessàries. Es recomana utilitzar un entorn virtual abans de fer-ho:

```bash
pip install -r requirements.txt
```

4. Executa l'scrapping:

 Per executar l'scrapper useu la següent línia de comandes al terminal (per exemple per descarregar les dades de La Liga i la Serie A de la temporada 2023/2024)
   ```bash
    python source/main.py --leagues "LaLiga" "Serie A" --season "2023/2024"
   ```
o per descarregar les dades de La Liga d'un sol any (temporada 2022/2023) podeu fer:

   ```bash
    python source/main.py --leagues "LaLiga" --season "2022/2023"
   ```

   El csv es generarà a la carpeta dataset.

   El dataset que genera el codi tal com està ara es pot consultar a la carpeta dataset del mateix repositori. També hi ha un dataset fictici (per temes de propietat intel·lectual) a Zenodo: https://doi.org/10.5281/zenodo.10120707. El dataset que hi ha conté les estadístiques dels partits de lliga de la temporada 2022-2023 de La Liga, Premier League, Serie A, Bundesliga i Ligue 1. La comanda per descarregar-lo seria:

      ```bash
    python source/main.py --leagues "LaLiga" "Bundesliga" "Serie A" "Ligue 1" "Premier League" --season "2022/2023"
   ```

## Lligues scrapejables

Les lligues descargables es citen a continuació:
-La Liga
-Premier League
-Ligue 1
-Serie A
-Bundesliga
-Liga Portugal
-Super Lig (Turquia)
-Eredivise
-Championship
-Premiership
-2. Bundesliga
-League One
-League Two

Per descarregar altres lligues caldria modificar algun paràmetre per la cerca de temporada o de la fase del campionat que es vol scrapejar.

## Llicència

Aquest conjunt de dades està destinat únicament a fins educatius. Llegir el fitxer de llicència per a més informació.





