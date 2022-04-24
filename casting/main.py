# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

leek_order = 'leek 4'
leek_order_integer = int(leek_order[leek_order.find('4')])
sum_total = leek_price * leek_order_integer
print(sum_total)

broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
broccoli_order_integer = float(broccoli_order[-3:]) 
total_sum = round(broccoli_order_integer * broccoli_price, 2)
print(str(broccoli_order_integer) + 'kg broccoli costs ' + str(total_sum) + 'e')
