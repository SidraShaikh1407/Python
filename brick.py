import pywhatkit as kit
import time
import random

clients =  [
    "+919820223473",
    "+919987099250",
] # add more numbers
message = """Hii

This is Sidra from IndiBrick.

"""

for number in clients:
    try:
        kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        print(f"Message sent to {number}")
    except Exception as e:
        print(f"Error sending to {number}: {e}")

    delay = random.randint(35, 45)
    print(f"Waiting {delay} seconds...")
    time.sleep(delay)
