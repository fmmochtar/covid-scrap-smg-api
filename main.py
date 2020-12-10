import uvicorn
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from bs4 import BeautifulSoup
from datetime import datetime, date, time, timezone

import json
import requests
import re
import os
import sys

app = FastAPI()

# Web scrap
scrap_url = 'https://siagacorona.semarangkota.go.id/halaman/covid19'

page = requests.get(scrap_url)
soup = BeautifulSoup(page.text, 'html.parser')
title = soup.title.text

# init and search for some stats
# note: latest web template revision is on 2020-09
stat = soup.find('div',{'class':'container-fluid'}).find('div', {'class':'row'})
s_text = stat.find_all('div', {'class': 'stat-text'})
s_digit = stat.find_all('div', {'class': 'stat-digit color-white' }, {'style': 'font-size:30px'})
s_digit2 = stat.find_all('span', {'style': 'font-size:26px'})

# store the parsed data inside the list
s_digit_parse = []
for k in range(len(s_digit)):
    s_digit_parse.insert(k, re.findall(r'\d+', s_digit[k].text))

kasus_total = []
kasus_total.insert(0, s_digit_parse[1][0])
kasus_total.insert(1, s_digit2[2].text)
kasus_total.insert(2, s_digit2[4].text)
kasus_total.insert(3, s_digit2[6].text)
kasus_total.insert(4, s_digit_parse[3][0])
kasus_total.insert(5, s_digit_parse[5][0])

# Number of cases
n_treatment = [ s_digit_parse[7][0], s_digit2[1].text, s_digit2[2].text ]
n_recovered = [ s_digit_parse[9][0], s_digit2[3].text, s_digit2[4].text ]
n_fatality =  [ s_digit_parse[11][0], s_digit2[5].text ,s_digit2[6].text ]
n_suspect = [ s_digit_parse[3][0] ]
n_probable = [ s_digit_parse[5][0], s_digit2[0].text ]

# rewrite the label
label_kasus = [ 'Total Kasus Terkonfirmasi',
        'Kasus Dirawat (Aktif)',
        'Kasus Sembuh',
        'Kasus Meninggal',
        'Suspek',
        'Probable'
]

treatment_text = ['Kota Semarang', 'Luar Kota', 'Total']
recovered_text = ['Kota Semarang', 'Luar Kota', 'Total']
fatality_text = ['Kota Semarang', 'Luar Kota', 'Total' ]
suspect_text = ['Suspek']
probable_text = ['Total', 'Kematian Probable']

kasus = ['jumlah', 'dirawat', 'sembuh', 'meninggal', 'suspek', 'probable']

d_simple = []
d_treatment = []
d_recovered = []
d_fatality = []
d_suspect = []
d_probable = []

for t_1 in range(len(label_kasus)):
    d_simple.insert(t_1, {'label': label_kasus[t_1], 'jumlah': kasus_total[t_1]})
for t_2 in range(len(n_treatment)):
    d_treatment.insert(t_2, {'label': treatment_text[t_2], 'jumlah': n_treatment[t_2]})
for t_3 in range(len(n_recovered)):
    d_recovered.insert(t_3, {'label': recovered_text[t_3], 'jumlah': n_recovered[t_3]})
for t_4 in range(len(n_fatality)):
    d_fatality.insert(t_4, {'label': fatality_text[t_4], 'jumlah': n_fatality[t_4]})
for t_5 in range(len(n_suspect)):
    d_suspect.insert(t_5, {'label': suspect_text[t_5], 'jumlah': n_suspect[t_5]})
for t_6 in range(len(n_probable)):
    d_probable.insert(t_6, {'label': probable_text[t_6], 'jumlah': n_probable[t_6]})

# API endpoint
@app.get("/")
def home():
    response = RedirectResponse("/docs")
    return response

@app.get("/api")
def get_basic_data():
    return jsonable_encoder(d_simple)

@app.get("/api/dirawat")
def get_treatment_data():
    return jsonable_encoder(d_treatment)

@app.get("/api/sembuh")
def get_recovered_data():
    return jsonable_encoder(d_recovered)

@app.get("/api/meninggal")
def get_fatality_data():
    return jsonable_encoder(d_fatality)

@app.get("/api/suspek")
def get_suspect_data():
    return jsonable_encoder(d_suspect)

@app.get("/api/probable")
def get_probable_data():
    return jsonable_encoder(d_probable)



