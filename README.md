# PowerOutages
This python script scrapes https://www.duquesnelight.com/outages-safety/current-outages for municipalities and customers affected during real-time power outages.
This python script also scrapes data from https://poweroutage.us/, and returns list of electric provider companies in each state along with customer information (customers tracked, customers currently out).

### Prerequisites
* **Scrapy**
* **Scrapy-Splash**
* **Docker**

### Set-up
To run the python script, open terminal and copy paste the following command:
```
docker run -p 8050:8050 scrapinghub/splash
```

Make sure Docker is running beforehand.

### Usage
To run the python script, open an instance of terminal and change the current directory to the following:
```
cd PowerOutages/spiders/
```
For data scraped from https://www.duquesnelight.com/outages-safety/current-outages, copy paste the following command:
```
scrapy crawl current -o ../../feed_exports/current.json
```

For data scraped from https://poweroutage.us/, copy paste the following command:
```
scrapy crawl power -o ../../feed_exports/poweroutages.json
```

The scraped data are stored in feed_exports.
