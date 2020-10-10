from spider.request_factory import get_data_by_item_name,get_all_data_by_name_concurrent
from pprint import pprint
import pandas as pd

data = get_data_by_item_name('bean', '北京市')
# pprint(data)

df = pd.DataFrame(data[1:], columns=data[0])
print(df)
