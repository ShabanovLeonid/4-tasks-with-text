def Sorted(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    WordsSingle = {};
    for word in allWords:
        if len(word) > 3:
            WordsSingle.update({word: allWords.count(word)})

    keysSorted = []
    for key in WordsSingle:
        keysSorted.append(key)

    keysSorted.sort();

    for key in keysSorted:
        print(key)

def Word(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    WordsSingle = {};

    for word in allWords:
        WordsSingle.update({word: allWords.count(word)})

    keysSorted = []
    for key in WordsSingle:
        keysSorted.append(key)
    keysSorted.sort()

    for key in keysSorted:
        print(f"{key} - {WordsSingle[key]}")

def TopFive(text):
    allWords = text.split()
    allWordsSingle = {};

    for word in allWords:
        allWordsSingle.update({word: allWords.count(word)})

    wordsWithCount = {}
    for word in allWordsSingle:
        wordsWithCount.update( {word: allWords.count(word)} )

    iteration = 1
    for word in sorted(wordsWithCount.items(), key=lambda item: item[1], reverse=True):
        if iteration <= 5:
            print(f"Top {iteration} - {word[0]}: {word[1]} times")
            iteration += 1;
    print("\n")

def ShowText(text):
    print(len(text))

text = input("\nвпишіть текст: ")
while True:

    action = input("виберіть дію: \n1 - сортировка слів\n2 - загальна кількість слів\n3 - скільки символів\n4 - топ 5 слів по повтореню\nEnter your answer: ")
    if action == "1":
        Sorted(text);
    elif action == "2":
        Word(text)
    elif action == "3":
        ShowText(text)
    elif action == "4":
        TopFive(text)
    else:
        print("Invalid action!")