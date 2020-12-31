import random

while True:
    print('Write your question')
    question = input()
    if question == ' ':
        print('This is not a question!')
    else:
        Answers = ['Definitely gonna happen',
                   '95% it will happen',
                   'Most likely',
                   'Yes',
                   'Be prepared',
                   'Definitely not!',
                   'Oh, no...',
                   'Sorry but very doubtful',
                   'No',
                   'You wish']

        print(Answers[random.randint(0, len(Answers) - 1)])
            


