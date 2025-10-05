balance = 700 

print("Welcome to Mini ATM")

print(f"Your balance is {balance}")

print("\nChoose an option")

print("1. Check your balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Exit")

while True:
  choice = input("Enter your choice (1-4):")
  if choice == "1":
    print(f"Your balance is {balance}")
  if choice== "2":
    amount = int(input("Enter amount to deposit:"))
    balance += amount
    print(f"Deposit successful! New balance = ${balance}")
  if choice == "3":
    amount = int(input("Enter amount to withdraw:"))
    balance -=amount
    print(f"withdrawal successful! New balance = ${balance}")
  if choice == "4":
    print("goodbye!thanks for using Mini ATM")
    break
