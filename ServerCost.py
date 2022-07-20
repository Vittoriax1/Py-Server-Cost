# Created by Jennifer Souvannasing, SEC290, Chap 2 Exercise, 07/10/22

# Cost per hour to run one server
cph = 0.51

# Calculate the cost to run 1 server per day and per month
dayrate = cph * 24
monthrate = dayrate * 30

# Output of calculations
print('=' * 100)
print('The cost to run one server per hour is: $ {:,.2f}'.format(cph))
print('The cost to run one server per day is: $ {:,.2f}'.format(dayrate))
print('The cost to run one server per month is: $ {:,.2f}'.format(monthrate))

#What if you are on a budget of 918$
budget1 = 918
runout = budget1 / dayrate
print('Your budget is ${:,.2f}. You can run one server for {:.2f} days before your budget runs out.'.format(budget1,runout))
budget2 = float(input('Test a different budget amount: '))
runout2 = budget2 / dayrate
print('Your new budget is ${:,.2f}. You can run one server for {:.0f} days before your budget runs out.'.format(budget2,runout2))
print('=' * 100)

# What about more servers?
numserv = int(input('How many servers are you running? '))
hrserv = cph * numserv
print('The cost to run',numserv,'servers per hour is: $ {:,.2f}'.format(hrserv))
dayserv = 24*hrserv
print('The cost to run',numserv,'servers per day is: $ {:,.2f}'.format(dayserv))
monthserv = 30*dayserv
print('The cost to run',numserv,'servers per month is: $ {:,.2f}'.format(monthserv))
print('=' * 100)


