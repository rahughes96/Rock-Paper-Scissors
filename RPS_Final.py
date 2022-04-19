
import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
from time import sleep

def user_choice():

    while True: 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, frame = cap.read()

        frame2 = cv2.flip(frame,1)

        resized_frame = cv2.resize(frame2, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame2)

        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        print(np.argmax(prediction[0]))
        if np.argmax(prediction[0])==0:
            user_choice="Rock"
            return user_choice
        elif np.argmax(prediction[0]) == 1:
            user_choice="Paper"
            return user_choice
        elif np.argmax(prediction[0]) == 2:
            user_choice="Scissors"
            return user_choice
        else:
            user_choice="Nothing"
            return user_choice
               
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def countdown(sec=5):
    total_sec=sec

    while total_sec>0:
        print(total_sec)
        time.sleep(1)
        total_sec -= 1


import random
comp_list=["Rock","Paper","Scissors"]
game_on = True
comp_win_count = 0
play_win_count = 0
Round = 0



while True:

    Round += 1
    print(f"Round {Round}")

    comp_choice = random.choice(comp_list)

    countdown()

    player_choice = user_choice()

    if comp_choice == player_choice:
        print(f"Player: {player_choice} \nComputer: {comp_choice}")
        print("Its a tie")
        game_on=True

    for n in range(len(comp_list)-1):

        if (comp_choice == comp_list[n] and player_choice == comp_list[n-1]):
            print(f"Player: {player_choice} \nComputer: {comp_choice}")

            comp_win_count += 1
            game_on = False

        elif  (player_choice == comp_list[n] and comp_choice == comp_list[n-1]):
            print(f"Player: {player_choice} \nComputer: {comp_choice}")

            play_win_count += 1
            game_on = False


    print(f"Computer: {comp_win_count} Player: {play_win_count}")
    if comp_win_count == 3:
        print("Computer Wins")
        game_on = False
        break

    elif play_win_count == 3:
        print("Player wins")
        game_on = False
        break

again = input("would you like to play again? y/n: ")
if again.lower()=='y':
    game_on = True
elif again.lower()=='n':
    game_on = False
    