from datetime import datetime

date = datetime.now()
print(date)
date = str(date)

date = date[:16]
print(date)

# def main():
#     bitcoin_history = []
#     while True:
#         price = get_latest_bitcoin_price()
#         date = datetime.now()
#         bitcoin_history.append({'date': date, 'price': price})

#         # Send an emergency notification
#         if price < BITCOIN_PRICE_THRESHOLD:
#             post_ifttt_webhook('bitcoin_price_emergency', price)

#         # Send a Telegram notification
#         # Once we have 5 items in our bitcoin_history send an update
#         if len(bitcoin_history) == 5:
#             post_ifttt_webhook('bitcoin_price_update', 
#                                format_bitcoin_history(bitcoin_history))
#             # Reset the history
#             bitcoin_history = []

#         # Sleep for 5 minutes 
#         # (For testing purposes you can set it to a lower number)
#         time.sleep(5 * 60)