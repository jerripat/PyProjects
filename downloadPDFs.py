#!/usr/bin/env python


import urllib.request

url=input("Enter Link to Download PDF : ")
Name=input("Enter a Name for the PFD file : ")
FileName = Name+".pdf"
urllib.request.urlretrieve(url, FileName)


