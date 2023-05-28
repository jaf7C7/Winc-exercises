# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# Most widely spoken language (==)
spain_lang = 'Castilian Spanish'
switz_lang = 'Swiss'
print(spain_lang == switz_lang)  # False

# Most prevalent religion (==)
spain_religion = 'Roman Catholic'
switz_religion = 'Roman Catholic'
print(spain_religion == switz_religion)  # True

# Name length of capital city (!=)
spain_capital_length = len('Madrid')
switz_capital_length = len('Bern')
print(spain_capital_length != switz_capital_length)  # True

# GDP (Spain < Switzerland)
spain_gdp = 1798
switz_gdp = 618
print(spain_gdp < switz_gdp)  # False

# Population growth (Spain < 1% and Switzerland < 1%)
spain_pop = 0.12
switz_pop = 0.64
print(spain_pop < 1 and switz_pop < 1)  # True

# Population (Spain > 10 million or Switzerland > 10 million)
spain_pop = 47222613
switz_pop = 8563760
print(spain_pop > 10000000 or switz_pop > 10000000)  # True

# Population (Spain > 10 million > Switzerland or
#             Switzerland > 10 million > Spain)  # True
print(spain_pop > 10000000 > switz_pop or switz_pop > 10000000 > spain_pop)
