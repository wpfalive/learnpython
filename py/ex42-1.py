from sys import exit
from random import randint

class Game(object):
    def __init__(self, start):
        self.quips = [
            "You died. you kinda suck at this.",
            "Your mom would be proud. If she were smater.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]

        self.start = start

    def play(self):
        next = self.start
from sys import exit
from random import randint

class Game(object):
    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mon would be proud. If she were smarter.",
            "Such a laser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n--------"
            room = getattr(self, next)
            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print "The Gothons of Planet Percal #25 have invaded"
        print "your ship and destroyed your entire crew."
        print " You are the last surviving member and your last"
        print " mission is to get the neutron destruct bomb from"
        print " the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting"
        print " into an escape pod"
        print "\n"
        action = raw_input("> ")

        if action == "shoot!":
            print "you are dead. Then he eats you."
            return 'death'
        elif action == "dodge!":
            print "eats you."
            return 'death'
        elif action == "tell a joke":
            print "enter laser weapon armory"
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet"
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print code
        guess = raw_input("[keypad]> ")
        guesses = 0

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from thier ship and you die."
            return 'death'

    def the_bridge(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprises 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They havent't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try disarm"
            print "the bomb. You die knowing the will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweet."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the closse button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return "escape_pod"
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

    def escape_pod(self):
        print "You rush throught the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly and Gothons are on the ship, so your run is clear of"
        print "interfreence. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1, 5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return "death"
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into sapce heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            exit(0)

a_game = Game("central_corridor")
a_game.play()
