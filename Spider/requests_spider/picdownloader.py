#-*-coding:utf8-*-
import urlparse
import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


# f = open('source.txt','r')
# html = f.read()
# f.close()
# print html
url = "https://otc.cbex.com/page/s/search/index"
# url = 'https://www.crowdfunder.com/browse/deals'
html = requests.get(url).text
# print html

    # <div class="bdlist_img"><a href="/prj/detail/2178.html" target="_blank">
    # <img src="/editorUpload/image/2016/02/IMIMG-2016020023-3811/1456126240016039194-logo.jpg_MzAwLDMwMA==.jpg"/> </a>
urls_field = re.findall('<div class="bdlist_img">(.*?)</a>',html,re.S)
pic_urls = []
for field in urls_field:
    pic_url = re.findall('<img src="(.*?)"/>',field,re.S)
    # new_full_url = urlparse.urljoin("https://otc.cbex.com",pic_url[0])
    # print pic_url
    pic_urls.append(pic_url)
print pic_urls
i = 0
for each in pic_urls:
    new_full_url = urlparse.urljoin("https://otc.cbex.com",each[0])
    print "now downloading:" + str(i)
    pic = requests.get(new_full_url)
    fp = open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1



# class PicDownLoader(object):
#     def getpictures(self, url):
#         html = requests.get(url)
#         html.encoding = 'utf-8'
#         print html.text



# if __name__ =="__main__":
# 	url = "https://otc.cbex.com/page/s/search/index"
# 	pic_downloader = PicDownLoader()
# 	pic_downloader.getpictures(url)
