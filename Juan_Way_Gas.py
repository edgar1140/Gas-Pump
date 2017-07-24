# gas pump program

# user selects if they want regular, mid-grade, or premium

# pay after fill option
# user inputs the number of gallons
# computer displays the cost


# pre-pay
# user inputs the amount of money to pay
# computer displays the amount of money to pay

# OTHER THINGS TO CONSIDER
# nice clean code
# have a nice interface and customer experience
# use your function well
# make it personalized to you


# pay_before:
    #gallons = money / gas price

def price_of_gas(type_gas):
    """ (str) -> float
    This function will print a message to the user 
    and return the float value of the price per gallon
    >>> price_of_gas('regular')
    You picked regular which is 1.17
    1.17
    >>> price_of_gas('mid-grade')
    You picked regular which is 1.20
    1.20
    >>> price_of_gas('premium')
    You picked regular which is 2.50
    2.50
    """
    if type_gas == 'regular' or type_gas == 'Regular':
        print('You picked regular which is 1.17')
        return 1.17
    elif type_gas == 'mid-grade' or type_gas == 'Mid-grade':
        print('You picked mid-grade which is 1.20')
        return 1.20
    elif type_gas == 'premium' or type_gas == 'Premium':
        print('You picked premium which is 2.50')
        return 2.50
    else:
        return None


def pay_before(money,type_gas):
    ''' ( float, float) -> (float)
    returns amount of gallons

    >>> gallons(20, 1.17)
    17.09
    >>> gallons(10, 1.20)
    8.3
    >>> gallons(25, 2.50)
    10
    '''
    gallons = (money) / (type_gas)
   
   # return 2 decimal places
    return float(round(gallons, 2))

    # money = gallons * gas_price
def pay_after( gallons, type_gas):
     ''' ( float, float) -> (float)
     return amount of dollars
     >>> money(34, 1.17)
     39.78
     >>> money(65, 1.20)
     78
     >>> money(23, 2.50)
     57.5
     ''' 
     money = (gallons * type_gas)
     return float(round(money))





print('Hello welcome to Juan Way Gas Station!!!\n') 
type_gas= input('what gas type would you like regular 1.17, mid-grade 1.20, or premium 2.50\n')
payment_type = input('Would you like to pre pay or pay after\n')
print(payment_type)



if payment_type == 'pre pay':
    money = input('How much money would you like to pay\n')
    # gallons = money / gas_price
    print('total', (float(money) / price_of_gas(type_gas)), 'gallons.' )

elif payment_type == 'pay after':
    gallons = input('\nHow many gallons would you like?\n')
    print('you total $', (float(gallons) / price_of_gas(type_gas)))
    
    
 
# if gallons == 'regular':
# regular = gallons * 1.17
#     print(regular)

# elif 'mid-grade':
#     mid_grade = gallons * 1.20
#     print(mid_grade)

# else:
#     premium = gallons * 2.50
#     print(premium)
