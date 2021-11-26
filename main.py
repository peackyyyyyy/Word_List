import itertools
import os
import string


def password_wordlist(start_range, end_range, file_name="brute.txt"):
    chars = string.ascii_lowercase + string.digits + '!' + '?' + ',' + '(' + ')' + '{' + '}' + ':' + ';' + '@' + '#' + '$' + '.'
    attempts = 0
    f = open(file_name, 'a')

    for password_length in range(start_range, end_range):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            f.write(guess)
            f.write("\n")
            print(guess, attempts)

    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_range = 1
    end_range = 5
    path = os.getcwd()
    file_name = "ni_list.txt"
    path = os.path.join(path, file_name)

    password_wordlist(start_range, end_range, path)

