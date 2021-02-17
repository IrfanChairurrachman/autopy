def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  new_text = []
  for word in words:
    # Create the pig latin word and add it to the list
    new_word = word[1:] + word[0] + "ay"
    # Turn the list back into a phrase
    new_text.append(new_word)
  return ' '.join(new_text)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"