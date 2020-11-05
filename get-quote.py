import random


def get_quote():

    f = open('quotes.txt')
    quotes = f.readlines()
    f.close()
    random_number = random.randint(0, len(quotes)-1)
    print(quotes[random_number])


if __name__ == "__main__":
    get_quote()
