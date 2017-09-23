from sys import exit
import random


class Scene(object):

    def enter(self):
        print "This is an error"
        exit(1)


class Begin(Scene):

    def enter(self):
        print "You are Harry Potter, and you, Ron and Hermione have decided"
        print "to stop Snape from getting the Philosopher's stone for Voldemort"
        print "by going through the trapdoor and getting the stone first."
        print "Good luck!\n"
        return 'fluffy_room'


class FluffyRoom(Scene):

    def enter(self):
        print "You, Ron and Hermione are in the room with Fluffy the three-headed dog."
        print "You need to play a song to make Fluffy go to sleep. Compose a song using"
        print "the notes a, b, c, d, e, f, or g in any combination you want (you don't"
        print "have to use every note). But Fluffy will only go to sleep if he likes your"
        print "song! And each head has a favorite note that it wants to hear. The favorite"
        print "notes change every day, along with the number of times the note needs to"
        print "be played to satisfy that head. Sometimes a head will be satisfied with"
        print "hearing its favorite note once, or it might want to hear it up to 3 times."

        # randomly select fluffy's favorite notes and how many times to play it
        notes = ["a", "b", "c", "d", "e", "f", "g"]
        fav_notes = random.sample(notes, 3)

        note_times = []
        for i in range(3):
            note_times.append(random.randint(1,3))

        # compose your song
        song = []

        for i in range(15):
            print "Play note %i for your song" % (i + 1)
            note = raw_input("> ")
            if len(note) > 1:
                print "One note at a time please!"
            elif note not in "abcdefg":
                print "Those aren't even musical notes! You'll never get Fluffy to sleep that way."
            else:
                song.append(note)
        print "Your song is:", " ".join(song)

        # check if Fluffy's favorite notes are in your song enough times
        x = 0
        for i in fav_notes:
            note_count = song.count(i)
            if note_count >= note_times[x]:
                x += 1
            else:
                print "Fluffy doesn't like your song! He refuses to fall asleep!"
                return 'failed'

        print "Fluffy likes your song! He goes to sleep, and you, Ron and Hermione"
        print "sneak through the trap door."
        return 'devils_snare_room'


class DevilsSnareRoom(Scene):

    def enter(self):
        print "\n"
        print "You fall through the trap door onto a plant which turns out to be"
        print "Devil's Snare! You, Ron and Hermione become entangled in the deadly"
        print "plant! What do you do?"

        calm = False
        panic = False

        while True:
            action = raw_input("> ")

            if "calm" in action or "still" in action:
                print "You remember from Herbology that Devil's Snare works more quickly"
                print "the more you struggle so you stay calm and move as little as possible."
                calm = True
            elif "panic" in action:
                print "You can't remember anything about Devil's Snare and you start to panic!"
                print "The more you panic, the tighter the plant ensnares you!"
                panic = True
            elif "fire" in action and panic:
                print "The Devil's Snare wraps even more tightly around you, so that"
                print "you can't even move to cast a spell!"
                return 'failed'
            elif "fire" in action and not calm:
                print "You go to light a fire but the more you move, the more tightly the"
                print "Devils' Snare wraps around you!"
                panic = True
            elif "fire" in action and calm:
                print "You also remember from Herbology that Devil's Snare likes the"
                print "cold and damp, so you light a fire. The plant shrinks back from"
                print "the warm flames and you, Ron and Hermione are able to escape."
                print "You find a door and the three of you go through it."
                return 'key_room'
            else:
                print "...What?"


class KeyRoom(Scene):

    def enter(self):
        print "\n"
        print "You, Ron and Hermione enter a room filled with flying keys. There's"
        print "another door across the room, but it's locked. You need to catch the"
        print "key that opens the door using the provided broomsticks. You look at"
        print "the keys and notice one with a damaged wing. That's probably the one"
        print "you need!"

        # make key area
        keys = []
        for i in range(5):
            keys.append(["o"] * 5)

        def print_keys():
            for row in keys:
                print " ".join(row)
            print "\n"

        # see the key with damaged wing
        h = random.randint(0,4)
        w = random.randint(0,4)
        keys[h][w] = "F"
        print_keys()

        print "The key can move in any direction (up, down, sideways, diagonal) but"
        print "it can only move one space at a time (or it might not move at all)."
        print "To catch the key, correctly guess where it will move next by entering"
        print "a number from 0 to 4 corresponding to the row (top to bottom) and then"
        print "column (left to right) where the key could be."

        # make the key move; repeats until they catch the key
        while True:
            keys[h][w] = "o"
            h = h + random.randint(-1, 1)
            while h > 4:
                h -= 1
            while h < 0:
                h += 1
            w = w + random.randint(-1, 1)
            while w > 4:
                w -= 1
            while w < 0:
                w += 1
            keys[h][w] = "F"

            # they guess where the key is
            print "Enter the number (0 to 4) of which row you think the key will be in."
            guess_row = raw_input("> ")
            print "Enter the number (0 to 4) of which column you think the key will be in."
            guess_col = raw_input("> ")

            print_keys()

            if int(guess_row) == h and int(guess_col) == w:
                print "You caught the key! Now you can open the door."
                return 'chess_room'
            else:
                print "The key eludes you!"


