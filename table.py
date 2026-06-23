
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


Last=[]
First=[]
Email=[]
Due=[]

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")


table = driver.find_element(By.ID,"table1")

rows = table.find_elements(By.TAG_NAME,"tr")


for r in rows[1:]:

    cols = r.find_elements(By.TAG_NAME,"td")

    Last.append(cols[0].text)

    First.append(cols[1].text)

    Email.append(cols[2].text)

    Due.append(cols[3].text)



df = pd.DataFrame({

    "Last":Last,
    "First":First,
    "Email":Email,
    "Due":Due

})


df.to_csv("table_data.csv",index=False)

print(df)

driver.quit()


















input("enter dabao")