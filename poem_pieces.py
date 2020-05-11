# Kuhlmann sonnet generator

# Import our modules
import pandas as pd
import random as rd

# Open our text files and convert them into DataFrames
    # Single-use nouns
mono_nouns = pd.read_csv('1syllablenouns.txt', )
# Rename the column
mono_nouns.columns = ['word']
# Make sure all values are a string
mono_nouns = mono_nouns.applymap(str)

    # Prepositions
mono_preps = pd.read_csv('1syllableprepositions.txt')
# Rename the columns
mono_preps.columns = ['word']
# Make sure all values are a string
mono_preps = mono_preps.applymap(str)

    # Multi-noun phrases
multi_nouns = pd.read_csv('3syllablephrases.txt')
# Rename the column
multi_nouns.columns = ['word']
# Make sure all values are a string
multi_nouns = multi_nouns.applymap(str)

    # Most commonly-used words in English
    # Source: https://github.com/first20hours/google-10000-english
common_words = pd.read_csv('google-10000-english-no-swears.txt')
# Rename the column
common_words.columns = ['word']
# Make sure all values are a string
common_words = common_words.applymap(str)

# Make a new dataset of only the most commonly-used nouns with no swear words
# Source: http://www.datasciencemadesimple.com/intersection-two-dataframe- \
# pandas-python-2/
nouns_filtered = pd.merge(mono_nouns, common_words, how='inner')
# Make sure all values are a string
nouns_filtered = nouns_filtered.applymap(str)

# Define a function to get a random word from the DataFrame
    # Takes a DataFrame as an argument
def random_word(words_df):
    # Find the length of the DataFrame
    n = len(words_df) - 1
    
    # Randomly generate an integer x between 0 and n
    x = rd.randint(0,n)
    
    # Get the value (word) of the cell in row x
    word = words_df.at[x,'word']
    
    # We want the word to be capitalized as in Kuhlmann's sonnets
    # Source: https://stackoverflow.com/questions/1549641/how-to-capitalize- \
    # the-first-letter-of-each-word-in-a-string
    word = word.title()
    
    return word

# First let's define a function which makes the beginning of a line
    # Preposition-noun phrase
def beginning(mono_preps, nouns_filtered):  
    # Start with an empty list
    l1 = []

    # Randomly generate a preposition using random_word
    prep = random_word(mono_preps)
    # Append it to the list
    l1.append(prep)
    
    # Generate a noun using random_word
    noun = random_word(nouns_filtered)
    # Append it to the list
    l1.append(noun)

    # Join the elements of the list together into a string
    beginning = ' '.join(l1)

    return beginning

# Next let's define a function which makes the middle part of a line
    # We need eleven monosyllabic nouns
def middle(nouns_filtered):
    # Start a counter
    count = 0
    
    # Make an empty list
    l2 = []
    
    # Open a while loop to make a list of eleven randomly-generated nouns
    while count < 11:
        # Generate a noun using random_word
        word = random_word(nouns_filtered)
        # Append the noun to a list
        l2.append(word)
        
        # Count this loop
        count += 1
        
    # Join the elements of the list together into a string
        # Separate by "/"
    middle = ' / '.join(l2)
    
    return middle

# Lastly, let's define a funtion which makes the end of a line
    # Trisyllabic noun phrases, e.g. "Wheat and Bread," "Morning Rays"
def end(nouns_filtered, multi_nouns):
    # Will randomly choose noun-and-noun or multi-noun phrases
        # Value will determine which kind of phrase
    value = rd.getrandbits(1)
    
    # Multi-noun phrase
    if value == 0:
        end = random_word(multi_nouns)
       
    # Make a noun-and-noun phrase
    else:
        # Create an empty list
        l3 = []
        
        # Randomly generate noun 1
        word1 = random_word(nouns_filtered)
        # Append it to the list
        l3.append(word1)
        
        # Generate noun 2
        word2 = random_word(nouns_filtered)
        # Append it to the list
        l3.append(word2)
        
        end = ' and '.join(l3)
        
    return end

# Now let's define a function which creates one entire line
def line(beginning, middle, end):
    # Create an empty list
    l_parts = []
    
    # Make the beginning of the line
    beginning = beginning(mono_preps, nouns_filtered)
    # Append it to the list
    l_parts.append(beginning)
    
    # Make the middle
    middle = middle(nouns_filtered)
    # Append it to the list
    l_parts.append(middle)
    
    # Make the ending
    end = end(nouns_filtered, multi_nouns)
    # Append it to the list
    l_parts.append(end)
    
    # Join each element of the list together, separated by "/"
    line = ' / '.join(l_parts)
    
    return line

# Now let's define a function which writes an entire stanza
    # Four lines
def stanza(line):
    # Create a counter
    count = 0
    
    # Create an empty list
    l_lines = []
    
    # Open a while loop
    while count < 4:
        # Generate a line
        p = line(beginning, middle, end)
        # Append it to the list
        l_lines.append(p)
        
        # Count this loop
        count += 1
      
    stanza = '\n'.join(l_lines)
    
    return stanza

# Lastly, let's define a function which writes an entire Kuhlmannian sonnet
    # Three stanzas
def sonnet(stanza):
    # Create a counter
    count = 0
    
    # Create an empty list
    l_stanzas = []
    
    # Open a while loop
    while count < 3:
        # Generate a stanza
        j = stanza(line)
        # Append it to the list
        l_stanzas.append(j)
        
        # Count this loop
        count += 1
             
    sonnet = '\n'.join(l_stanzas)
    
    return sonnet
        
def Kuhlmann_sonnet(sonnet):
    print(sonnet(stanza))
    
Kuhlmann_sonnet(sonnet)
