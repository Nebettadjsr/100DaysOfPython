import art
print(art.logo)


def find_winner (some_dic):
    win_user = ""
    win_bid = 0
    for name, bid in some_dic.items():
        if bid > win_bid:
            win_user = name
            win_bid = bid
    print(f"The winner is: {win_user} with a bid of ${win_bid}")

bid_dic = {}
more_bidders = True
while more_bidders:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bid_dic[user_name] = user_bid # add user to dictionary
    ask = input("Are there more bidders? Y/N?\n").lower()
    print("\n" * 20)
    if ask == "n":
        more_bidders = False # stop loop
        find_winner(bid_dic)
    
