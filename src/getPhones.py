# -*- coding: utf-8 -*-
import urllib.request as rqst
from bs4 import BeautifulSoup as bs
import json
from collections import OrderedDict
import os

#--------------------------------------------------------
def input2url(searchTxt) :
    #userInput = input("Enter the phone name : ")
    #----------------------
    history = open('../Data//history.csv','a')
    history.write("{}\n".format(searchTxt))
    #creat history
    
    temp = searchTxt.replace(" ","+")
    url = "http://www.gsmarena.com/results.php3?sQuickSearch=yes&sName="+temp
    #converting text to link
    return url
    
#--------------------------------------------------------
    
def createSoup(url):
    #for creating soup of the desirable page
    return (bs(rqst.urlopen(url),"html.parser"))
    
#-------------------------------------------------------- 
    
def getName(soup):
    #extracting data from soup data
    divSrc = soup.find("div",{"class" : "makers"})
    
    getList = divSrc.findAll('li')
    links = []    
    name = []
    images = [] 
    for phoneName in getList:
        if len(name) < 11 :
            #----------------------
            refLink = phoneName.find('a')
            links.append("http://www.gsmarena.com/"+(refLink.get("href")))
            #getting phone Links
            #----------------------
            imgSrc = refLink.find("img")
            images.append(imgSrc.get('src'))
            #getting image links
            #----------------------
            title = phoneName.find('span').text
            #getting phone Names 
            name.append(title)
            #----------------------
        else:
            break
    #-------creating Dict---------
    details=OrderedDict()
    for i in range(len(name)):
#       print(name[i])
        details[name[i]]={'link':links[i],
                         'image':images[i]}
        #if os.path.exists("../images/{}.jpg".format(i)):
         #   os.remove("../images/{}.jpg".format(i))
        path = "../Data//online//images/"
        if  os.path.exists(path):
            
            rqst.urlretrieve(images[i],"../Data//online//images//{}.jpg".format(i))
        else : 
            os.makedirs(path)
            rqst.urlretrieve(images[i],"../Data//online//images//{}.jpg".format(i))
                         
                    
#    print(len(details))
#    print("-----------------------------")
#    print('----------------------------')
#    print(details)
   #--------creating File--------
    path = "../Data//online/"
    if os.path.exists(path):
        
        ofl = open('../Data//online//data.json','w')
        json.dump(details,ofl)
        of2 = open('../Data//online//data2.json','w')
        json.dump(name,of2)
    else:
       os.makedirs(path)
       ofl = open('../Data//online//data.json','w')
       json.dump(details,ofl)
       of2 = open('../Data//online//data2.json','w')
       json.dump(name,of2)
    

#--------------------------------------------------------    
'''    
def main():

    getName()
    print(" -----------DONE------------ ")
    print("-----------------------------")
    #calling function in main()    
            
#--------------------------------------------------------      
    
if __name__ == '__main__' :
    main()

'''