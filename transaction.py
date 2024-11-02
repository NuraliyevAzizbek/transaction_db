transaction_db = {
    "12345": [],
}
card_info = {
    "12345": {"password": "1234", "balance": 1000},
}


def payment(payment_type, amount):
    if payment_type == "1":
        payment_type = "Communal"
    elif payment_type == "2":
        payment_type = "Bank Account"
    elif payment_type == "3":
        payment_type = "Internet"
    else:
        print("Invalid payment type")
    transaction_db[card_id].append(f"{payment_type}: {amount}")
    card_info[card_id]["balance"] -= amount
    print("Your balance is", card_info[card_id]["balance"])


card_id = input("Enter your card id: ")
if card_id not in transaction_db:
    print("Invalid card id")
else:
    while True:
        password = input("Enter your password: ")
        if password != card_info[card_id]["password"]:
            print("Wrong password! \nPlease try again.")
            continue
        else:
            while True:
                a = input("""
--- Assalomu aleykum! ---
1) Balance
2) Transaction
3) Transaction history
4) Change password
0) Exit
Enter your choice: """)
                if a == "0":
                    break
                elif a == "1":
                    print("Your balance is:", card_info[card_id]["balance"], "sum")
                elif a == "2":
                    b = input("""
--- Payment Type ---
1) Communal
2) Bank Account
3) Internet
0) Exit
Enter your choice: """)
                    if b == "0":
                        break
                    else:
                        amount = int(input("Enter amount of money: "))
                        if amount > card_info[card_id]["balance"]:
                            print("Your balance is:", card_info[card_id]["balance"], "sum")
                        else:
                            payment(b, amount)
                elif a == "3":
                    print(len(transaction_db[card_id]))
                    for txn in transaction_db[card_id]:

                        if len(transaction_db[card_id]) == 0:
                            print("Transaction history is empty")
                        else:
                            print(txn)
                elif a == "4":
                    while True:
                        c = input("Enter your password(exit 0): ")
                        if c != card_info[card_id]["password"]:
                            print("Wrong password! \nPlease try again.")
                        elif c == "0":
                            break
                        else:
                            new_password = input("Enter your new password: ")
                            print("Password added successfully! \nYour new password is:", new_password)
                            card_info[card_id]["password"] = new_password
                            break
                else:
                    print("Invalid choice")
        break
