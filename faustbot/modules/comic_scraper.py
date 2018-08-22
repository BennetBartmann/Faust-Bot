import random

import requests


# Comic scraper scrapes comics from urls that have no website based random functionality. Comic URLs have to be
# in comics.py
class ComicScraper(object):

    # Scrapers for specific websites follow here:

    # scraper for Betamonkeys
    @staticmethod
    def scrape_betamonkeys(url):
        # get latest comic id from the website, then generate a random number within the range of 1 and the latest c
        # omic.
        # Finally generate a new comic url from that. I know this is dirty - But it works for a comic i guess ;)
        r = requests.get(url)
        comic_id_latest = \
            r.content.decode("utf-8").split("http://betamonkeys.co.uk/wp-content/stripshow_comics/betamonkeys")[
                1].split(
                ".png")[0]
        random_comic_number = str(random.randint(1, int(comic_id_latest)))
        random_comic_url = "http://betamonkeys.co.uk/wp-content/stripshow_comics/betamonkeys" + random_comic_number + ".png"
        return random_comic_url + " Betamonkeys " + random_comic_number + " | Betamonkeys"

    # scraper for Nichtlustig
    @staticmethod
    def scrape_nichtlustig():
        # TODO: Write a scraper for Nichtlustig!
        return "Bisher kein Scraper für Nichtlustig."

    # your custom scraper here
    # def scrapeYourCustomComic(url):
    # return "Your custom scraped URL"

    # Main scraping function. Takes url, decides scraping method to use. If no scraping method is found: return "No pa
    # rser found"
    @staticmethod
    def get_random_comic(url):
        if "betamonkeys.co.uk" in url:
            return ComicScraper.scrape_betamonkeys(url)

        if "nichtlustig.de" in url:
            return ComicScraper.scrape_nichtlustig()

        else:
            return "No parser found for comic URL: " + url
