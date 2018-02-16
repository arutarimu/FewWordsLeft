# Made by Arta (Alex Kim)
# This code searches through words.txt, which is every English words
# Then it finds out which words can be typed using only the left hand of QWERTY keyboard
# It has minimalistic search options

# Creating a list of letters typed by left hand
left_hand_alphabets = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
for index in range(0, len(left_hand_alphabets)):
    left_hand_alphabets.append(left_hand_alphabets[index].upper())


def analyze(word):  # A function to see if the letter in a word is in the list
    n = 0
    for letter in word:
        if letter in left_hand_alphabets:
            n = n + 1
    if n == len(word):
        return True
    else:
        return False


class FewWordsLeft:  # FewWordsLeft class has attributes and methods that help find left-hand-only typed words
    def __init__(self, word, my_list):
        self.word = word
        self.my_list = my_list

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word

    def get_my_list(self):
        return self.my_list

    def set_my_list(self, some_list):
        self.my_list = some_list

    def find(self, letter, my_list):
        return letter in my_list

    def search_by_alphabet(self, x, y):
        if x in left_hand_alphabets:
            new_list = []
            for i in range(0, len(y)):
                if str(y[i]).startswith(x.lower()):
                    new_list.append(y[i])
            return new_list
        else:
            print("invalid")

    def starts_with(self, x, y):
        starts_list = []
        for i in y:
            if str(i).startswith(x.lower()):
                starts_list.append(i)
        if len(starts_list)!= 0:
            for i in starts_list:
                print(i)
        else:
            print("Not found.")


def main():
    main_file = open("words.txt", "r", encoding="utf-8")  # Reading the word.txt file using utf-8 unicode encoding
    my_list = []
    for line in main_file:
        line = line.strip("\n").lower()
        if analyze(line):
            my_list.append(line)
    my_list.sort()
    arta_words = FewWordsLeft("", my_list)
    while True:
        print("***** Welcome to the left-hand-only-word finder. (QWERTY only) *****")
        my_input = str(input("        *** To see the whole list, enter W. ***"
                             "\n        *** To see by Alphabet, enter A. ***"
                             "\n        *** To search by front bit of the word, enter S. ***"
                             "\n        *** To Quit the program, enter Q. ***"
                             "\n"))
        if my_input in ["W", "w"]:
            for i in my_list:
                print(i)
        elif my_input in ["A", "a"]:
            another_input = str(input("Enter the Alphabet : "))
            for i in arta_words.search_by_alphabet(another_input, my_list):
                print(i)
        elif my_input in ["S", "s"]:
            other_input = str(input("Enter the bit :"))
            arta_words.starts_with(other_input, my_list)
        elif my_input in ["Q", "q"]:
            print("Goodbye.")
            break
        else:
            print("Please try again")


if __name__ == '__main__':
    main()