class ChessRoom(Scene):

    def enter(self):
        print "\n"
        print "In this room is a giant chess board and you must play your way across."
        print "Luckily Ron is basically a chess prodigy, so he can direct you and"
        print "Hermione in what to do. Ron gets most of the important chess pieces,"
        print "but he wants you to get as many pawns as possible. To go after the pawns"
        print "enter either 0 or 1. You must get at least 5 pawns to win."

        count = 0
        for i in range(10):
            pawn = random.randint(0, 1)
            print "Attempt #%i" % (i + 1)
            guess = raw_input("> ")
            try:
                guess = int(guess)
            except ValueError:
                guess = -1
            if guess > 1 or guess < 0:
                print "The instructions were very clear! Pick either 0 or 1!"
            elif guess == pawn:
                print "You got a pawn!"
                count += 1
            else:
                print "You didn't get a pawn."

        if count >= 5:
            print "You got enough pawns! You are able to win the chess game, but"
            print "Ron has to sacrifice himself in order for you to get the King."
            print "He is knocked out by the Queen, and you and Hermione go on to"
            print "the next room without him."
            return 'troll_room'
        else:
            print "You didn't get enough pawns, and you lose the chesss game."
            return 'failed'



class TrollRoom(Scene):

    def enter(self):
        print "\n"
        print "You and Hermione enter a room which has a huge troll in it! The troll"
        print "is holding a large club and appears to just be waking up from being"
        print "previously knocked out. You'll have to fight it to get to the next room!"

        confused = False
        count = 0

        while True:
            action = raw_input("> ")

            if count > 4:
                print "The troll becomes fed up and decides to tackle you!"
                return 'failed'
            elif "throw" in action:
                print "You and Hermion start throwing anything you can find at the troll."
                print "It doesn't really hurt the troll, but since there are two of you"
                print "it keeps changing its mind about who to go after."
            elif "yell" in action or "shout" in action:
                print "You start yelling, hoping to confuse the troll. The noise echoes"
                print "around the room and the troll can't figure out where it's coming"
                print "from. You have successfully confused the troll!"
                confused = True
            elif action == "wingardium leviosa" and not confused:
                print "You try casting 'Wingardium Leviosa' on the troll's club (it worked"
                print "on the troll at Halloween) but the troll has too firm a grip on its"
                print "club! You need to distract or confuse it first."
            elif action == "wingardium leviosa" and confused:
                print "While the troll is still confused, you cast 'Wingardium Leviosa'"
                print "on its club. The club soars into the air, then falls back down"
                print "on the troll's head with a huge CRACK. The troll is out cold!"
                print "You and Hermione can enter the next room."
                return 'potion_room'
            elif action == "alohomora":
                print "In a panic, you shout the first spell you can think of: 'ALOHOMORA!'"
                print "To your surprise, the spell unbuttons the troll's trousers and they"
                print "fall down, causing him to trip and fall! The troll is very disoriented."
                confused = True
            elif action == "lumos":
                print "In a panic, you shout the first spell you can think of: 'LUMOS!'"
                print "The end of your wand lights up. That's not helpful in this situation!"
            else:
                print "...What?"
            count += 1


