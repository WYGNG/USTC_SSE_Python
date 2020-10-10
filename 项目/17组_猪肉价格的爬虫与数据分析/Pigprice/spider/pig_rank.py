from spider.request_factory import load_html_to_bs, urls, get_input
from pprint import pprint
import re
import pandas as pd
items = {}
for i in load_html_to_bs(urls.get('rank_index')).select(".list_nav div a"):
    items[i.text] = i.attrs['href']
item = get_input(items, 'item')

a = load_html_to_bs(urls.get('baseUrl') + items.get(item)).select(".list_tab ")
result = [re.split('\n| ',i) for i in a[0].text.strip('\n\n').split('\n\n\n')]
# dataframe结果
df = pd.DataFrame(result[1:],columns = result[0])
print(df)
# pprint(result)   #原result结果
