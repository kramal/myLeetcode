string = 'Almas is my name eee '
words = [ ]
curr_word = [ ]

for ch in string :
    if ch == ' ' :
        words.append ( ''.join ( curr_word ) )
        curr_word = [ ]
        continue

    curr_word.append ( ch )

print ( words )
len_words = len ( words )

for i in range ( 0, len_words // 2 ) :
    temp = words [ i ]
    words [ i ] = words [ len_words - i - 1 ]
    words [ len_words - i - 1 ] = temp

print ( words )
