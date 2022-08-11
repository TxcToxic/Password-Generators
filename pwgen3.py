import json
import time
import string
import random

# string.digits = 123...
# string.ascii_letters = abc... ABC..
# string.punctuation = !?/...

chars = string.digits + string.ascii_letters + string.punctuation
pw = ''.join(random.choice(chars) for _ in range(32))
data = {
    "time": f"{time.strftime('%T -- %D')}",
    "password": f"{pw}"
}

with open("./password.json", "w") as file:  # do not use a or r otherwise your json file won't keep working!
    file.write(json.dumps(data, indent=4))
