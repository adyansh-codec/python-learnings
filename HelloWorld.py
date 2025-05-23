import time
import os

word = "Hello My Name is Python and I am your first program "
while True:
    print(word, end='\r', flush=True)
    word = word[1:] + word[0]
    time.sleep(0.3)