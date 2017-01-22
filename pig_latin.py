"""
pig_latin.py (6 points)
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

IPO for to_pig_latin function
-----
input (parameters): a string
processing: convert the string into pig latin
output (return value): a new string (in pig latin)

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""
#define the function and make sure it takes in one parameter.
#make the parameter a string
#convert all the characters in the string to lowercase
#slice the first two words of the string to see if its ch, sh, th
#make multiple if statements to see which if statement is appropriate for each word
#determine the initial eltter of the word
#return the final pig latter word once converted
#if it is not an alphabet return the string as it is! (Return s)
def to_pig_latin(string):
    s = str(string)
    lower_case = s.lower()
    two_letter_result = lower_case[0:2]
    if (lower_case.isalpha())== True:
        if len(lower_case) > 1:
            vowel_result = lower_case[0]
            if vowel_result =="a" or vowel_result =="e" or vowel_result == "i" or vowel_result == "o" or vowel_result =="u":
                pig_latin_word = lower_case+"ay"
            
            elif two_letter_result =="ch" or two_letter_result =="sh" or two_letter_result =="th" or two_letter_result=="qa":
                pig_latin_word = lower_case[2::]+two_letter_result+"ay"
                
            else:
                pig_latin_word = lower_case[1::]+lower_case[0]+"ay"
            return pig_latin_word
        else:
            return s
    else:
        return s

assert "angechay"== (to_pig_latin("change")), "when a word begins with 'ch', 'sh, 'th' or 'qa', the answer should/nremove those letters and place\n them at the end" 
assert "orangeay"==(to_pig_latin("orange")), "when a word begins with a vowel, add ay at the end"
assert "678"==(to_pig_latin("678")), "when a characters are not alphabets do not change anything"
assert "onstonantcay"==(to_pig_latin("constonant")), "with words that are constanants just take the first letter move it to the end and add ayy"
