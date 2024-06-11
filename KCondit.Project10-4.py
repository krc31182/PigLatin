# Kenneth Condit
# 6/11/2024

# import string mod
import string

def main():
    print("Pig Latin Translator by Ken Condit")

    # get input
    while True:
        text = input("\nEnter text: ").strip()
        if not text:
            print("No text entered. Try again.")
            continue

        # convert to lowercase
        original_text = text.lower()
        # to pig latin with function
        translated_text = translate_to_pig_latin(original_text)

        # display both versions
        print("\nEnglish: " + original_text)
        print("Pig Latin: " + translated_text)

        while True:
            choice = input("\nContinue? (y/n): ").lower()
            if choice == "n":
                print("\nBye!")
                return
            elif choice == "y":
                break
            else:
                print("Invalid entry. Try again.")

# split up words 
def translate_to_pig_latin(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return ' '.join(translated_words)
# define vowels
def translate_word(word):
    vowels = "aeiou"
    
    word = word.translate(str.maketrans('', '', string.punctuation))

    if not word:
        return word

    # if starts with vowel add way   
    if word[0] in vowels:
        return word + "way"

    
    first_vowel_index = -1
    for i, char in enumerate(word):
        # if y is first character its a consonant if not its a vowel
        if char in vowels or (char == 'y' and i != 0):
            first_vowel_index = i
            break

      # if no vowel add ay
    if first_vowel_index == -1:
        return word + "ay"  
    
    return word[first_vowel_index:] + word[:first_vowel_index] + "ay"

if __name__ == "__main__":
    main()
