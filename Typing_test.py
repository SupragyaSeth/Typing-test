from random import random
import time
import random

randlist = ["come", "when", "it", "logo"]
random.shuffle(randlist)
wordcount = len(randlist)
print(*randlist)

while True:
    t1 = time.time()
    textinput = str(input("Enter the Sentence:"))
    t2 = time.time()
    accuracy = len(set(textinput.split())&set(randlist))
    accuracy = accuracy/wordcount
    timetaken = t2 - t1
    wpm = wordcount / timetaken
    print("WPM", wpm, "Accuracy", accuracy, "Timetaken", timetaken)
    break