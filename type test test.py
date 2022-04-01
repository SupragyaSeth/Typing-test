import time


string = "hello this is bob"
wordcount = len(string.split())
print(string)

while True:
    t1 = time.time()
    textinput = str(input("Enter the Sentence:"))
    t2 = time.time()
    accuracy = len(set(textinput.split())&set(string.split()))
    accuracy = accuracy/wordcount
    timetaken = t2 - t1
    wpm = wordcount / timetaken
    print("WPM", wpm, "Accuracy", accuracy, "Timetaken", timetaken)
    break
