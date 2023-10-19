from autoscraper import AutoScraper

url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = [""]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)