Title :
Bitcoin Price Notification.

Aim: The objective of this project is to use python to get the price of bitcoin (BTC) from a website (API URL) and send notification of the same on Telegram app.
Also mail notification is received on the user's gmail account.

The price of Bitcoin and other cryptocurriencies change frequently in a small interval of time.
So we have to constantly keep a track for trading purpose and monitor it's price. Now a days it is not possible to take out time thst often to monitor it's price all the time due to our busy schedule.

So this project comes handy to keep the user updated with the price of bitcoin and other cryptocurriencies.

It sends notifications on Telegram on regular interval of few minutes. And there is a perovision to get mail notifications of the same on gmail too.

One more thing is that if the price crosses the boundry of user's trading prospectus or falls below a certain threshold price, then an emergency notification will be sent to have a prompt action of Buy / Sell. (Depends).

This project File Runs on command-line. So Need to provide few arguments for the Same.
Mainly 4 arguments need to be provided here. (must)
Arguments: Ex. BTC 10 5 5
1. BTC or ETH for title of cryptocurrency.

2. Lower threshold price for emergency notification.
    For BTC the input must be a 2-digit number indicating USD in thousands.
    ex. 10 = $ 10000

    For ETH the input is straight forward in USD $ 300
    ex. 300 = $ 300

3. There will be seperate individual notifications but the notifications will be received continuously after certain intervals and an history log will be maintained for all notifications. Here user mmust input length of the log list. 
    ex. 5 for 5 notifications in a log.

4. The last argument is the time frequency in minutes to receive notifications.
    ex. 5 for receiving notifications every 5 mins.

The code then runs and the notification output is received on Telegram as seperate notifications and a log even.

Mail is sent on the user's gmail account even.

The user can choose to visit the Website provided in the mail for detailed view of different cryptocurriencies.

The user can choose to get notifications for Ethereum cryptocurrency by typing the arguments as : ETH 300 5 5

The code runs succesfully.

Enjoyed doing the project.