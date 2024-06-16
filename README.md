A project inspired by tech with tim
https://www.youtube.com/watch?v=th4OBktqK1I&list=WL&index=61&ab_channel=TechWithTim

I did it a bit more complicated, added object oriented programming and design patterns.
the game is a "one armed bandit" style game, the rules are simple:

The user puts a bet in the machine, then puls the trigger down, which starts the spin of the wheels.
there are three or more wheels with symbols on them from different types. 
some symbols give money, some affect the amount given by others, some form combinations. for example the famous 777
is a combination of the "jack pot" which gives the highest amount of money to the user no matter the bet he placed.
https://en.wikipedia.org/wiki/Slot_machine


The user is asked for a bet. the machine has a table of winning, where the user can see what he will be paid if he wins.
the win is bet times the pay table's value.

It looks like that: the user bet $10, then spined the wheel
He got this:

║  🍒  🍉  🍉  ║
║  🍓  🍉  🍓  ║
║  🍉  🍉  🍒  ║

In that case The user gets $40. His bet times 4, because he has two combinations of watermelons diagonal and straight upwards


Pay table: if any 3 (horizontal, vertial, or diagonal) has this combination (combinations are multiplied!):

7️⃣ 7️⃣ 7️⃣ - jack pot! the user gets the jack pot
🍒 🍒 🍒 - X40
🍓 🍓 🍓 - X10
🍉 🍉 🍉 - X2


👑 - if the crown is on the board the user gets: 
                                                X10 for a crown or a flower
                                                X7 for each 7
                                                X3 for each cherry
                                                X2 for each strawberry
                                                X1 for each watermelon
                                                all combinations are ignored



🌸 - if the flower is on the table combinations ignore placement,
that means that for each 3 of any kind the combination will be applied,
but the flower is ignored if there is a crown