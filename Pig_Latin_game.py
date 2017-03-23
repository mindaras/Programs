Pig Latin game concept: removes the first letter from a word and puts it to the back of the word and appends a suffix
'ay'. Example: 'Python' after Pig Latin translation: 'ythonay'

Kodas:

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]  // paima zodi nuo 2 raides iki pat galo (dar galima [1:len(new_word)])
    print 'Your Pig Latin translation: ' + new_word
    
else:
    print 'empty'