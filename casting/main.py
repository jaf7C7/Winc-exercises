# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# Part 2
leek_order = 'leek 4'
leek_order_qty = int(leek_order[leek_order.find('4'):])
sum_total = leek_price * leek_order_qty
print(sum_total)

# Part 3
broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
broccoli_order_qty = float(broccoli_order[broccoli_order.find('1.6'):])
broccoli_sum_total = round(broccoli_price * broccoli_order_qty, 2)
print(
    str(broccoli_order_qty) +
    'kg broccoli costs ' +
    str(broccoli_sum_total)
    + 'e'
)
