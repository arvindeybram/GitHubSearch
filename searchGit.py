import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")


def traversePage(tagName):
    global outputFile
    newIndex = 0
    linkList = []
    for a in tagName:
        link = a.get_attribute('href')
        if "#L" in link:
            splits = link.split("#L")
            if (splits[-1]).isdigit():
                if splits[0] not in linkList:
                    linkList.append(splits[0])
                newIndex += 1
    with open(outputFile, 'a') as filePointer:
        for eachLink in linkList:
            filePointer.write(str(eachLink) + '\n')

    return newIndex


def processURL(url_1):
    initIndex = 1
    while True:
        browser = webdriver.Chrome(chromedriver, options=options)
        browser.get(url_1.format(PAGENUMBER=initIndex))
        time.sleep(5)
        print(url_1.format(PAGENUMBER=initIndex))
        aTagsInLi = browser.find_elements_by_css_selector('a')
        totalLinksPerPage = traversePage(aTagsInLi)
        print(totalLinksPerPage)
        if totalLinksPerPage == 0:
            break
        initIndex += 1
        browser.close()
    browser.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-if", "--input_file", required=True, type=str, help='Input File Name')
    parser.add_argument("-of", "--output_file", required=True, type=str, help='Output File Name')
    parser.add_argument("-d", "--driver_path", required=True, type=str, help='Complete path to chromedriver')
    parser.add_argument("-s", "--search", required=True, type=str, help='Keyword to search')
    args = parser.parse_args()

    keyword = args.search
    payload = '/search?p={PAGENUMBER}&q=' + keyword + '&type=code'
    inputFile = args.input_file
    outputFile = args.output_file
    chromedriver = args.driver_path

    with open(inputFile, 'r') as f:
        for each_url in f.readlines():
            url1 = each_url.strip() + payload
            processURL(url1)
