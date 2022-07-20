
from app import *


def get_exc():
    api_client = ApiClient(RequestConnection(requests))
    data_xml = api_client.get_xml(
        'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(parse_course(xml_adapter, data_xml))
