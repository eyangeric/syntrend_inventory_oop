from src.index import store
from src.customer import Customer

def test_initialize_customer():
    cher = Customer('cher', 'hwang')
    assert store['customers'] == {1: cher}
    assert cher.__dict__ == {'id': 1, '_first_name': 'CHER', '_last_name': 'HWANG'}

def test_customer_update_with_setter():
    cher = Customer('cher', 'hwang')
    cher.first_name = 'yi-hsuan'
    cher.last_name = 'huang'
    assert cher.__dict__ == {'id': 2, '_first_name': 'YI-HSUAN', '_last_name': 'HUANG'}