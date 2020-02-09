gameMonsters = {
  "bird" : {
    "name" : "Bird",
    "moves" :["peck","swoop"],
    "hp" : 5,
    "xp_given" : 1,
    "drop" : False,
    "fer": 0,
    "acr" : 0
  },
  "angry_bird" : {
    "name" : "Mad Bird",
    "moves" :["peck","swoop"],
    "hp" : 10,
    "xp_given" : 2,
    "drop" : False,
    "fer": 1,
    "acr" : 1
  },  
  "squirrel" : {
    "name" : "Squirrel",
    "moves" :["bite","claw"],
    "hp" : 8,
    "xp_given" : 1,
    "drop" : ["potion", 60],
    "fer": 0,
    "acr" : 0
  },
  "angry_squirrel" : {
    "name" : "Angry Squirrel",
    "moves" :["bite","claw","pounce"],
    "hp" : 12,
    "xp_given" : 2,
    "drop" : False,
    "fer": 1,
    "acr" : 1
  },
  "mouse" : {
    "name" : "Mouse",
    "moves" :["nibble","squeak"],
    "hp" : 5,
    "xp_given" : 1,
    "drop" : False,
    "fer": 0,
    "acr" : 0
  },
  "housemouse" : {
    "name" : "House Mouse",
    "moves" : ["nibble", "squeak"],
    "hp" : 13,
    "xp_given" : 3,
    "drop" : ["catnip", 25],
    "fer" : 2,
    "acr" : 2
  },
  "rat" : {
    "name" : "Rat",
    "moves" : ["nibble", "squeak", "bite"],
    "hp" : 20,
    "xp_given" : 5,
    "drop" : False,
    "fer" : 4,
    "acr" : 3
  },
  "bat": {
    "name" : "Bat",
    "moves" : ["swoop", "squeak"],
    "hp" : 12,
    "xp_given" : 2,
    "drop" : False,
    "fer" : 0,
    "acr" : 2
  },
  "bigbat": {
    "name" : "Big Bat",
    "moves" : ["swoop", "squeak", "claw"],
    "hp" : 18,
    "xp_given" : 5,
    "drop" : False,
    "fer" : 1,
    "acr" : 4
  },
  "rabbit" : {
    "name" : "Bunny",
    "moves" :["bunny"],
    "hp" : 9,
    "xp_given" : 2,
    "drop" : ["bunny ears", 45],
    "fer": 0,
    "acr" : 0
  },
  "snake" : {
    "name" : "Snake",
    "moves" :["slither","hiss"],
    "hp" : 15,
    "xp_given" : 3,
    "drop" : ["snake hat", 25],
    "fer": 0,
    "acr" : 0
  },
  "fish" : {
    "name" : "Fish",
    "moves" : ["splash"],
    "hp" : 6,
    "xp_given" : 2,
    "drop" : ["fish hat", 25],
    "fer" : 0,
    "acr" : 2
  },
  "streetcat" : {
    "name" : "Streetcat",
    "moves" :["bite","claw","kick","barf"],
    "hp" : 15,
    "xp_given" : 3,
    "drop" : ["cat ears", 10],
    "fer": 0,
    "acr" : 0
  },
  "child" : {
    "name" : "Human Child",
    "moves" :["backrub","tailgrab"],
    "hp" : 20,
    "xp_given" : 5,
    "drop" : False,
    "fer": 0,
    "acr" : 0
  },
}
mlist = gameMonsters.keys()