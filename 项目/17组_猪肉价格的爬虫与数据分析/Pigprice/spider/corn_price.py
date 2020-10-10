from spider.request_factory import get_data_by_item_name,get_all_data_by_name_concurrent
from pprint import pprint

pprint(get_data_by_item_name('corn', '北京市'))
pprint(get_all_data_by_name_concurrent('corn'))