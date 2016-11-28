
import json
import getPhones as gp
import re
import csv

def getData():
    url = "http://www.gsmarena.com/makers.php3"
    soup = gp.createSoup(url)
    
    data = soup.find("div",{"class":"st-text"})
    
    table = data.findAll("a")
    cmpName=[]
    deviceCount=[]
    
    
    
    for td in table:
        devices =td.find("span").text
        cmp = re.compile(r'\b.*{}.*'.format(devices))
        cmpName.append(str(cmp.match(td.text).group()).replace(devices," "))
        deviceCount.append(devices)
        
    
       
    return (cmpName,deviceCount)
    
def getTopBrand():
    url = "http://www.gsmarena.com/"
    soup = gp.createSoup(url)
    brandName = []
    
    data = soup.find("div",{"class" :"brandmenu-v2 light l-box clearfix" })
    ul = data.findAll("a")
    for li in ul:
        br = li.text.replace("\n","")
        brandName.append(br.lower())
    del(brandName[0])
    del(brandName[37])
    del(brandName[36])
    topPhones = []
    likes=[]
    top10 = soup.find("table",{"class" : "module-fit blue"})
    temp = top10.findAll("th",{"headers":"th3b"})
    for phone in temp:
        topPhones.append(phone.text)
    temp=top10.findAll("td",{"headers":"th3c"})
    for like in temp :
        likes.append(like.text)
    
    createJson(brandName)
    topPhoneLikes = []
    for i in range(len(likes)):
        topPhoneLikes.append((topPhones[i],likes[i]))
        
    of = open("../Data//top10.json","w")
    json.dump(topPhoneLikes,of)
    print("------------------------")
        
    

    
def createCSV():
    brandDevice = getData()
    with open('../Data//Brand.csv', "w" ) as csvfile:
        csvMaker = csv.writer(csvfile , delimiter=' ',
                              quotechar = '\t' , quoting = csv.QUOTE_MINIMAL)
        for i in range(len(brandDevice[0])):
            csvMaker.writerow(brandDevice[0][i] + brandDevice[1][i])
            #csvMaker.writerow(brandDevice[1][i])
            

def createJson(brandName):
    of2 = open('../Data//topBrand.json','w')
    json.dump(brandName,of2)
    
#createCSV()  
#getTopBrand()
