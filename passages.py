import random
import time
def FindAccuracy(input_passage,output_passage) :
    output_wordcount = len(output_passage)
    print(output_wordcount)
    count = 0
    word_match=0
    for x in input_passage:
        print(x,output_passage[count])
    
        if (count+1 < output_wordcount) & (x == output_passage[count])  :
            
            word_match=word_match+1
        count=count+1
    print(word_match)    


#Passages that the user has to type
passage1 = "The cat walked down the road"
passage2 = "The apple grows on the tree"
passage3 = "There are birds in the sky"
passage4 = "The mouse ate the cheese"

randlist = [passage1, passage2, passage3, passage4]
choice = random.choice(randlist)
value = choice.split()
wordcount = len(value)
print( "\n" + choice)

#Calculations
input("\n Press Enter to Start...")
t1 = time.time()
textinput = str(input("\n" + "Enter the Sentence: "))

t2 = time.time()
split_input = textinput.split()
FindAccuracy(value,split_input)
accuracy = len(set(textinput.split())&set(value))
accuracy = (accuracy/wordcount) * 100

timetaken = t2 - t1

textval = textinput.split()
textval2 = len(textval)

wpm = (textval2 * 60) / timetaken
wpm = round(wpm)

accuracy = round(accuracy)
timetaken = round(timetaken)

print("\n" + "WPM", wpm, "Accuracy", accuracy , "Timetaken", timetaken)