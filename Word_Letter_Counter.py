def frequencies(text):
    mydict={}
    for word in text.split():
        clean_word="".join(c for c in word if c.isalpha())
        if len(clean_word)>=2:
            if clean_word in mydict:
                mydict[clean_word]+=1
            else:
                mydict.update({clean_word:1})
    return mydict
def word_count(text):
    count = 0
    for word in text.split():
        if len(word) >= 2:
            count += 1
    return count

def letter_count(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def main():
    while True:
        text = input("Enter a sentence(type 'ex' to exit): ")
        if text.lower().strip()=="ex":
            break
        print(f"The count of word(s) is {word_count(text)}")
        print(f"The count of letter(s) is {letter_count(text)}")
        print(f"The frequencies of words:")
        for key,value in frequencies(text).items():
            print(f"{key} : {value}")
if __name__ == "__main__":
    main()
