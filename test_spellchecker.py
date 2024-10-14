# test_spellchecker.py

# Importing the SpellChecker class from the spellchecker module
from spellchecker import SpellChecker

def main():
    # Create an instance of the SpellChecker
    spell_checker = SpellChecker()

    # Define two sample sentences
    sentences = [
        "Ths is an exmple of a sentnce with a few speling errors.",
        "This is a correct sentence with no mistaks."
    ]

    for sentence in sentences:
        print(f"Original Sentence: {sentence}")

        # Split the sentence into words for spell checking
        words = sentence.split()

        # Check the spelling of each word
        misspelled = spell_checker.unknown(words)

        # Display the misspelled words and suggestions
        for word in misspelled:
            print(f"Misspelled Word: {word}")
            print(f"Suggestions: {spell_checker.candidates(word)}")

        # Correct the sentence by replacing misspelled words with the first suggestion
        corrected_sentence = sentence
        for word in misspelled:
            corrected_word = spell_checker.candidates(word)
            if corrected_word:  # Ensure there are suggestions available
                corrected_sentence = corrected_sentence.replace(word, next(iter(corrected_word)))

        print(f"Corrected Sentence: {corrected_sentence}\n")

if __name__ == "__main__":
    main()
