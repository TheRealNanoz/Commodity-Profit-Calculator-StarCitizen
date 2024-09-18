def RMC_profit(SCU):
  total_SCU = SCU
  buy_price = 10968.99986 #buy price for 1SCU of RMC
  sell_price = 13406.99958 #sell price for 1SCU of RMC
  valueX = 1.2209863990279967056176076931776 #profit times
  total_input = (total_SCU * buy_price)
  total_return = (total_SCU * sell_price)
  total_profit = str(float(total_return) - float(total_input))
  total_input = str(total_input)
  total_return = str(total_return)
  print("your aUEC input should be: "+total_input)
  print("your aUEC return should be: "+total_return)
  print("your aUEC profit should be: "+total_profit)

SCU = int(input("Enter how much SCU of RMC is being used: "))
RMC_profit(SCU)
  #THIS IS OLD AND THE PRICES FOR 3.24.1 HAVE NOT YET BEEN ADDED