import random
import string

# string.digits = 123...
# string.ascii_letters = abc... ABC..
# string.punctuation = !?/...

chars = string.digits + string.ascii_letters + string.punctuation
pw = ''.join(random.choice(chars) for _ in range(32))

open("./password.txt", "a").write(f"Password > {pw}\n")
