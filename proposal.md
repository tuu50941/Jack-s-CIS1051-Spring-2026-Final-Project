# Proposal

## What will (likely) be the title of your project?

Babble

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

I will make a board which allows you to place letters upon it, giving one or two players points as they make words, similar to the board game, Scrabble.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My software will function similar to how the Scrabble board game is played, swapping between two players as it does so. To do this, a simple boolean variable could likely be used. Players can place letters on the board and once they have told the program they have finished their word, they can be attributed points based on the point value of each letter used. Dictionaries could be used to store the point values of each letter as well as the quantity of each letter so that, for example, 2 x's are not placed on the board when there are only 1 in the original game. Both players will be given 7 random letters at the start of the game and at the end of each turn be given more random letters until they have 7 again. Each time a letter is randomly selected, the program should subtract 1 from its quantity in the letterQuantity dictionary similar to how you would reach into the letter pouch to get more when playing the board game. To ensure that the program knows which player has which letters, lists could be given to each player. Lastly, there should be some system set in place that would allow the program to keep track of other words on the board so that letters could be placed between them to form new ones. 

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

Not combining with another course's final project.

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

I am not planning to collaborate with other classmates.

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

Have a functional Scrabble-inspired board game that follows most of the real rules of Scrabble and knows how letters should be properly placed, while subtracting the quantity of those letters each time and giving players points at the appropriate times. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

Have a functional Scrabble-inspired virtual game that follows most of the real rules of Scrabble and has an option to be played between 2 and 4 players. 

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

Have a fully functional virtual Scrabble game that uses AI to access a dictionary to check the validity of words.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I would first need to look into how to use pygame. Through pygame, I can figure out how to efficiently create an interactive visual board since using a turtle in IDLE and trying to figure out which spots would have to be clicked would be very ineffecient. Next, to ensure the game is set up correctly, I could create a letterPoints dictionary, a letterQuantities dictionary, two empty lists that will be used later to store letters for each player, and a isPlayerOneTurn variable that can be used to swap between the two players.
