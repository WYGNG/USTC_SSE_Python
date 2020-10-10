# -*- coding: UTF-8 -*-
# version: 1.1.0 2019.10.22 最新一次PDF下载
from datetime import date

from selenium import webdriver
import os, io
import time
import re
from io import open
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.icis.com/dashboard/reports"
userId = "----------"
password = "-----------"

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd()}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=options)


def download():
    print("登陆中")
    browser.get(URL)
    browser.find_element_by_css_selector("#username-input").send_keys(userId)
    browser.find_element_by_css_selector("#password-input").send_keys(password)
    browser.find_element_by_css_selector("#login-button").click()
    browser.find_element_by_css_selector("#unified_reports_view_main > li:nth-child(2) > a").click()
    time.sleep(5)
    # browser.find_element_by_xpath("//*[@id='unified_reports_view_main']/li[2]/ul[2]/li/div[2]/a[3]").click()
    print("登陆成功")
    print("正在选择文件")
    while 1:
        count = 0
        try:
            time.sleep(1)
            browser.find_element_by_xpath(
                "//*[@id='unified_reports_view_main']/li[2]/ul/li/div[2]/input[@value='PriceReport']/../a[3]").click()
            print("下载文件中")
            break
        except NoSuchElementException:
            if count == 60:
                print("网络环境差或文件不存在")
                return 0
            count += 1
            continue


def switchDownload():
    print("正在设置浏览器")

    def expand_shadow_element(element):
        shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    browser.get("chrome://settings/content/pdfDocuments")
    root1 = browser.find_element_by_css_selector('body > settings-ui')
    shadow_root1 = expand_shadow_element(root1)
    root2 = shadow_root1.find_element_by_css_selector('#main')
    shadow_root2 = expand_shadow_element(root2)
    root31 = shadow_root2.find_element_by_css_selector('settings-basic-page')
    shadow_root31 = expand_shadow_element(root31)
    root3 = shadow_root31.find_element_by_css_selector(
        '#advancedPage > settings-section.expanded > settings-privacy-page')
    shadow_root3 = expand_shadow_element(root3)
    root4 = shadow_root3.find_element_by_css_selector('#pages > settings-subpage > settings-pdf-documents')
    shadow_root4 = expand_shadow_element(root4)
    shadow_root4.find_element_by_css_selector('#toggle').click()


def readPdf(path):
    print("下载成功：" + path)
    print("正在读取文件")
    codec = 'utf-8'
    filePath = path
    manager = PDFResourceManager()
    output = io.StringIO()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    with open(filePath, 'rb') as infile:
        for page in PDFPage.get_pages(infile, check_extractable=True):
            interpreter.process_page(page)
            convertedPDF = output.getvalue()
    output.close()
    converter.close()
    return convertedPDF


def getName():
    fileName_list = os.listdir(os.getcwd())
    for item in fileName_list:
        if re.match(".*pdf$", item):
            return item


def parse(text, fileName):
    info = re.search(".PP BOPP Film.*CFR China Import(.*)", text, re.M | re.S)
    bopp_infos = info.group(1)
    bopp_infos_box = bopp_infos.split("\n")
    bopp_infos_box = [i for i in bopp_infos_box if i != '' and i != ' ' and i != 'Price Range' and i !="\xa0" and i !="USD/tonne"]
    bopp_infos_box = [i for i in bopp_infos_box if len(i) < 15]
    #print(bopp_infos_box)

    fileTime = re.match(".*\) (.*)\.pdf", fileName).group(1)

    infom = {
        "date": fileTime,
        "trend1": str(bopp_infos_box[0]),
        "priceRange": bopp_infos_box[1],
        "trend2": str(bopp_infos_box[2])
    }

    return infom


def deleteFile(fileName):
    os.remove(fileName)


def closeBrowse():
    browser.quit()


def save(info):
    pass


if __name__ == '__main__':
    switchDownload()
    download()
    while 1:
        try:
            fileName = getName()
            text = readPdf(fileName)
            break
        except:
            continue
    # print(text)
    info = parse(text, fileName)
    print(info)
    save(info)
    deleteFile(fileName)
    closeBrowse()
