#def RMC_profit(SCU):
#  total_SCU = SCU
#  buy_price = 10968.99986 #buy price for 1SCU of RMC
#  sell_price = 13406.99958 #sell price for 1SCU of RMC
#  valueX = 1.2209863990279967056176076931776 #profit times
#  total_input = (total_SCU * buy_price)
#  total_return = (total_SCU * sell_price)
#  total_profit = str(float(total_return) - float(total_input))
#  total_input = str(total_input)
#  total_return = str(total_return)
#  print("your aUEC input should be: "+total_input)
#  print("your aUEC return should be: "+total_return)
#  print("your aUEC profit should be: "+total_profit)
#
#SCU = int(input("Enter how much SCU of RMC is being used: "))
#RMC_profit(SCU)
  #THIS IS OLD AND THE PRICES FOR 3.24.1 HAVE NOT YET BEEN ADDED

import requests
import json

def NEW_RMC(SCU):
    commodityName = None
    commodityID = None
    total_SCU = SCU
    RMC_Query = int(input("Do you wish to search RMC (1), enter your own commodity ID (2), or enter a name (3): "))
    if (RMC_Query != 1) and (RMC_Query != 2) and (RMC_Query != 3):
        raise Exception("You may only input 1 (RMC) or 2 (Other ID)!")
    elif (RMC_Query == 1):
        commodityID = 63
        commodityName = "RMC"
        ID = True
    elif (RMC_Query == 2):
        commodityID = int(input("Enter commodity ID: "))
    elif (RMC_Query == 3):
        commodityName = input("Enter commodity name (e.g. Agricium): ")
        name_search = True #so that the program uses the name instead of the ID
    commodities_url = "https://uexcorp.space/api/2.0/commodities"
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        
        response = requests.get(commodities_url, headers=headers)
        
        if response.status_code == 200:
            try:
                data = response.json()

                
                if 'data' not in data or not data['data']:
                    print("No data found!")
                    return
                
                
                buy_price = None
                sell_price = None
                for item in data['data']:
                    if (item.get("id") == commodityID) or (item.get("name") == commodityName):  # RMC has id = 63, other values will respond with different materials
                        buy_price = item.get("price_buy")
                        sell_price = item.get("price_sell")
                        commodityName_JSON = item.get("name")
                        break
                        # updated V2.1.0
                
                if buy_price is None or sell_price is None:
                    raise Exception(f"Buy or Sell price not found for {commodityName}.")
                    return

                
                total_input = total_SCU * buy_price
                total_return = total_SCU * sell_price
                total_profit = total_return - total_input

                
                print(f"Your aUEC input for {commodityName_JSON} should be: {total_input}")
                print(f"Your aUEC return from {commodityName_JSON} should be: {total_return}")
                print(f"Your aUEC profit from {commodityName_JSON} should be: {total_profit}")

            except json.JSONDecodeError: # this provides as much response as possible if an error occurs so you may submit an issue on github or make your own modifications to the code
                print("Error: The API response is not in the expected JSON format.")
        elif response.status_code == 401:
            print("Error: Unauthorized access. Check your API key.")
        else:
            print(f"Error: Failed to retrieve data. Status code: {response.status_code}")
            print(f"Error details: {response.text}")
    except Exception as e:
        print(f"Error: {e}")


SCU = int(input("Enter how much SCU of material is being used: "))
if not type(SCU) is int:
    raise TypeError("Must only accept integer values for SCU")
NEW_RMC(SCU)
