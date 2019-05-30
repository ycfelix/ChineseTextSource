import json
import requests
from typing import List, Dict

ctp_base = "http://api.ctext.org"


def gettext(urn):
    return ctpapicall("gettext?urn="+urn)


def ctpapicall(querystring):
    response = requests.get(ctp_base+"/"+querystring, cookies=cookies).text
    data = json.loads(response)
    if('error' in data):
        raise Exception('CTP API Error', data['error']['code'], data['error']['description'])
    return data


def produce_urls_list()-> List:
    urls_list = []
    with open("urls.txt", encoding='utf-8') as urls:
        for line in urls:
            start = line.index('<a href="') + 9
            end = line.rindex('"', start)
            urls_list.append(line[start:end])
    return urls_list


def get_text_from_url(url: str)-> Dict:
    return gettext("ctp:"+url)


def get_data_from_urls(urls: List):
    calling = 0
    for url in urls[452:]:
        raw_text = get_text_from_url(url)
        file_title = 'data/' + raw_text['title'] + '.json'
        with open(file_title, "w", encoding='utf-8') as f:
            f.write(json.dumps(raw_text, ensure_ascii=False))
        print("Got " + raw_text['title'])
        calling += 1
        if calling % 50 == 0:
            print("Finished calling " + str(calling))


if __name__ == "__main__":
    global cookies
    cookies = {}
    requests.get("http://api.ctext.org/getstatus", cookies=cookies)
    urls_list = produce_urls_list()
    get_data_from_urls(urls_list)
