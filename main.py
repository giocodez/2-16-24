coffee_prices = [0]*7
current_payment = [0]*7
names = ["Bob", "Jeremy", "Coworker A", "Coworker B", "Coworker C", "Coworker D", "Coworker E"]
total_coffee_prices = 0

def input_prices():
  print("Add the Prices of the Favorite Coffee of each Coworker")
  coffee_prices[0] = input("Bob: ")
  coffee_prices[1] = input("Jeremy: ")
  coffee_prices[2] = input("Coworker A: ")
  coffee_prices[3] = input("Coworker B: ")
  coffee_prices[4] = input("Coworker C: ")
  coffee_prices[5] = input("Coworker D: ")
  coffee_prices[6] = input("Coworker E: ")

def main(n):
  input_prices()
  #may uncomment and just input your own values in below array if desired and comment out input_prices if too annoying to use for programmers
  #coffee_prices = [3.42, 5.44, 4.33, 2.43, 3.12, 3.95, 4.44]
  cont = 0
  for x in range(len(coffee_prices)):
    coffee_prices[x] = float(coffee_prices[x])
  total_coffee_prices = sum(coffee_prices)
  while cont < n:
    payer_index = current_payment.index(min(current_payment))
    print("day " + str(cont+1) + ": " + names[payer_index] + " is paying")
    current_payment[payer_index] += total_coffee_prices - coffee_prices[payer_index]
    cont += 1

k = int(input("How many days should I schedule?: "))
main(k)