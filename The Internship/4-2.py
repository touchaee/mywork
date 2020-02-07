from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/companies', methods = ['GET'])
def get_img():
    url = 'https://theinternship.io/'
    img = []
    len_company = []
    list_logo = []
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    for image in soup.find_all('img', class_ = 'center-logos'):
        img.append(url + image.get('src'))
    for i in soup.select('span.list-company'):
        len_company.append(len(i.text))
    sorted_img = [img for _,img in sorted(zip(len_company,img))]
    for i in sorted_img:
        logo = {}
        logo['logo'] = i
        list_logo.append(logo)
    json = {'companies' : list_logo}
    return json

if __name__ == "__main__":
    app.run(debug = True)