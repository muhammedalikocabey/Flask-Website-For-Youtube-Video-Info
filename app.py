# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:53:09 2020

@author: muham
"""


# -*- coding: utf-8 -*-
"""

@author: Muhammed Ali KOCABEY
08.01.2020
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import locale 
import time 
import re

def remove_html(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return  TAG_RE.sub('', text)



def videoBilgileriniGetir(video_url):
    
    #       Browser ve Web Sitesini Aç 
    driver_path = "chromedriver.exe"
    locale.setlocale(locale.LC_ALL, "tr")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=tr')
    
    browser = webdriver.Chrome(executable_path=driver_path, options = options)
    del driver_path
    
    browser.maximize_window()
    
    browser.implicitly_wait(5)
    
    browser.get(video_url)
    timeout = 5
    
    try: 
        element_present = EC.presence_of_element_located((By.ID, 'primary'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        pass
        
    ########################################################################################################
    
    video_tagleri_elements = browser.find_elements_by_xpath("//yt-formatted-string[@class='super-title style-scope ytd-video-primary-info-renderer']/a")
    
    video_tagleri = list()
    
    for tag in video_tagleri_elements:
        tag_inner = tag.get_attribute("innerHTML")
        tag_href = tag.get_attribute("href")
        video_tagleri.append([tag_inner, tag_href])
        
    del video_tagleri_elements
    
    
    vid_name = browser.find_element_by_xpath("//h1[@class='title style-scope ytd-video-primary-info-renderer']/yt-formatted-string").get_attribute("innerHTML")
    
    
    goruntulenme_sayisi = browser.find_element_by_xpath("//yt-view-count-renderer/span[@class='view-count style-scope yt-view-count-renderer']").get_attribute("innerHTML").split()[0]
    
    
    yayinlanma_tarihi = browser.find_element_by_xpath("//div[@id='date']/yt-formatted-string").get_attribute("innerHTML")
    
    
    
    like_and_dislike = list()
    
    like_and_dislike_elements = browser.find_elements_by_xpath("//ytd-toggle-button-renderer/a/yt-formatted-string[@id='text']")
                                         # //div[@id='top-level-buttons']/ytd-toggle-button-renderer/a/yt-formatted-string")
    
    for i in like_and_dislike_elements:
        like_and_dislike.append(i.get_attribute("aria-label"))
        
    video_like = like_and_dislike[0].split()[0]
    video_dislike = like_and_dislike[1].split()[0]
    
    del like_and_dislike
    
    time.sleep(1)

    paylas_butonu = browser.find_element_by_xpath("//div[@id='top-level-buttons']/ytd-button-renderer[@class='style-scope ytd-menu-renderer force-icon-button style-default size-default'][1]")
    paylas_butonu.click()
    
    time.sleep(1)
    
    
    
    yerlestir_butonu = browser.find_element_by_xpath("//yt-share-target-renderer/button[@id='target']/div[@id='title' and text()='Yerleştir']")
    yerlestir_butonu.click()
    
    time.sleep(1)
    
    embed_kod = browser.find_element_by_xpath("//div[@class='textarea-container fit style-scope iron-autogrow-textarea']/textarea").get_attribute("value")

    soup = BeautifulSoup(embed_kod, 'html.parser')
    embed_src = soup.find("iframe")
    embed_kod = embed_src["src"]

    embed_kapat_buton = browser.find_element_by_xpath("//div[@id='title-bar']/yt-icon")
    embed_kapat_buton.click()


    browser.execute_script("window.scrollTo(0, 500)") 
    time.sleep(2)
    
    
    try: 
        element_present = EC.presence_of_element_located((By.ID, 'count'))
        WebDriverWait(browser, 6).until(element_present)
    except TimeoutException:
        pass
    
    
    yorum_sayisi = browser.find_element_by_xpath("//div[@id='title']/h2[@id='count']/yt-formatted-string").get_attribute("innerHTML").split()[0]
    
    
    browser.execute_script("window.scrollTo(0, 1200)") 
    
    
    
    all_comments = list()
    
    
    kisi_adlari_elements = browser.find_elements_by_xpath("//ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/a/span")
    yorum_tarihi_elements = browser.find_elements_by_xpath("//ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/yt-formatted-string/a")
    yorum_icerik_elements = browser.find_elements_by_xpath("//ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-expander/div/yt-formatted-string[@id='content-text']")
    yorum_liked_elements = browser.find_elements_by_xpath ("//ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-comment-action-buttons-renderer/div[@id='toolbar']/span[@id='vote-count-left']")
    
    
    for i in range(len(kisi_adlari_elements)):
        kisi_ad = kisi_adlari_elements[i].get_attribute("innerHTML").strip()
        tarih = yorum_tarihi_elements[i].get_attribute("innerHTML").strip()
        yorum = remove_html(yorum_icerik_elements[i].get_attribute("innerHTML")).strip()
        like = yorum_liked_elements[i].get_attribute("aria-label").strip()
        all_comments.append([kisi_ad, tarih, yorum, like])
    
    
    video_Bilgileri = [embed_kod, vid_name, video_url, video_tagleri, goruntulenme_sayisi, 
                       yayinlanma_tarihi, video_like, video_dislike, yorum_sayisi, all_comments]
    
    return video_Bilgileri


# a = videoBilgileriniGetir("https://www.youtube.com/watch?v=tiEt1qkaaGA")



#%%

from flask import Flask, Markup, render_template, redirect, url_for, request


    
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        pass

    else:
        return render_template("index.html")

@app.route("/video", methods=["POST", "GET"])
def video_page():
    if request.method == "POST":
        video_url = request.form.get("youtube_url")
        
        if len(video_url) < 5:
            hata = "Lütfen URL'yi Doğru Giriniz..."
            return render_template("index.html", hata=hata)
        
        
        video_bilgileri = videoBilgileriniGetir(video_url)
        
        return render_template("video.html", video_bilgileri=video_bilgileri)
    else:
        return redirect(url_for("home"))
    
    
@app.errorhandler(500)
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()













































