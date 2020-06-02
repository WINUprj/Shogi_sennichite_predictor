from bs4 import BeautifulSoup
import html5lib
import requests
import re

def get_soup(url, content_format):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, content_format)
    return soup

def get_table_rows(soup):
    rows = []
    table = soup.find('table', {'id': 'list'}).find('tbody')
    
    for row in table.find_all('tr'):
        for data in row.find_all('td'):
            rows.append(data.text)
    
    return rows

def get_table_columns(soup):
    col_names = []
    table = soup.find('table', {'id': 'list'}).find('thead').find('tr')

    for tr in table.find_all('th'):
        col_names.append(tr.text)

    return col_names