class PotionRoom(Scene):

    #this is a variation of the Monty Hall problem
    def enter(self):
        print "\n"
        print "In this room there are 7 potion bottles lined up on a table, and"
        print "fires spring up to block both the way on and the way you came."
        print "There's a piece of parchment with a riddle about which bottle holds"
        print "the potion which will allow you to pass through the fire to go onward"
        print "or backward. Hermione starts reading the riddle, but you decide to"
        print "try picking one of the bottles at random. (Choose a number 1 to 7.)\n"
        print "Which bottle do you choose?"

        # sorts bottles into either keep or eliminate
        # if they guessed correct bottle eliminate will have 6 instead of 5
        # this works better than other methods tried because if you pop only keep
        # bottles or only eliminate bottles then it screws up when the indexes
        # shift or if they initally guessed correctly
        bottles = [1, 2, 3, 4, 5, 6, 7]
        guess_bottle = int(raw_input("> "))
        true_bottle = random.randint(1,7)
        eliminate = []
        keep = []

        for i in range(7):
            bottle = bottles.pop()
            if bottle == guess_bottle or bottle == true_bottle:
                keep.append(bottle)
            else:
                eliminate.append(bottle)

        random.shuffle(eliminate)

        print "Hermione has been able to determine from the riddle the contents"
        print "of some of the bottles. She has been able to narrow it down to two"
        print "of the bottles, one of which is the bottle you randomly selected."
        print "Hermione eliminates:"
        # even if eliminate has 6 it only prints out 5 (usually it should have 5)
        for i in range(5):
            x = eliminate.pop()
            print "bottle #%i" % x

        print "Do you want to switch to the other bottle or stick with your"
        print "original choice? (Enter the number of the bottle you choose.)"

        guess_bottle = int(raw_input("> "))

        if guess_bottle == true_bottle:
            print "You picked the correct bottle! But there is only enough potion"
            print "for one person, so you decide that you'll go on alone and Hermione"
            print "will go back and get Ron and try to send an owl to Dumbledore."
            return 'mirror_room'
        else:
            print "You picked the wrong bottle."
            return 'failed'


class MirrorRoom(Scene):

    def enter(self):
        print "\n"
        print "You enter the final room to find, to your surprise, not Professor"
        print "Snape but Professor Quirrell! He's been working for Vodemort all"
        print "along! Not only that, but Voldemort's face is stuck on the back of"
        print "Quirrell's head underneath his turban! Also in the room is the Mirror"
        print "of Erised, which you know from previous experience will show you the"
        print "thing you want most in the world."


        distracted = False
        aware = False
        while True:
            action = raw_input("> ")

            if "talk" in action or "question" in action:
                print "You try to distract Quirrell by asking him about his evil plan"
                print "and acting sufficiently impressed. Like any good villain, he"
                print "starts monologuing. Maybe you'll get a chance to look in the"
                print "mirror while he's distracted!"
                distracted = True
            elif "mirror" in action and not distracted:
                print "You try to look in the mirror but Quirrell notices what you are"
                print "up to and stops you."
                return 'failed'
            elif "mirror" in action and distracted:
                print "You know the mirror will show you what you want most in the world,"
                print "and right now what you want most in the world is to find the stone"
                print "before Quirrell, so if you look in the mirror, you should see"
                print "yourself finding it, and you'll know where it's hidden! While"
                print "Quirrell is still monologuing, you look into the mirror and see...\n"
                print "...yourself, holding the stone! Mirror you puts the stone in your"
                print "pocket, and miraculously, you feel the stone in your real pocket!\n"
                return 'final_boss_battle'
            else:
                print "...What?"


class FinalBossBattle(Scene):

    def enter(self):
        print "\n"
        print "You're wondering if you can make a break for it with the stone,"
        print "when Voldemort starts talking to you from the back of Quirrell's"
        print "head. He tries to convince you to join him but you refuse because"
        print "he murdered your parents. Then he tells Quirrell to attack you,"
        print "but Quirrell can't touch you without being burned. You realize"
        print "your only hope is to hold onto Quirrell for as long as possible,"
        print "even though doing so also puts you in agonizing pain."
        print "\nYou grab onto Quirrell; he is being burned, but you are also in"
        print "terrible pain. You can give up, or keep fighting for as long as you"
        print "can. (To keep fighting enter a number from 1 to 10. To give up enter"
        print "'give up'.)"

        while True:
            print "\nQuirrell is still trying to attack you, and you're in incredible"
            print "pain! Keep fighting or give up?"

            action = raw_input("> ")
            win = random.randint(1,10)

            if action == "give up":
                print "You just can't take any more, and stop fighting."
                return 'failed'
            elif int(action) == win:
                print "You keep fighting through the pain, but eventually you pass out.\n"
                print "You wake up in the hospital wing with Dumbledore, who says"
                print "you held Quirrell off just long enough for him to come rescue"
                print "you! Quirrell has died, Voldemort fled, and Nicolas Flamel has"
                print "decided to destroy the Philsopher's stone to keep Voldemort from"
                print "ever getting it."
                return 'finished'
            else:
                print "You keep fighting, even though your head feels like it's about"
                print "to split open."


class Failed(Scene):

    def enter(self):
        print "\n"
        print "You failed to stop Voldemort getting the stone! His imminent return"
        print "will usher in a new Dark era marked by fear and death."
        print "Play again? Or give up and accept your fate?"

        action = raw_input("> ")

        if "play" in action:
            return 'begin'
        else:
            print "So be it. YOU LOSE."
            exit(0)


class Finished(Scene):

    def enter(self):
        print "\nYou stopped Voldemort from getting the stone! Good job!"
        exit(0)
