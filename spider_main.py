import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getAllImageLink():
    html = urllib2.urlopen('http://sc.chinaz.com/tupian/fengyetupian.html').read()
    soup = BeautifulSoup(html)

    liResult = soup.findAll('div',attrs={"class":"box picblock col3"})
    print len(liResult)

    for li in liResult:
        imageEntityArray = li.findAll('img')
        for image in imageEntityArray:
            link = image.get('src2')
            imageName = image.get('alt')
            filesavepath = '/Users/corolcorona/desktop/picture/%s.jpg' % imageName
            urllib.urlretrieve(link,filesavepath)


if __name__ == '__main__':
    getAllImageLink()
