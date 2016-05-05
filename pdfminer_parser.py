from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from cStringIO import StringIO
from bs4 import BeautifulSoup

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    
    
    str = retstr.getvalue()
    
    
    retstr.close()
    return str




def soupObject():
    # hdr = {'User-Agent':'Mozilla/5.0'}
    # req= urllib2.Request(url,headers=hdr)
    # page=urllib2.urlopen(req)
    soup = BeautifulSoup(open("/home/rahul/pdf-parser/x.html"))
    return soup


if __name__ == '__main__':
    # print convert_pdf_to_txt("SSC_paper_1.pdf")
    print soupObject()
