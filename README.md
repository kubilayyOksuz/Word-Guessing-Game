<h1>Word Guessing Game</h1>
This is a game I wrote on Python and actually the first script I've written without any help from YouTube or any other sources.
<h1>Requirements</h1>
<ul>
<li>random module</li>
<li>words.py</li>
</ul>
<h1>How to Build</h1>
I found a list of English words and put them in a file I named words.py. Then I imported the file, and the random module, to my main game file.
<h1>How Does It Work</h1>
The computer chooses a random word from the list and gives the user the length of the word it chose. Then the user enters a character, a letter or "-", and the computer tells the user if the character is in the word or not. The user can see the characters that have been used. If the character is in the word, the computer tells how many times the character is in the word. Every time the user enters an input, the computer asks the user if the user would like to take a guess.
<br>
<br>
The computer counts how many times the user entered a character or how many times the user took a guess. The computer offers a clue every three tries but only offers three clues. If the user doesn't take the clue, the user's tries gets reduced by three. After 15th try, the game is over.
