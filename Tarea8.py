investment_in_bitcoin = 1.2
bitcoin_to_euros = 40000

def BitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros):
    euro_value = investment_in_bitcoin * bitcoin_to_euros
    return euro_value

investment_in_euro = BitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)

if investment_in_euro <= 30000:
      print ("Your investment is bellow 30,000€!")
else:
     print ("Your investment is above 30,000€!")

# La consola ejecuta: Your investment is above 30,000€!

investment_in_bitcoin = 1.2
bitcoin_to_euros = 25000

def BitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros):
    euro_value = investment_in_bitcoin * bitcoin_to_euros
    return euro_value

investment_in_euro = BitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)

if investment_in_euro <= 30000:
      print ("Your investment is bellow 30,000€!")
else:
     print ("Your investment is above 30,000€!")

# La consola ejecuta: Your investment is below 30,000€!