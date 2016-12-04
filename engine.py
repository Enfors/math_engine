#!/usr/bin/env python3
"Python engine for practicing simple math."

from __future__ import print_function # To shut PyLint up

import random

class Engine(object): # pylint: disable=too-few-public-methods
    "Main engine class."

    def __init__(self, database=None):
        self.database = database

    def start(self):
        "Mainly used for testing."
        print("Engine started.")
        user = User("Student-name", "Parent-name")

        drill = MultiplicationDrill(user)
        status = drill.start()

        if status.output:
            print(status.output)

        while not status.done:
            user_input = input("-> ")
            status = drill.recv_input(user_input)
            print(status.output)



class User(object): # pylint: disable=too-few-public-methods
    "Keeps track of a user of the math engine."

    def __init__(self, name, reports_to=None):
        self.name = name
        self.reports_to = reports_to # User's parent / teacher user object.



class Activity(object):
    "An activity for a user, such as a drill."

    def __init__(self, user):
        self.user = user

    def start(self):
        "This function should be overridden."
        print("%s.start(): not implemented." % repr(self))

    def recv_input(self, text):
        "Accept user input for the Activity. Should be overridden."
        return ActivityStatus("%s.recv_input(): not implemented." % repr(self),
                              done=True)



class ActivityStatus(object): # pylint: disable=too-few-public-methods
    "Returned from activities."

    def __init__(self, output, done=False):
        self.output = output
        self.done = done



class Drill(Activity):
    "An activity of type Drill."

    def __init__(self, user, num_questions=5):
        super(Drill, self).__init__(user)
        self.num_questions = num_questions
        self.num_answered = 0
        self.num_correct = 0
        self.question = None
        self.answer = None

    def start(self):
        "Start the Drill."
        self.make_question()
        return ActivityStatus(self.format_question())

    def make_question(self):
        "Must be overridden."
        self.question = "Why doesn't this work?"
        self.answer = "Because Enfors coded it incorrectly."

    def format_question(self):
        "Format the question properly for asking."
        return "Question %d of %d:\n%s" % (self.num_answered + 1,
                                           self.num_questions,
                                           self.question)

    def recv_input(self, user_input):
        user_input = int(user_input)

        self.num_answered += 1

        if user_input == self.answer:
            output = "Correct!\n"
            self.num_correct += 1
        else:
            output = "No, the correct answer is %d.\n" % self.answer

        if self.num_answered < self.num_questions:
            self.make_question()
            output += self.format_question()
            return ActivityStatus(output, done=False)
        else:
            output += "Drill complete. Correct answers: %d out of %d." %\
                      (self.num_correct, self.num_questions)
            return ActivityStatus(output, done=True)



class MultiplicationDrill(Drill):
    "A Drill of type Multiplication."

    def __init__(self, user, num_questions=5, starting_limit=12, limit=12):
        super(MultiplicationDrill, self).__init__(user, num_questions)
        self.starting_limit = starting_limit
        self.limit = limit

    def make_question(self):
        "Store a question."
        num_a = random.randint(2, self.limit)
        num_b = random.randint(2, self.limit)

        self.question = "%d * %d" % (num_a, num_b)
        self.answer = num_a * num_b



class AdditionDrill(Drill):
    "A Drill of type Addition."

    def make_question(self):
        "Store a question."

        num_a = random.randint(2, 10)
        num_b = random.randint(2, 10)

        self.question = "%d + %d" % (num_a, num_b)
        self.answer = num_a + num_b



if __name__ == "__main__":
    Engine().start()
