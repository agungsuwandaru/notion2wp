
import sys
import re
from pip._vendor import requests
from selenium import webdriver
import time

#usage: notion2wp-v2.py notion-url output-file
def getNotionContent(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(10)
    element_body = browser.find_element_by_class_name('notion-body')
    html_body = element_body.get_attribute('innerHTML')
    element_toc = browser.find_element_by_class_name('notion-table_of_contents-block')
    html_toc = element_toc.get_attribute('innerHTML')
    browser.close()
    return [html_body, html_toc]


# get content of img src and add domain address
def getImageUrl(notionFileContent):
    i = 0
    urls = re.findall(r'img src="/image[\w%/&;\-\.?=]+', notionFileContent)
    for url in urls:
        url = "https://notion.so" + url[9:]
        url = url.replace(';', '&')
        urls[i] = url
        i += 1
    return urls


# get html of potion-api
def getPotionContent(url):
    notion_id = re.findall(r'\w+', url)[-1]
    return requests.get('https://potion-api.now.sh/html?id=' + notion_id).text


def mixNotionUrlsToPotion(potion_content, urls):
    i = 0
    urls_potion = re.findall(r'img src="[\w:\%\/\&\;\-\.\?\=\(\)]+', potion_content)
    for url_potion in urls_potion:
        potion_content = potion_content.replace(url_potion, "img src=\"" + urls[i])
        i += 1
    return potion_content


#insert id selector into <h1>, <h2>, <h3>
def insertIdSelector(potion_content):
    i = 1
    headings_potion = re.findall(r'<h[123]>', potion_content)
    #print(headings_potion)
    for heading_potion in headings_potion:
        pattern = re.compile('<h[123]>')
        where = [m for m in pattern.finditer(potion_content)][0]
        before = potion_content[:where.start()]
        after = potion_content[where.end():]
        potion_content = before + heading_potion[:3] + ' id="' + str(i) + '">' + after
        i += 1
    return potion_content


#insert ID to "a href" on the TOC, e.g. <a href="#1">
def inserIdSelectorToLink(notion_content):
    i = 1
    urls = re.findall(r'a href="/[\w%/&;#\-\.?=]+', notion_content)
    for url in urls:
        notion_content = notion_content.replace(url, "a href=\"#" + str(i))
        i += 1
    return notion_content


notion_url = sys.argv[1]
result_file = sys.argv[2]
streamWrite = open(result_file, 'w')
notion_content = getNotionContent(notion_url)
body_content = notion_content[0]
toc_content = notion_content[1]
urls = getImageUrl(body_content)
potion_content = getPotionContent(notion_url)
body_content = mixNotionUrlsToPotion(potion_content, urls)
body_content = insertIdSelector(body_content)
toc_content = inserIdSelectorToLink(toc_content)


streamWrite.write(toc_content + '<p>' + body_content)
