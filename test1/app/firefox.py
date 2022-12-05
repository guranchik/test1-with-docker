from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox

from selenium.webdriver import FirefoxOptions

import time
def parce():
    Cars=[[1,2],[3,4]]
    print("1")
    url ='https://www.mobile.de/ru/%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C/opel-insignia/vhc:car,ms1:19000_35_,frn:2018,ful:diesel,ger:automatic_gear,itp:leather,vcg:estatecar,elw:true,srf:true,ehs:true,blt:true,eas:true,stp:true'
    options = FirefoxOptions()
    print("2")
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(6)
    print("3")
    button = driver.find_element(By.CLASS_NAME, 'sc-bczRLJ.iBneUr.mde-consent-accept-btn')
    button.click()
    cars = driver.find_elements(By.CLASS_NAME, 'g-row.js-ad-entry')
    while True:
        print("0")
        Car=['','','']
        cars = driver.find_elements(By.CLASS_NAME, 'g-row.js-ad-entry')
        for a in cars:
            title = a.find_elements(By.CLASS_NAME, 'vehicle-title.g-col-12.u-text-nowrap')
            for b in title:
                Car[0]=b.text.replace('\n',' ')
            brutto_price=a.find_elements(By.CLASS_NAME, 'seller-currency.u-text-bold')   
            for c in  brutto_price:
                Car[1]=c.text.replace('(Брутто)','')
            link=a.find_element(By.CLASS_NAME, 'vehicle-data.track-event.u-block.js-track-event.js-track-dealer-ratings')
            link = link.get_attribute('href')
            Car[2]=link
            Cars.append(Car)
        try:    
            button = driver.find_element(By.CLASS_NAME, 'pagination-nav.pagination-nav-right.btn.btn--muted.btn--s')
            button.click()   
        except:
            print("all") 
            break       
    return Cars

print(parce())
