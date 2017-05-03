import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup

url='http://sc.chinaz.com/tupian/fengyetupian.html'
nextlink=''

def getAllImageLink(url):
    
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)

    liResult = soup.findAll('div',attrs={"class":"box picblock col3"})
    print url
    print len(liResult)

    for li in liResult:
        imageEntityArray = li.findAll('img')
        for image in imageEntityArray:
            link = image.get('src2')
            imageName = image.get('alt')
            filesavepath = '/Users/corolcorona/desktop/picture/%s.jpg' % imageName
                #urllib.urlretrieve(link,filesavepath)
    try:
        nextHtml = soup.findAll('a',attrs={"class":"nextpage"})[0].get('href')
        if nextHtml:
           nextlink='http://sc.chinaz.com/tupian/'+nextHtml
           getAllImageLink(nextlink)

    except Exception,e:
        print '---end---'



if __name__ == '__main__':
    getAllImageLink(url)
