
from bs4 import BeautifulSoup
import requests
url = 'https://www.amazon.ae/s?k=iphone&crid=3Q3DZ0PUU1PWJ&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
all_listitems = soup.find('div', class_= "s-main-slot s-result-list s-search-results sg-row")
name = all_listitems.find_all('h2')
clear_name = [_.text for _ in name]
filtered_list = [item for item in clear_name if item not in ['Results', 'More results','Related searches']]
    
# print(filtered_list)
# len = 51




#for price
price = all_listitems.find_all('span', class_ = 'a-price-whole')
clean_price = [_.text for _ in price]
# print(clean_price)
#len = 48
import pandas as pd
from datetime import datetime

df = pd.DataFrame({'Product Name': filtered_list, 'Price': clean_price, 'date':datetime.today()})
# df.to_csv(r'C:\my_work\IPhone_Price_Everyday\everday_price.csv')

# today
today_date = str(datetime.today().strftime('%Y-%m-%d'))
df.to_csv(rf'C:\my_work\IPhone_Price_Everyday\CSV_files\Price_on_{today_date}.csv')
