import random
import time
from xxlimited import Str

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

#Functions
def Accuracy(l_textinput, l_originalstr):
    split_input = l_textinput.split()
    wordcount = len(l_originalstr)
    accuracy = len(set(l_textinput.split())&set(l_originalstr))
    accuracy = (accuracy/wordcount) * 100 
    accuracy = round(accuracy)
    return accuracy

def WPM(l_textinput, l_timetaken):
    list_wordcount = l_textinput.split()
    temp_wordcount = len(list_wordcount)
    wpm = (temp_wordcount * 60) / l_timetaken
    wpm = round(wpm)
    return wpm

#Passages that the user has to type
passage1 = "The cat walked down the road"
passage2 = "The apple grows on the tree"
passage3 = "There are birds in the sky"
passage4 = "The mouse ate the cheese"

randlist = [passage1, passage2, passage3, passage4]
choice = random.choice(randlist)
value = choice.split()
print( "\n" + choice) 

#Finding time
input("\n Press Enter to Start...")
t1 = time.time()
textinput = str(input("\n" + "Enter the Sentence: "))
t2 = time.time()
timetaken = t2 - t1
timetaken = round(timetaken)

print("\n" + "WPM:", WPM(textinput, timetaken), "Accuracy:", str(Accuracy(textinput, value)) + "%" , "Timetaken:", timetaken)