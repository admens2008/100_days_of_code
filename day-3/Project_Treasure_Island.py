print('''       __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

where = input("Where do you want to go? Left or Right: ").lower()
if where == "left":
    next = input("Good! What do you want to do next? SWim or Wait: ").lower()
    if next == "wait":
        door = input("Excellent! Which door? Blue or Red?: ").lower()
        if door == "yellow":
            print("Marvelous! YOU WIN! CONGRATULATIONS!")
        elif door == "red":
            print("DISASTER! Burned by FIRE! GAME OVER!")
        elif door == "blue":
            print("BRRRRR! Eaten by BEASTS! GAME OVER!")
        else:
            print("SAD! GAME OVER!")
    else:
        print("Attacked by trout! GAME OVER!")
else:
    print("Fall into a hole. GAME OVER!")