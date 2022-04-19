# Rock-Paper-Scissors

MILESTONE 1

Using teachable machine, a model was built containing four classes to recognise the "rock paper and scissors" symbols, as well as a lack there-of, through the webcam. This created a model which was downloaded from the "Tensorflow". The contents were then unzipped and saved in a directory, which allowed access through Visual Studio Code.


MILESTONE 2

Creating a virtual environment involved downloading the relevant dependencies; Tensorflow, opencv and ipykernel. This was done at the terminal using conda install and pip install.

Using the code provided we are then able to run the model from the previous milestone, checking that it indeed recognises the relevant hand gestures.

<img width="652" alt="Screenshot 2022-04-19 at 19 25 36" src="https://user-images.githubusercontent.com/102994234/164070730-c1fc2e51-39dc-4283-9e39-81106cefb398.png">


MILESTONE 3

To store the users choice, for this stage an input function worked, later to be replaced by the webcams capturing of the hand gesture.

<img width="474" alt="Screenshot 2022-04-19 at 19 23 29" src="https://user-images.githubusercontent.com/102994234/164070424-96c516b6-f4b3-4204-a845-4d44bedb66be.png">

To store the computers choice, this chooses a random element of a list containing the three possibilities, shown below, using the random module. Both the user choice and the computer choice are saved as functions, that are called later during the game code

<img width="281" alt="Screenshot 2022-04-19 at 18 36 07" src="https://user-images.githubusercontent.com/102994234/164062612-8ed86bad-81d7-4c1a-a182-b4ea2976ae34.png">

The game code uses the same list shown above, to decide who wins. Index 'n' of this list, always beats the index 'n-1', so the code uses this fact to compare the user and computer choice, while also checking for a tie. 

<img width="570" alt="Screenshot 2022-04-19 at 18 38 09" src="https://user-images.githubusercontent.com/102994234/164062950-8b570d0c-1f3e-415d-8858-ca812733bcc4.png">


MILESTONE 4

To store the users choice, using the argmax function from numpy to decide which gesture the user was showing, proved more useful than picking whichever entry was above 0.5. 


<img width="306" alt="Screenshot 2022-04-19 at 18 30 09" src="https://user-images.githubusercontent.com/102994234/164061624-edaa5c2d-228e-46a6-ae72-816c26af1b5c.png">

For the image capture to match the model, it needed to be flipped before comparing the two.

<img width="194" alt="Screenshot 2022-04-19 at 18 32 09" src="https://user-images.githubusercontent.com/102994234/164061918-7c4ceabc-b62e-4595-a340-58a87a3e73a4.png">

This was then stored in the form of a function..

<img width="473" alt="Screenshot 2022-04-19 at 19 29 59" src="https://user-images.githubusercontent.com/102994234/164071485-8af8d96c-719e-47a7-a18d-1461496a5642.png">

..Which then replaced the input function in the original game code

<img width="227" alt="Screenshot 2022-04-19 at 19 31 17" src="https://user-images.githubusercontent.com/102994234/164071680-994b570d-57d0-4477-9f7e-31b1de11c357.png">

The game is played best to 3, so the rounds are counted into an empty list as well as the 'win count' for each party. If either 'win count' reaches 3, the game is over and that party wins.

<img width="458" alt="Screenshot 2022-04-19 at 19 20 06" src="https://user-images.githubusercontent.com/102994234/164069929-1a0dfc3d-3dce-4664-b587-4b99857165f0.png">

The game is wrapped in a while-loop, checking if any of the conditions are met for either party to win, the boolean game_on is used to ask the player to play again, and exits the while-loop if not. 

