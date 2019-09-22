# I created this program to assist me in calculating the word count for my college newspaper section (Features)
#features is 6 pages. 1200 words per page

print('Welcome to the Express word counter. Please enter your article title when prompted to. Your expected word count when prompted to')
n = int(input("How many articles in Features this time?")) #asks the user for a number. This number will be stored as n and used to tell the for loop how many times to repeat itself.
x = [] #creates a blank list (x) the word count values will go into this
for i in range(n): #uses the n value gathered above. Value tells for loop how many times to repeat itself
    article = input('Enter an article title? ') #asks user for article title
    print(article) #prints article titles inputted
    word_count = x.append(int(input('Enter the word count for this article? '))) #Asks user for word count input. Saves this input to a list
    print(x) #prints the word counts inserted into list (x)
else: #when the range is finished the program moves onto this section
    print('total is', sum(x)) # adds the values in list (x) and prints out the result.
    print('I have to write...', sum(x) - 7200) #7200 is the told word count of Features. Subtracting 7200 from the told of the list (x) will give me a left over word count (what I have to contribute to my section)





