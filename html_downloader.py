import urllib2

class HtmlDownloader(object):

      def download(self,url):
          if url is none:
             return none
          response=urllib2.urlopen(url)

          if response.getcode!=200:
             return none
          return response.read()
