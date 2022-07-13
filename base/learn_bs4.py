import requests
from bs4 import BeautifulSoup


def get_html_content(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    return resp.text


if __name__ == '__main__':
    domain = 'https://www.umei.cc'
    main_path = '/weimeitupian/'

    content = get_html_content(domain + main_path)
    parser = BeautifulSoup(content, "html.parser")
    pic_box = parser.find_all('div', attrs={'class': 'pic-box'})
    for box in pic_box:
        ul_list = box.find_all('ul', attrs={'class': 'pic-list after'})
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                href = a.get('href')
                a_context = get_html_content(domain + href)
                a_parser = BeautifulSoup(a_context, 'html.parser')
                section = a_parser.find('section', attrs={'class': 'img-content'})
                finded_img = section.find('img')
                hd_image_src = finded_img.get('src')
                print(hd_image_src)

