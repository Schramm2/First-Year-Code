def to_pig_latin(sentence): #Function to convert a english sentence to piglatin
    """Function to turn a sentence to piglating"""
    words = []
    words = sentence.split(" ")
    for i in range( 0, len(words)):
        wordOnTrial = words[i]
        
        if wordOnTrial[0:1] == 'a' or wordOnTrial[0:1] == 'e' or wordOnTrial[0:1] == 'i' or wordOnTrial[0:1] == 'o' or wordOnTrial[0:1] == 'u':
            words[i] = words[i] + "way"
        else:
            for letter in wordOnTrial:
                if letter in "aeiou":
                    position = wordOnTrial.find(letter, 1)
                    break
            
            words[i] = wordOnTrial[position: len(wordOnTrial)+1] +"a" +wordOnTrial[0: position] + "ay"
    
    pigLatin = " ".join(words)
    return pigLatin


           
def to_english(sentence): #Function to convert a piglatin sentence to english
    words = []
    words = sentence.split(" ")
    for i in range(0, len(words)):
        wordOnTrial = words[i]
        if "way" in wordOnTrial:
            words[i] = wordOnTrial[0: len(wordOnTrial)-3]
        else:
            wordOnTrial = wordOnTrial[0:len(wordOnTrial)-2]
            
            words[i] = wordOnTrial        
            constonants = []
            constonants = wordOnTrial.split("a")[::-1]
            beginning = constonants[0]
            words[i] = beginning + wordOnTrial[0: wordOnTrial.find(beginning)-1]
            
           
            
    
    
    english =  " ".join(words)
    return english



