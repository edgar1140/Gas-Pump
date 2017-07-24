import Juan_Way_Gas_Core


def test_gas_price():
    assert Juan_Way_Gas_Core.gas_price('1', 1) == 1.17
    assert Juan_Way_Gas_Core.gas_price('2', 1) == 1.20
    assert Juan_Way_Gas_Core.gas_price('3',1) == 2.50

def test_add_nums():
    assert Juan_Way_Gas_Core.add_nums(7, 2) == 9
    assert Juan_Way_Gas_Core.add_nums(2, 7) == 9
    


def test_revenue_log():
    a = [
        ['a', 'b', 23],
        ['a', 'b', 34],
        ['a', 'b', 22]
        ]
    assert Juan_Way_Gas_Core.revenue_log(a) == 79