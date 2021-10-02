# Web-scraping web API for COVID-19 Kota Semarang website

[Bahasa Indonesia](https://github.com/fmmochtar/covid-scrap-smg-api) | English

## Description
This web-scraping web API can be used to grab HTML data from COVID-19 web tracker in Semarang [COVID-19 Kota Semarang](https://siagacorona.semarangkota.go.id/halaman/odppdpv2) which shows number of cases of COVID-19 in Semarang. Data taken from the website will be processed and forwarded as an API data that can be (re)used by other web or applications.

This app is written using Python, utilizes **FastAPI** as an API back-end, and **uvicorn** for the ASGI.

## Requirements
- Python 3
- Package dependencies (list included in requirements.txt)

## Installation and first-time use
1. Install the packages needed in the requirements.txt by using the command below.
```
pip3 install -r requirements.txt
```
2. Execute it directly (make sure you have a permission, if it doesn't, run ```chmod +x run.py``` instead), or by typing ```python3 ./run.py``` in the terminal.

## Configuration

Create `.env` file to configure the app. Take a look at `.env.example` for reference.
Default values are written below.

```
host_ip = '127.0.0.1'
host_port = '8000'

duration = 5
```
Values:
```host_ip```: IP address of the server / host.
```host_port```: Port for the service to be used.
```duration```: Service auto-restart time (in minutes).

Notes: in order to expose this service, make sure the ```host_ip``` value is ```0.0.0.0```.

## API Endpoint
API endpoints can be accessed and viewed in ```http://localhost:8000/docs```.

## Caveats
BeautifulSoup4 has no capability to dynamically refresh and reparse the web every time data changes occured. In order to serve the data in nearly real time without spamming HTTP requests to the web that being scraped, I give it a function to restart the server in minutes.
