# Final Exam Question 2 Harpreet Kaur(student id: 2031314)

class frenchLanguage:  # it returns the french version

    def __init__(self):
        self.translations = {"car": "Tesla", "bike": "Harley-Davidson",
                             "cycle": "3T Bikes"}

    def translator(self, txtMsg):
        return self.translations.get(txtMsg, txtMsg)  # change the message using translations


class spanishLanguage:  # it returns the spanish version

    def __init__(self):
        self.translations = {"car": "BMW", "bike": "Honda",
                             "cycle": "Alchemy"}

    def translator(self, txtMsg):
        return self.translations.get(txtMsg, txtMsg)  # change the message using translations


class englishLanguage:  # it returns the english version

    def translator(self, txtMsg):  # here return the same message
        return txtMsg


def Factory(language="English"):
    translator = {
        "French": frenchLanguage,
        "English": englishLanguage,
        "Spanish": spanishLanguage,
    }

    return translator[language]()


if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    txtMessage = ["car", "bike", "cycle"]

    for msg in txtMessage:
        print(f.translator(msg))
        print(e.translator(msg))
        print(s.translator(msg))

# Advantages.

# 1. we can easily add any new types of language without disturbing the existing code
# 2. we can avoid the light coupling ( mostly classes & objects are dependent each other) using this factory
    # methods we increase flexibility and re-usability of the code

# Disadvantages
# 1. Makes code more difficult to read as all of your code is behind an abstraction
    # that may in turn hide abstractions.
