import random
import time

#Functions
def Accuracy(l_textinput, l_originalstr):
    split_input = l_textinput.split()
    wordcount = len(l_originalstr)
    accuracy = len(set(split_input) & set(l_originalstr))
    accuracy = (accuracy/wordcount) * 100 
    accuracy = round(accuracy)
    return accuracy

def WPM(l_textinput, l_timetaken):
    list_wordcount = l_textinput.split()
    temp_wordcount = len(list_wordcount)
    wpm = (temp_wordcount * 60) / l_timetaken
    wpm = round(wpm)
    return wpm

def typingErrors(prompt, input):

    promptlist = prompt.split()
    inputlist = input.split()
    lenth = len(inputlist)
    errors = 0
    count = 0
    
    for x in promptlist:
        if (count < lenth ): 
            if (x != inputlist[count]):
                errors = errors + 1 
        else:
                errors = errors + 1
        count = count + 1    
        
    return errors

#Passages that the user has to type
passage1 = "The big black cat walked down the road"
passage2 = "The green apple grows on the tall tree"
passage3 = "There are many birds in the sky"
passage4 = "The little mouse ate the cheese"
passage5 = "She was sad to hear that fireflies are facing extinction due to habitat loss"
passage6 = "He did not cheat on the test because it was not the right thing to do"

randlist = [passage1, passage2, passage3, passage4, passage5, passage6]
choice = random.choice(randlist)
value = choice.split()
print( "\n" + choice) 

#Finding time
input("\n Press Enter to Start...")
t1 = time.time()
textinput = str(input("\n" + "Enter the Sentence: "))
t2 = time.time()
timetaken = t2 - t1

print("\n" + "WPM:", WPM(textinput, timetaken), "Accuracy:", str(Accuracy(textinput, value)) + "%" , "Timetaken:", round(timetaken) , "Number of Errors:", str(typingErrors(choice, textinput)))