from Utils.extracthtml import getHtml
import pandas as pd
flipUrl = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=13e12f8b-622f-4904-a064-f16e6888a650&sort=relevance"

flipHeader ={
    
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.6778.139\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.139\", \"Chromium\";v=\"131.0.6778.139\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=cm3x5zu4y3qaa1qeom0k83ida-BR1732547411026; K-ACTION=null; vh=730; vw=1536; dpr=1.25; rt=null; ud=7.ob55YpFv-Bf3TXHcfJwTmBPiRuVe7uR_JgXVvbK6i1-OzGF3cBoqFw6gZKHHyEszvGM8GnX-XCMvOrTosYHmWvcM1JyrAXfT4OfF5_NZkEvzcd3VEL3VZ7KxQNaCcaS1lASprBW470hJ_7ZXiXQsAqVlB7K0ysQO9e2ToL-TsaVWjk88gsvMoGnTls90eTmsjtzYOA8TfTLtwpJhByBR8A; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MzU2NjgzNzIsImlhdCI6MTczMzk0MDM3MiwiaXNzIjoia2V2bGFyIiwianRpIjoiYmNkNDhjZGMtMjI4My00MjY4LTllOWYtNjlmNTQ3YjRkODE0IiwidHlwZSI6IkFUIiwiZElkIjoiY20zeDV6dTR5M3FhYTFxZW9tMGs4M2lkYS1CUjE3MzI1NDc0MTEwMjYiLCJrZXZJZCI6IlZJMzVDQTcyOEQ2RDUxNDU5NEExOTEwQzcwRUExQkI2QzkiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.PFXC7yHOCOM1kyWIkQ0j4_Sj89noUd0N39k3ATKfrOE; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20069%7CMCMID%7C53934907183238735101830679465564080614%7CMCAAMLH-1734545174%7C12%7CMCAAMB-1734545174%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1733947574s%7CNONE%7CMCAID%7CNONE; qH=312f91285e048e09; Network-Type=4g; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Alaptops-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; S=d1t14Xz8/P0FdPz8/Pz97P1BDPyDH1l0TUpDc3sbxzPadNVVWk0Vdb64OrZrNX+GqI7liAGOFEYIqicXKqVdCp3zkjA==; SN=VI35CA728D6D514594A1910C70EA1BB6C9.TOK7C3D24DEA10243759A4BC56905A62E19.1734023794630.LO; vd=VI35CA728D6D514594A1910C70EA1BB6C9-1732547420945-4.1734023794.1734023614.152454923",
}

if __name__ == '__main__':
      

     flipData = getHtml(websiteUrl=flipUrl,showBrowser=False,screenshotName='./lp2')
      
     Allcollection=[]
     
for t in flipData.css('div[class="tUxRFH"]'): 

     allTitle = [t.text() for t in flipData.css('div[class="KzDlHZ"]')]
     print(allTitle)

     allprice = [t.text() for t in flipData.css('div[class="Nx9bqj _4b5DiR"]')]
     print(allprice)

     allimage = [t.attrs['src'] for t in flipData.css('img[loading="eager"][class="DByuf4"]')]
     print(allimage)

     allLaMRP = [t.text() for t in flipData.css('div[class="yRaY8j ZYYwLA"]')] 
     print(allLaMRP)

     allrating = [t.text()for t in flipData.css('div[class="_5OesEi"]')]
     print(allrating)

     allonlyrating = [t.text() for t in flipData.css('span > div[class="XQDdHH"]')]
     print(allonlyrating)

     DeliveryDate = [t.text() for t in flipData.css('div[class="k6cAZE dlFt9U"]')]
     print(DeliveryDate)

     ProductDetail = [t.text() for t in flipData.css('ul[class="G4BRas"]')]
     print(ProductDetail)

     allP_off = [t.text() for t in flipData.css('div[class="UkUFwK"]')]
     print(allP_off)

     AllLaptopData ={
          'Title':allTitle,
          'Price':allprice,
          'Img':allimage,
          'Mrp':allLaMRP,
          'Rating':allrating,
          'onlyRating':allonlyrating,
          'Delivery':DeliveryDate,
          'Detail':ProductDetail,
          'Off':allP_off

     }
     Allcollection.append(AllLaptopData)


     df = pd.DataFrame(AllLaptopData)
     df.to_csv('flipkard.csv')

     

                           
                           
    