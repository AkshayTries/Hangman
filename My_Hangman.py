def make_guess(l,newword,word): 
	for i in word:
			if l==i :
				newword[word.index(i)] = i
				if newword==word:
					newword=str(newword)
					print("-----"*16,"\n\n\n\nYou have won the game\n\n\n"+"The word was",list_to_string(word),"\n\n\nEnjoy")
					return newword	
	print("\n",newword,"\n\n\n\n")
	l=input("Make your guess \n")
	make_guess(l,newword,word)		
		  
def intro():
	print("Its HANGMAN\n")
	word = list("farce")
	newword=list("_"*len(word))
	l=input("Make your guess  \n")
	make_guess(l,newword,word)

def list_to_string(word):
	j=""
	for i in word:
		j=j+i
	return j

intro()

