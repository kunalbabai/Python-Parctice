def correction(word):
    from textblob import TextBlob
    from spellchecker import SpellChecker
    try:
        corrected_word = []
        wrong_word = []
        temp_str = ""
        final_str = []
        spelling = SpellChecker()
        if type(word) == str:
            misspelled = spelling.unknown(word)
            print(f"The Given Wrong Word is - {misspelled}", end="----->")
            temp_str = TextBlob(word)
            print(f"The Correced Word is - {temp_str.correct()}")
        elif type(word) == list:
            for i in word:
                wrong_word.append(spelling.unknown(i))
                corrected_word.append(TextBlob(i))
            for j in corrected_word:
                final_str.append(str(j.correct()))
            print(f"The Given Wrong Word is - {' , '.join(wrong_word)}", end="----->")
            print(' , '.join(final_str))
    except Exception as Ex:
        print(Ex)
correction('Data Scence')