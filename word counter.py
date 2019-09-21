#features is 6 pages. 1200 words per page

#ask for input category

#ask for input word count

#stop program when type finish

#add word counts

#subtract word counts from 7200
print('Welcome to the Express word counter. Please enter your section when prompted to. Your expected word count when prompted to')
n = int(input("How many articles in Features this time?"))
x = []
for i in range(n):
    article = input('Enter an article title? ')
    print(article)
    word_count = x.append(int(input('Enter the word count for this article? ')))
    print(x)
else:
    print('total is', sum(x))
    print('I have to write...', sum(x) - 7200)





