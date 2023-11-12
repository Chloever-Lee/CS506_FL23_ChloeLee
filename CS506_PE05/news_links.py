import requests
import bs4
import openpyxl  
from openpyxl import Workbook


res = requests.get('https://news.ycombinator.com/news')
try:
    res.raise_for_status()
    #print("Status Code: ", res.status_code) #expeting 200
    #print("Length of the text: ", len(res.text))
except Exception as exc:
    print("%s" %(exc))

soup = bs4.BeautifulSoup(res.text, "html.parser")
#store list of all <td.title> <span.titleline> tags to element 
element = soup.select("span.titleline")
#find all tr, athing may have href with http addresses
links = soup.findAll('tr',class_='athing')
f = open("News_link.txt", "w")
f.writelines("\nThis is text file for News- Title & Url\n")
#for loop to iterate each elements 
for el in element:
    title= el.get_text() #titleline would be display w/o tag
    
    for link in links:
        url = link.find_all('td')[2].a['href']  #to extract http address w/href 
        f.write(title)
        f.write("\n")
        f.write(url)
        f.write('\n')
    print(title +"\n"+url)
    print("\n")
#closing text file
f.close()
  

    

    
     







    

        

           
            
        
      







    













    











