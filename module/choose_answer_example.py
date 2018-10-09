# the module function is to build a module to build subject, and set individually contribution

# create a questions class, it's convenient to create subject having same attribution
# beforeahead to create a promt and answer to the questions
# build a def to test the function

from question import question

# describe the whole content
questions_prompt = [
    ('the color of apple is ', 'a = red','b = yellow'),
    ('the color of banana is ', 'a = red', 'b = yellow')
]

# build an object values to the object class
questions = [
    question(questions_prompt[0],'a'),
    question(questions_prompt[1],'b')
]

def run_test(questions):
    for question in questions: # each subject for whole modul
        scorr = 0
        answer = input(question.prompt) # input the contribution for each subject
        if answer == question.answer:
            scorr = scorr + 1
        print(scorr)

run_test(questions)