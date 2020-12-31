import random

while True:
    print('Write your question')
    question = input()
    if question == ' ':
        print('This is not a question!')
    else:
        def getAnswer(answerNumber):
            if answerNumber == 1:
                return 'Definitely gonna happen'
            elif answerNumber == 2:
                return '95% it will happen'
            elif answerNumber == 3:
                return 'Most likely'
            elif answerNumber == 4:
                return 'Yes'
            elif answerNumber == 5:
                return 'Be prepared'
            elif answerNumber == 6:
                return 'Definitely not!'
            elif answerNumber == 7:
                return 'Oh, no...'
            elif answerNumber == 8:
                return 'Sorry but very doubtful'
            elif answerNumber == 9:
                return 'No'
            elif answerNumber == 10:
                return 'You wish'
        print(getAnswer(random.randint(1,10)))
            
##        r = random.randint (1,10)
##        answer = getAnswer(r)
##        print(answer)
