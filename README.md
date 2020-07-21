# TR
## Verilen Youtube URL'sindeki videoya ait detayları ve belirli sayıdaki yorumu web sitesi üzerinde gösteren Python Flask ve Selenium scripti  
### Selenium WebDriver ile verilen URL'deki videoya ait detayları Flask web sitesi üzerinde gösteriyor.
------------------


Video'dan Detayları Çekebilmek İçin Kullanılan Xpath'ler
```
Video TAG'leri             =        //yt-formatted-string[@class='super-title style-scope ytd-video-primary-info-renderer']/a
Görüntülenme Sayısı        =        //yt-view-count-renderer/span[@class='view-count style-scope yt-view-count-renderer']
Yayınlanma Tarihi          =        //div[@id='date']/yt-formatted-string
Like ve Dislike Sayısı     =        //ytd-toggle-button-renderer/a/yt-formatted-string[@id='text']
Video Embed Kodu           =        //div[@class='textarea-container fit style-scope iron-autogrow-textarea']/textarea
Yorum Sayısı               =        //div[@id='title']/h2[@id='count']/yt-formatted-string


Yorum Yapan Kişi İsimleri  =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/a/span
Yorum Tarihleri            =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/yt-formatted-string/a
Yorum İçeriği              =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-expander/div/yt-formatted-string[@id='content-text']
Yorumun Beğenilme Sayısı    =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-comment-action-buttons-renderer/div[@id='toolbar']/span[@id='vote-count-left']
```


Yukarıda verilen XPath'lerdeki bilgiyi aldıktan sonra Flask Web Sitesi üzerinde düzenli bir şekilde gösteriyor.



Daha fazlası için [web siteme](https://www.muhammedalikocabey.com/blog) göz atabilirsiniz.

Yardım ve sorularınız için mail adresimden [me@muhammedalikocabey.com](mailto:me@muhammedalikocabey.com) bana ulaşabilirsiniz.







# EN
## Python Flask and Selenium script showing details of the video in the given Youtube URL and a certain number of comments on the website 
### It shows the details of the video in the URL provided with Selenium WebDriver on the Flask website.
------------------


Xpaths Used to Take Details from Video
```
Video TAGs                 =        //yt-formatted-string[@class='super-title style-scope ytd-video-primary-info-renderer']/a
Views                      =        //yt-view-count-renderer/span[@class='view-count style-scope yt-view-count-renderer']
Release date               =        //div[@id='date']/yt-formatted-string
Like and Dislike Count     =        //ytd-toggle-button-renderer/a/yt-formatted-string[@id='text']
Video Embedded Code        =        //div[@class='textarea-container fit style-scope iron-autogrow-textarea']/textarea
Number of Comments         =        //div[@id='title']/h2[@id='count']/yt-formatted-string


Names of Commenters        =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/a/span
Dates of Comment           =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/div[@id='header']/div[@id='header-author']/yt-formatted-string/a
Comment Content            =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-expander/div/yt-formatted-string[@id='content-text']
Comments Like              =        //ytd-comment-renderer/div[@id='body']/div[@id='main']/ytd-comment-action-buttons-renderer/div[@id='toolbar']/span[@id='vote-count-left']
```


After receiving the information in the XPaths given above, it regularly shows on the Flask Website.

You can browse my [website](https://www.muhammedalikocabey.com/blog) for more.

For help and questions, go to my mail address [me@muhammedalikocabey.com](mailto:me@muhammedalikocabey.com) you can contact me.
