investment_in_bitcoin = 1.2
bitcoin_to_euros = 40000

def bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros):
    euro_value = investment_in_bitcoin * bitcoin_to_euros
    return euro_value

investment_in_euro = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)

if investment_in_euro <= 30000:
      print ("Investment below 30,000€! SELL!")
else:
     print ("Investment above 30,000€!")

# La consola ejecuta: Investment above 30,000!

investment_in_bitcoin = 1.2
bitcoin_to_euros = 25000

def bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros):
    euro_value = investment_in_bitcoin * bitcoin_to_euros
    return euro_value

investment_in_euro = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)

if investment_in_euro <= 30000:
      print ("Investment below 30,000€! SELL!")
else:
     print ("Investment above 30,000€!")

# La consola ejecuta: Investment below 30,000€! SELL!