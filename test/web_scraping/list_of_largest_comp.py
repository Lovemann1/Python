from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table_ = soup.find_all('table')[0]
header = table_.find_all('th')
clean_header = [title.text.strip() for title in header]
print(clean_header)

import pandas as pd
df = pd.DataFrame(columns = clean_header)

data = table_.find_all('tr')
for row in data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [every_num.text.strip() for every_num in row_data]

    length = len(df)
    df.loc[length] = individual_row_data
print(df)
df.to_csv(r'C:\my_work\web_scraping\largest_company\companieslist.csv')
    
    