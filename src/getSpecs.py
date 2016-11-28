# -*- coding: utf-8 -*-
import urllib.request as rqst #for requesting web page
from bs4 import BeautifulSoup as bs  #for html parsing
import re  #for Regex
import json #For reading json file
#--------------------------------------------
def getURL ():
    #----Getting URL of the selected Phone----
    with open('../Data/online//data.json') as f:
        details = json.loads(f.read())
        return details
        
def getPhoneName():
    with open("../Data/online//name.json") as f :
        nameList = json.loads(f.read())
    
        return nameList
        

#-----------Creating Soup----------------
def createSoup():
    
    details = getURL()
    phoneName = getPhoneName()
    #print(getPhoneName())
    #print(type(phoneName[0]))
    url = details[phoneName[0]]
    return(bs(rqst.urlopen(url["link"]),"html.parser")),url["link"]
        
#--------Extrecting Data From Soup------------------
def getSpec():
    data = createSoup()
    soupData = data[0]
        #------regex for finding css class name------ 
    compileStat = re.compile(r'\bhelp.*accented\shelp-.*')
    feature = compileStat.findall(str(data[0]))
    formatedClasses= [i[:-2] for i in feature]
        
        
    #--------------------------
    basicFeature = soupData.find("div",{"class":"center-stage light nobg specs-accent"})
    basicDetail=[]
        #--------------------------
    for spec in basicFeature.findAll("span",{"class":"specs-brief-accent"}): 
        basicDetail.append(spec.text)
        #--------------------------    
    for formatedClass in formatedClasses :
        tempClass = soupData.find('li',{'class' : formatedClass}).text
        tempClass = (tempClass.replace('\n',"").strip())
        tempClass = tempClass.replace("\r","").strip()
        basicDetail.append(tempClass.replace("       "," ").strip())
        #--------------------------
    searchesSoup = soupData.find("li" ,{"class":"light pattern help help-popularity"})
    searchesPer = searchesSoup.find("strong",{"class":"accent"}).text
    searches = searchesSoup.find("span").text
        
        
    likesSoup = soupData.find("li" ,{"class":"light pattern help help-fans"})
    likes = likesSoup.find("strong",{"class":"accent"}).text
    basicDetail.append(searches)
    basicDetail.append(searchesPer)
    basicDetail.append(likes)
    basicDetail.append(data[1])
    #print(basicDetail)
    return basicDetail

#-----------Calling in main method-------------------
'''
def main():
    a = getSpec() 
    print(a[1][1])
      
    
#--------------------------------------------  
  
if __name__ == "__main__" : 
    main()
'''
