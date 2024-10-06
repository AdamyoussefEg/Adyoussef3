#مشروع اختصار الروابط
from pystyle import *
import pyshorteners as short
print(Box.Lines(" [+] Learn python with Adam [+] "))
Write.Print(" [+] This program for short url.  \n",Colors.blue_to_red,interval=0.1)
print(Box.DoubleCube("Example [4]"))

url = Write.Input(" [-] Write url for short :",Colors.yellow_to_red,interval=0.1)
ch=short.Shortener()
Write.Print(ch.tinyurl.short(url),Colors.green_to_white,interval=0.1)
input("\n press any key to exit ... ")
