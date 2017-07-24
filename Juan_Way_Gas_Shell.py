import Juan_Way_Gas_Core
import Juan_Way_Gas_disk

def main():
    print('Hello! welcome to Juan Way Gas Station. ', end='')
    
    msg = '''Which type of gass would you like?
    \t1. Regular $1.17\n
    \t2. Midgrade $1.20\n
    \t3. Premium $2.50\n '''
    while True:
        gas = input(msg)
        if gas.lower() == 'refuel':
            Juan_Way_Gas_Core.refill()
            print('Tanks refueled.')
            return None
        if gas.lower() == 'revenue':
            left = Juan_Way_Gas_disk.in_the_log()
            print('your total revenue is ${:.2f}'.format(Juan_Way_Gas_Core.revenue_log(left)))
            return None
        if gas == '1' or gas.lower() == 'one'or gas == '2' or gas.lower() == 'two' or gas == '3' or gas.lower() == 'three':
            break

        else:
            print('Sorry, invalid choice!')
    amount = input('How many gallons would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice!')
        return None

    
    gas_type = Juan_Way_Gas_Core.get_gas_type(gas)
    if not Juan_Way_Gas_Core.take_away(gas_type, amount):
        print('Please come back later.')
        return None
    
    print('Your total will be ${:.2f}'.format(Juan_Way_Gas_Core.gas_price(gas, amount)))
    Juan_Way_Gas_Core.keep_log(gas, amount, gas_type)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()