# ** Hangman project
-----------------------------------------------------------------------------------
first project learning code, with the use of the following technologies: VS Code, Python, Git, Github and other minipackages such as PYtest.

## Milestone 1.0
-----------------------------------------------------------------------------------
- Using python built in functions I have created a list containing 5 of my favourites fruits. By coding certain characters I am able to use different like the list[] function or the print() function as demonstrated below.

![](milestone.png)



## Milestone 1.1
---
- In this milestone I used a theh Python built-in *import random* module which allows the user to return a rnadom item from a given sequence through the *choice* method. By using *random.choice* method and passig the *word_list* from milestone 1 as the *choice* variable it allows us to randomly generate a word from *word_list*. I assigned the generated word to the variable *word*

![](milestone1.png)


## Milestone 1.2
---
- In this milestone I used the *input* function to get the user to input a single letter in the from a string which I assigned the variable *guess*. To validate the input I used ab *if* statement to make a conditional that the input should be a single alphabetical letter. If the condition is met, I used the *print* function to  print "Good Guess!". if the conditional is not met I used the *else* block to print "Oops! That is not a valid input."

![](milestone3.png)

## Milestone 2.0
-----------------
- In this task I created a code that will continuously ask the user for a letter and validate it.
- By creating a while loop with the condition set to true allowed the code to run continuously. In the body of the while loop I  wrote the code for the following steps instructions:
    - Asking the user to guess a letter and assigning it to the guess variable.
    - Checking the guess is a single, alphabetical character.
    - Break out of the loop if the guess passes the checks.
    - By utilisng the use of else statement if the guess does not pass the checks, print a message saying "Invalid letter. Please, enter a single alphabetical character."

![](milestone2t1.png)

## Milestone 2.1

- In this task I had to check whether the letter guessed by the user is in the secret randomly chosen word generated by the computer. e.g. if the user guesses the letter "r" and the secret word is "serene", then the code checks if "r" is in "serene".
- To accomplish this I created an if statement to check if the guess is in the word. In the body of the if statement, I created code to print a message saying "Good guess! {guess} is in the word.". For {guess} I used the .format function to show the actual guess type by the user. I then created an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." if the guess is not in the word.

![](milestone2t2.png)


## Milestone 2.2

### In this part of the task I had to create 2 functions: check_guess and ask_for_input functions. 
- The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
    - I defined a function called check_guess. Then passed in the guess as a parameter for the function.
    - In the body of this function I wrote a code to convert the guess into lower case.
    - I then moved the code I wrote to check if the guesss is in the word into this function block.

![](milestone2t3.png)


- The ask_for_input function will ask the user for inpout.
    - I defined a function called ask_for_input.
    - I then moved the code to Iteratively check if the input is a valid guess task 
    - I called the check_guess function to check if the guess is in the word into this function block, but outside the while loop and passed in the guess as an argument to the method.
    - I then called the ask_for_input function to test your code outside the function.

![](milestone2t3.png)

## Milestone 3.1 - Creating class
---
- For this I had to create a Hangman *class*. As the pictures below displays. *CLass* allows the means of bundling data and functionality. This created a new object which allowed for *instances* of that object to made. Each instance of the object has an *attribute* attached to it to maintain its state. However class instances can have methods (Defined by its class) which allow its state to be modified (refer to Milestone 3.2). Through watching the prerequisite content and more research and actually applying trial attempts to code myself did I start understanding the basics of what a class does.



![](hangman_class.png)
![](hangman_attributes.png)

## Milestone 3.2 - Methods for running checks 
---
*method is a function that is defined inside a class.*

- I created 2 methods:
    1. a method that will ask the user to guess a letter and that will check if the guess is in the word:
        - to create this method I used the *def* function to create the *check_guess_method* and passed the word guess as the parameter.
        - In the body of the method, I created for: 
            -converting the guessed to lower caser using the *.lower* function which returned the letter in minuscule case.
            - I created an if statement that checks if the guess is in the word. If this was true in the body of the statement I wrote code to print "Good guess! {guess} is in the word." By using the *{}* and passing guess though  it allows me to format the string and print the letter guessed by the user.

    2.  a method that will check if the guess is in the word:
        - Again I used the *def* function to create the *ask_for_input* and wrote th following code in the body:
            - a while loop with the condition set to true.(refer to ask_for_input.png)
            - I asked the user to guess  a letter and assigned it the varible guess through the *input()* which will display the message guess a letter but return the letter guessed by the user.
            - I created an *if* statement that runs if the guess is NOT a single alphabetical character by implimentign the buit in *ascii_lowercase* to ensure the guesss is a letter and not a number or other charater:
                - In the body of the if statement, I wrote code printing "Invalid letter. Please, enter a single alphabetical character."
            - I created an *elif* statement that checks if the guess is already in the list_of_guesses. THis was done using in function whcih allowed me to pass guess through the list_of_guesses  and check if the letter has already been used by the user:
                - In the body of the elif statement, I wrote code printing "You already tried that letter!".
            -However if the guess is a single alphabetical character and it's not in the list_of_guesses:, I created an else block and called the check_guess method and passed the guess as an argument.
            - I wrote code to add the guess to the list_of_guesses which I achieved by imploying *.append()* which appended the guess to list_of_guesses.
            - I then called the ask_for_input method to test your code. To do this I *game* to instantiate the class and passed thtough wordlist as a parameter. I followed this up by calling game.ask_for_input().

