# 2-16-24

In the repo there is a main.py file.

In your terminal just navigate to the folder that holds the main.py file. Run python main.py to start the program.

Notice: This assumes that you have all the necessary installations needed to run basic python on your machine.

Assumptions:
Coffee Prices of each of the Coworkers remains the same and does not change over the course of the schedule.
Coworkers each order the same drink each day and do not change their preferences.

How to Enter Data:
You will be prompted to enter the amount of days that should be scheduled. One person will be assigned to pay each day.
You will also be prompted to submit the prices of each coworkers drink.
If you know how to code in python and are annoyed by submitting data via 7 inputs for all the prices: comment out ln 17 which is input_prices() and uncomment ln 19 and input whatever coffee prices you like. In coffee_prices[0] will be the price for the first coworker Bob. len(coffee_prices) == 7.

Example Inputs (Each of the numbers are input by the user post entry):
How many days should I schedule?: 45
Add the Prices of the Favorite Coffee of each Coworker
Bob: 4.42
Jeremy: 9.99
Coworker A: 8.89
Coworker B: 2.33
Coworker C: 4.32
Coworker D: 5.99
Coworker E: 3.23

How does the program determine who must pay for coffee?
The total cost of the order is computed and then the order price of the owner's drink is deducted. This way, only the amount of money spent on coworkers is kept track of. This keeps it fair since some coworkers will be buying cheaper drinks that others.
The person who has spent the least total so far will be the person who buys drinks that night.

Well Have Fun... and don't buy overpriced drinks.
