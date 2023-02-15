#Amusing Joke
#Brute force solution.
#First. The name is compared char by char with the pile, counting every equal character.
#Second. Then the residence is compared, if all characters are in the pile the program will print YES.
#IF THERE ARE A CHARACTER DIFFERENT THE PROGRAM WILL PRINT NO

def solution():
    #input
    name = input()
    residence = input()
    letters = input()
    #Adding elements from the pile in a list
    pile = []
    for char in letters:
        pile.append(char)
    #Comparing the name, if it is in the pile it will be removed
    for char in name:
        if char in pile:
            pile.remove(char)
        else:
            return 'NO'
    #Comparing the residence, if it is in the pile it will be removed
    for char in residence:
        if char in pile:
            pile.remove(char)
        else:
            return 'NO'
    #If the list is empty will be printed SYES
    if not pile:
        return 'YES'
    else:
        return 'NO'
def main():
    print(solution())

if __name__ == "__main__":
    main()