![](check_guess.png)
![](ask_for_input.png)

## Milestone 3.3 - What happens if the letter is in word
---
- In this task I extend the check_guess_method to replace the underscore(s) in the word_guessed with the letter guesssed by the user.In the if block of your check_guess method, after your print statement:
    -I created a *for-loop* that will loop through each letter in the word using the *indexing* function which allows me to refer to an element of an iterable by its position within the iterable and the *enumarate()* function which adds a counter to an iterable and returns it in a form of enumerating object. 
        - Within the for-loop, i proceeded:
            -to create an *if* statement that checks if the letter is equal to the guess through the use of *==* operator that compares the value or equality of two objects.
                - In the if block, I replaced the corresponding "_" in the word_guessed with the guess, by *indexing* the word_guessed at the position of the letter and assign it to the letter. This was acheived buy assiging the *word_guessed [indx]* to the letter.
        - Outside the for-loop, I reduce the variable num_letters by 1.


![](loop_indexing.png)

## Milestone 3.4 What happens if the letter is NOT in word
---
- In this task I had to define what happens if the guess is not in the word you are trying to guess:
    -In the check_guess method, I created an *else* statement. Within the else block:
        - I reduced the `num_lives' by 1.
        - Then I wrote code to print "Sorry, {letter} is not in the word."
        - and again wrote code to print another message saying "You have {num_lives} lives left." By using the *{}* in this code allows me to format string and print the value of num_lives.
    - Outside the else, I appended the guess to the list_of_guesses using the *.append()* to ensure that the letter can be appended to the list_of_guesses in both conditions.



![](task_4.png)

## Milestne 4.0 Coding the logic of the game
---
- In this task I had to ceate code that will put the game together and allow it to run. To achieve this I had to create a function that will run all the code. I createa a new script called milestone_4.py, I copied and pasted all the codes in milestone_3.py file into the newly created milestone_4.py file.

- Below that *def* (define) a function called play_game with the word_list as the3 parameter. Inside the function. I wrote code for the following steps:
    - I created an *instance* of the Hangman class by calling the Hangman class and assigning it to a variable called *game*. I purposely did not copy this code to not repeat myself.
    -In the instance of the class I passed *word_list and num_lives* as arguments to the game object. 
    - Below I created  a while loop and set the condition to True, in  the body I wrote code for the following:
        1. To check if the 'num_lives'is equal to 0, I used the  *==* equals to operator which if it was true I wrote code to print a message saying 'You lost!' meaning the game has ended and the user lost.
        2. Secondly, I had to check if the 'num_letters' is greater than 0 andto accomplish this I used the *>+* equal to or greater than operator and set the value to 1. If theere was 1 or more letters still in num_letters then I to called the 'ask_for_input' method for this instance so the user can continue playing the game. 
        3. Lastly, I had to check if the'num_lives' is not 0 and the 'num_letters' is not greater than 0. To achive this I employed  the *>=* equal/greater than operator to chek if the num_lives was equal to or more than 1 and the *==* equal too operator to check if the num_letters was equal to 0. If these conditions were true then the user will have won the game. However, n this step I encontoured an issue in my code as the value assigned to the num_letters was an int but some of the words had double letters which resulted in the code continously asking the user to guess a letter even when they had completed the full word or the code wouldn't print.To rectify this I uodated the code in attributes of the Hangman class to change the value of num_lives to a set. This allowed me to check if the guessed letter was present in 'num_letters'. if the letter was present I employed the *.remove()* method and passed guess as a variable through it to remove the character that matched it in the set even if it was more than one letter. This then allowed me use the *len()* function with num_lives through it to use *==* operator in the if statemant so it could run smoothly and have an end. I then wrote code to print a message saying 'Congratulations. You won the game!'.
- Outside the function, to play the game I had to call the play_game function  and pass in 'word_list" as argument to the function to be able to play the game.







![](task_5.png)
## Conclusion 
---
- From my understanding of the project so far is that most of the tools needed to write code are there it is matter of learning and trying different approaches to problems. As the project progresses I'm understanding how the small pieces of code (statements and while loops) are used to create other bigger codes (functions).
- From building the Hangman class I can see why the object oriented programming is vital to coding as it makes handling large code easier by providing the user simpler, consistent structures. 
- I have also learnt that code maybe function as designed and there maybe values or indents in the wrong place that affect how the code runs, being able to systematically where the error occurs with help of python errors will be an excellent tool to master. 
- From this project I have learnt the basics methods, operators, and functions of python and how they interact together to build a bigger picture. As I immerse myself in more of the basics and hoing over the prerequisite knowledge the more I learn and start to see the peices fit in it together.




