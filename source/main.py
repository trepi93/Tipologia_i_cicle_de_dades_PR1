from browser import Browser
from scraper import WhoScoredScrapper
import argparse

# Arguments per executar l'script passant-li arguments per consola
parser = argparse.ArgumentParser()
parser.add_argument("--leagues", help="Enter array of leagues separated by commas", type=str, nargs='+')
parser.add_argument("--season", help="Enter season in format yyyy/yyyy")
args = parser.parse_args()


# Realitzem el webscraping, servint-nos de la classe WhoScoredScreapper (que és l'scraper pròpiament) i del navegador
# que aixeca la classe browser.
with Browser() as browser:
    print("Comprovem el user agent: ", browser.user_agent)
    scraper = WhoScoredScrapper(browser)

    # Li passem els paràmetres que volem scrapejar. Cal passar-li un array amb les lligues (vegeu Readme per les
    # lligues disponibles) i una temporada.

    scraper.scrape(args.leagues, args.season)
    scraper._data2csv('dataset.csv')
