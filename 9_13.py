"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Anas Monjib
Email:      amonjib@gmail.com
Student Id: H291936

"""
from collections import OrderedDict

def main():
    p_words = OrderedDict()

    p_words['Loop'] = 'using for in to loop through defined orders'
    p_words['Booleon'] = 'a statement with true or false as answer'
    p_words['List'] = 'a list of names or things'
    p_words['String'] = 'basically what the computer understands as text'
    p_words['pyhton'] = 'computer programming language'
    p_words['set'] = 'using set() only prints items once if they are the same'
    p_words['print'] = 'This statement prints the output on the screen'
    p_words['Dictionary'] = 'this right here is an exm. of a dictionary'

    print("Python glossary:\n")
    for term, meaning in p_words.items():
        print(term + ': ' + meaning)

if __name__ == "__main__":
    main()
