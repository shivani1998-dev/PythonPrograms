import art
print(art.logo)
bidders_present=True
user_details={}

while bidders_present:
         user_name=input("What is your name?:")
         user_bid=int(input("What is your bid? $"))
         user_details[user_name]=user_bid

         other_bidders=input("Are there any other bidders? Type 'yes' or 'no': ")
         if other_bidders=='yes':
             bidders_present=True
         else:
             bidders_present=False
             highest_bid=0
             highest_bidder_user=""
             for user in user_details:
                if user_details[user]>highest_bid:
                   highest_bid=user_details[user]
                   highest_bidder_user=user
             print(f"The winner is {highest_bidder_user} with a bid of ${highest_bid}")




