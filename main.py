from replit import clear
from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console.
run_again= True
bid_dictionary= []


while run_again:
    name= input("what is your name\n")
    bid_price = int(input("how much is your bid \n $ "))
    entry = {
      "bidder": name,
      "amount": bid_price
    }
    bid_dictionary.append(entry)
    play_again = input("enter 'yes' or 'no' to add another bidder\n").lower()
    if play_again=="no":
      run_again=False
    else:
      clear()
    entry = {}

def highest_bid(bid_dict):
    win_bid = bid_dict[0]["amount"]
    win = bid_dict[0]["bidder"]
    for element in bid_dict:
      if element["amount"]>win_bid:
         win_bid = element["amount"]   
         win = element["bidder"]
    print(f"the highest bid is {win} with $ {win_bid} ")


clear()
highest_bid(bid_dictionary)


  
