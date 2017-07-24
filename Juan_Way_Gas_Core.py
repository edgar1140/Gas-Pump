def gas_price(gas, amount):
    """ str -> Float"""
    if gas == '1':
        return float(amount) * 1.17
    elif gas == '2':
        return float(amount) * 1.20
    elif gas == '3':
        return float(amount) * 2.50

def get_gas_type(gas):
    """(str, float) --> str"""
    if gas == '1' or gas.lower() == 'one':
        gas_type = 'Regular'
    elif gas == '2' or gas.lower() == 'two':
        gas_type = 'Midgrade'
    elif gas == '3' or gas.lower() == 'three':
        gas_type = 'Premium'
    return gas_type

def keep_log(gas,amount, gas_type):
    price = gas_price(gas, amount)
    message = '\n{}, {}, ${}'.format(gas_type, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)



def revenue_log(left):
    """ return float value of total dollars spent"""
    
    price = 0 
    for item in left:
        price += item[2]
    return price
   
def in_the_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left


def take_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[0] == gas_type:
            if float(amount) > item[1]:
                print('Sorry amount of gas have been reached, We only have 5000.0 gallons.')
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file: 
        file.write(message)
    return True

def refill():
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]= str(item[2])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)  

    with open('tank.txt', 'w') as file:
        file.write(message)

def add_nums(a, b):
    return a + b
    