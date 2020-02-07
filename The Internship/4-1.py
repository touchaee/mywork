from bs4 import BeautifulSoup
import requests
path_url = 'https://theinternship.io/'

def get_img(url):
    img = []
    len_company = []
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, features='lxml')
    for image in soup.find_all('img', class_ = 'center-logos'):
        img.append(image.get('src'))
    for i in soup.select('span.list-company'):
        len_company.append(len(i.text))
    sorted_img = [img for _,img in sorted(zip(len_company,img))]
    return sorted_img

if __name__ == "__main__":
    img  = get_img(path_url)
    for i in img:
        print(i)