from sys import exit
from random import randint

prompt = "> "
misunderstand = "What does that even mean?! Go back and please rephrase your answer."
treasure_var = False
song_var = False
rebellious_var = False
responsible_var = False
promise_var = False
hook_var = False
suspicion_var = False
bestfriend_var = True
shipparts_var = False
zombonus_var = False

def start():
    print "Welcome to outer space!"
    print "Would you like to be a pirate or a law-abiding citizen?"
    pirate = raw_input(prompt)
    while pirate != "pirate":
        if "citizen" in pirate:
            print "Are you sure? Being a law-abiding citizen is boring :P"
            pirate = raw_input(prompt)
        else:
            print "That wasn't one of the choices! Stop fooling around."
            pirate = raw_input(prompt)
    print "Good choice! 'Tis a pirate's life for you!"
    planet()


def planet():
    print "You're an illustrious pirate flying through outer space in your spaceship with your crew."
    print "You come across an unguarded planet filled with unimaginable treasure."
    print "Do you fly down to the surface to check it out or assume it's a trap and fly away?"
    tr_planet = raw_input(prompt)
    if "surface" in tr_planet:
        planet_surface()
    elif "away" in tr_planet:
        privateers()
    else:
        print misunderstand
        planet()

def planet_surface():
    print "You fly down to the planet's surface."
    print "There's more treasure here than you've ever seen in your life!"
    print "Do you load up as much treasure as you can carry or go explore the planet?"
    treasure = raw_input(prompt)
    if "treasure" in treasure:
        treasure_sit()
    elif "explore" in treasure:
        explore_planet()
    else:
        print misunderstand
        planet_surface()

def treasure_sit():
    print "You start loading treasure into your ship."
    print "There's fabulous jewels, precious metals, rare crystals and space rocks."
    print "Out of the corner of your eye you see it:"
    print "It looks like a small, simple blue cube, but it calls to you."
    print "You find its pull irresistible. Should you take it?"
    global treasure_var
    treasure_var = True
    song_cube = raw_input(prompt)
    double_no = False
    triple_no = False
    while True:
        if song_cube == "yes":
            global song_var
            song_var = True
            print "Your surroundings seem to vanish for a split second."
            print "You hear what can only be described as the most beautiful song in the world."
            print "Then in a flash it's gone, and even as you ponder it, it fades from your memory."
            print "The cube has vanished."
            leave_planet()
        elif song_cube == "no" and triple_no:
            leave_planet()
        elif song_cube == "no" and not double_no:
            print "The cube is calling you. You want to take it so bad!"
            print "Will you take it?"
            double_no = True
            song_cube = raw_input(prompt)
        elif song_cube == "no" and double_no:
            print "You've never wanted anything in your life as badly as you want the cube."
            print "The temptation is nearly unbearable."
            print "Will you take it?"
            triple_no = True
            song_cube = raw_input(prompt)

def leave_planet():
    print "You load up as much treasure as will fit on your ship."
    if song_var:
        print "As you're exiting the planet's atmosphere, two alien beings appear suddenly on your ship."
        print "They appear very imposing and you feel a cold dread steal over you."
        print "Do you throw yourself at their mercy or stand your ground?"
        answer_aliens = raw_input(prompt)
        if "mercy" in answer_aliens:
            print "You promise to return everything you stole and beg the aliens' forgiveness."
            print "You are quite eloquent."
            aliens_speak()
        elif "stand" in answer_aliens:
            print "You stand your ground. You have your dignity!"
            print "You demand to know what these strange beings want,"
            print "insisting the treasure was out in the open for anyone to take."
            global rebellious_var
            rebellious_var = True
            aliens_speak()
        else:
            print misunderstand
            leave_planet()
    else:
        privateers()

def aliens_speak():
    print "The aliens say, 'Silence! We care not for these material objects;"
    print "'What concerns us is the _____.'"
    print "The last word doesn't translate and sounds like a loud buzzing."
    print "Do you deny taking whatever it is, or take responsibility and promise to return it?"
    promise = raw_input(prompt)
    if "deny" in promise and rebellious_var:
        print "You angrily deny any knowledge of what they're talking about."
        print "Unfortunately you have spoken disrespectfully to the aliens one too many times."
        dead("The aliens suck out your brain and you die.")
    elif "deny" in promise and not rebellious_var:
        print "You angrily deny any knowledge of what they're talking about."
        ultimatum_sit()
    elif "promise" in promise or "responsibility" in promise:
        print "You promise to give it back if they'll tell you what it is and how."
        global responsible_var
        responsible_var = True
        ultimatum_sit()
    else:
        print misunderstand
        aliens_speak()

def ultimatum_sit():
    print "They say, 'It is the _____. The sacred song. It is inside you. You must return it.'"
    print "Suddenly you remember the mysterious cube. Could this be what they mean?"
    print "The aliens say, 'You have three days."
    print "'If you do not return the ____ in that time we will take it by force;"
    print "'your life with it if necessary.'"
    print "You feel a stirring of anxiety for the safety of your crew."
    print "Should you speak up or stay silent?"
    crew_safety = raw_input(prompt)
    if "speak" in crew_safety and responsible_var:
        print "You say, 'Wait, what about my crew? Will they be harmed?'"
        print "They answer, 'Because you have taken responsibility for the theft,"
        print "'we will not harm any member of your crew. You have our word.'"
        print "You breath a sigh of relief."
        global promise_var
        promise_var = True
        aliens_leave()
    elif "speak" in crew_safety and not responsible_var:
        print "You say, 'Wait, what about my crew? Will they be harmed?'"
        print "They answer, 'Do you take full responsibility for the theft?'"
        print "Do you answer yes or no?"
        resp_answr = raw_input(prompt)
        if resp_answr == "yes":
            print "You agree to take full responsibility."
            print "The aliens say, 'Then you have our word none of your crew will be harmed.'"
            print "You breath a sigh of relief."
            promise_var = True
            aliens_leave()
        else:
            print "You do not agree."
            print "The aliens say, 'Then we will make no promises concerning your crew.'"
            print "You hear angry whispers coming from some of your crew."
            aliens_leave()
    elif "silent" in crew_safety:
        print "You decide not to say anything and risk angering the aliens further."
        aliens_leave()
    else:
        print misunderstand
        ultimatum_sit()

def explore_planet():
    print "Pirates are after adventure as well as treasure!"
    print "You and a few crew members, including your first mate and best friend, go explore."
    print "You don't have to go too far before you find an interesting-looking cave."
    print "You go inside and find two tunnels branching off the main cave."
    print "Do you take the left tunnel or the right?"
    cavetunnel = raw_input(prompt)
    if cavetunnel == "left":
        snake_pit()
    elif cavetunnel == "right":
        monster_cave()
    else:
        print misunderstand
        explore_planet()

def snake_pit():
    print "After following the left tunnel for a while, you stumble across a snake pit."
    print "You didn't see it in time to stop so you fall in!"
    print "Do you panic and thrash about, calmly move forward, or go back to the other tunnel?"
    snakesss = raw_input(prompt)
    if "panic" in snakesss:
        print "The snakes react to your panic and also panic, biting you."
        dead("The snakes' venom delivers unto you a slow and agonizing death.")
    elif "forward" in snakesss:
        print "You stay calm, and the snakes are actually pretty chill."
        print "They actually don't even move that much."
        print "You slowly move to the other side of the pit and climb out,"
        print "then continue down the tunnel."
        bug_cave()
    elif "back" in snakesss:
        print "You carefully climb back out of the pit, careful not to disturb the snakes."
        monster_cave()

def monster_cave():
    print "After following the right tunnel for a while, you enter a large cavernous area."
    print "At the opposite end you see two more tunnels branching off."
    print "But standing in front of these tunnels is a horrifying monster!"
    print "It has many tentacles and eyes, and looks both slimy and scaly."
    print "You have only one weapon with you, a small laser gun."
    print "How will you get the monster to move?"
    monster_moved = False
    advantage = False
    disadvantage = False
    while True:
        move_monster = raw_input(prompt)
        if "taunt" in move_monster:
            print "The monster doesn't react at all. It probably doesn't understand you."
        elif "shoot" in move_monster and monster_moved:
            dead("The monster becomes angry and disembowels you.")
        elif "shoot" in move_monster and advantage:
            print "The monster was distracted and you managed to hit it!"
            print "It moves away from the tunnel entrances."
            monster_moved = True
        elif "shoot" in move_monster and disadvantage:
            dead("The monster becomes angry and disembowels you.")
        elif "shoot" in move_monster and not advantage:
            print "You shoot at the monster but it deflects the shots."
            disadvantage = True
        elif "yell" in move_monster or "scream" in move_monster:
            print "The monster is momentarily startled! This could be your chance to shoot!"
            advantage = True
        elif "poke" in move_monster or "prod" in move_monster:
            print "The monster quivers and shrinks back from this harrassment."
            print "It moves away from the tunnel entrances."
            monster_moved = True
        elif "play dead" in move_monster:
            dead("The monster is not fooled and crushes you with its powerful tentacles.")
        elif "tunnel" in move_monster and monster_moved:
            monstunnel_choice()
        else:
            print "What? What? What are you doing? Look at your life, look at your choices."

def monstunnel_choice():
    print "Do you take the left tunnel or the right?"
    tunn_choice = raw_input(prompt)
    if tunn_choice == "left":
        swamp_room()
    elif tunn_choice == "right":
        spike_room()
    else:
        print misunderstand
        monstunnel_choice()

def swamp_room():
    print "You stumble into another cave. This one is partially flooded."
    print "It's so swampy that after only a few steps you're afraid of getting stuck."
    print "You can't go back because the monster is still there."
    print "You take the chance of moving onward, but there's a good chance you'll be"
    print "sucked into the swamp and die."
    raw_input(prompt)
    swamp_stuck = randint(0,1)
    if swamp_stuck == 0:
        print "You are unlucky!"
        dead("The swamp sucks you under and you die.")
    else:
        print "You are lucky! You manage to get through the swamp to the other side."
        bug_cave()

def spike_room():
    print "You stumble into another cave. Immediately a boulder rolls down to seal the way"
    print "you just came in. You can see another boulder blocking a tunnel across the cave."
    print "Spikes start slowly descending from the ceiling!"
    raw_input(prompt)
    print "Just as you're thinking things can't get worse, water starts rising from the floor."
    print "How will you get out of this dire predicament?"
    switch_lever = False
    boulder_tired = False
    lasso_count = 0
    while not switch_lever:
        if lasso_count == 3:
            print "You run out of time!"
            dead("You die a slow agonizing death both drowning and being impaled by spikes.")
        action = raw_input(prompt)
        if "give up" in action:
            dead("You die a slow agonizing death both drowning and being impaled by spikes.")
        elif "boulder" in action and not boulder_tired:
            print "You try to move the boulder but it's too heavy."
            boulder_tired = True
        elif "boulder" in action and boulder_tired:
            dead("You tire yourself out trying to move a much too heavy boulder and drown.")
        elif "look" in action:
            print "You see no other exits, but what's that, high on the cave wall?"
            print "It appears to be a small lever!"
            print "You have a length of rope, maybe you can lasso it!"
        elif "lasso" in action:
            lasso_lever = randint(1,3)
            if lasso_lever == 1:
                print "You successfully lasso the lever!"
                print "When you pull, the spikes go back up and the water drains away."
                switch_lever = True
            else:
                print "You missed the lever!"
                lasso_count += 1
    print "The boulders roll away from the tunnels and you move onward."
    bridge_game()

def bug_cave():
    print "You're walking along when you hear a strange crunching noise."
    raw_input(prompt)
    print "You look down and the floor is covered in all kinds of creepy crawlies!"
    print "On a scale of 1 to 10, how creeped out are you by bugs?"
    gross_bugs = int(raw_input(prompt))
    if gross_bugs > 7:
        print "You are pretty grossed out. You feel panic rising inside you."
        print "Do you fight the panic or give in?"
        panic_bugs = raw_input(prompt)
        if "fight" in panic_bugs:
            print "You fight the panic down and keep going."
            bridge_game()
        elif "give" in panic_bugs:
            print "You surrender to your impulse to panic and run around screaming."
            dead("In your panic you run off a cliff and impale yourself on a stalagmite.")
        else:
            print misunderstand
            bug_cave()
    else:
        print "You aren't really scared of bugs so you just keep walking like normal."
        bridge_game()

def bridge_game():
    # create the bridge
    bridge = []
    bridge.append(["|", "_", "_", "_", "|"])
    for i in range(10):
        bridge.append(["|", "_", str(i), "_", "|"])
    bridge.append(["|", " ", " ", " ", "|"])

    def print_bridge():
        for row in bridge:
            print "".join(row)

    # assign the rotten slats
    rotten = []
    how_many = randint(1,3)
    for i in range(how_many):
        slat = randint(0,9)
        while slat in rotten:
            slat = randint(0,9)
        rotten.append(slat)

    # game instructions
    print "You come to a wide ravine with a narrow rope bridge crossing it."
    print "This bridge doesn't look very reliable. Some of the slats might be rotten."
    raw_input(prompt)
    print "You find 5 rocks lying on the ground."
    print "You can test a slat by throwing a rock on it to see if it gives way."
    print "Choose carefully though, because you only have enough rocks to test half."
    print "To test a slat, pick a number from 0 to 9."

    # test 5 slats
    for i in range(5):
        print_bridge()
        print "You are on stone %i. Which slat do you test?" % (i + 1)
        try:
            test_slat = int(raw_input(prompt))
        except ValueError:
            print "That's not even a number! Are you even taking this seriously?"
            test_slat = 10
        if test_slat > 9 or test_slat < 0:
            print "The instructions were very clear! Pick a number from 0 to 9!"
        elif test_slat in rotten:
            print "The slat gives way! You've found a rotten one!"
            rotten.remove(test_slat)
            bridge[test_slat + 1][2] = "X"
        else:
            print "The slat holds!"
            bridge[test_slat + 1][2] = "o"
    print_bridge()

    # if you found all the rotten slats you win
    if len(rotten) == 0:
        win_bridge()
    else:
        print "You didn't find all the rotten slats! Play again or move on?"
        bridge_again = raw_input(prompt)
        if "play" in bridge_again:
            bridge_game()
        else:
            lose_bridge()

def win_bridge():
    print "You found all the rotten slats and cross safely!"
    cave_treasure()

def lose_bridge():
    print "Your crewmembers cross the bridge ahead of you,"
    print "but when you try to cross the bridge, a slat breaks and you fall!"
    raw_input(prompt)
    print "You are dangling precariously above the ravine by a fraying rope."
    print "Your best friend starts to run out onto the bridge to save you,"
    print "but you can see that another spot on the bridge is about to break."
    print "Do you warn your friend to stay back?"
    warn_friend = raw_input(prompt)
    if warn_friend == "yes":
        save_friend()
    elif warn_friend == "no":
        save_self()
    else:
        print misunderstand
        lose_bridge()

def save_friend():
    print "You shout out a warning to your friend. They heed your warning and stay back."
    print "Suddenly the bridge snaps completely!"
    raw_input(prompt)
    survive = randint(0,1)
    if survive == 0:
        print "The rope tethering you to safety is wrenched from your grasp."
        print "The last thought that crosses your mind is that at least you managed"
        print "to spare your best friend."
        dead("You plummet to your death, smashed to pieces on the rocks below.")
    else:
        print "You miraculously manage to hang on."
        print "You crash painfully into the cliff edge, but you survive."
        print "You climb up to where your crewmembers are waiting."
        cave_treasure()

def save_self():
    print "You stay silent as your friend rushes out to save you."
    print "They manage to pull you up, and for a second you think all will be well."
    raw_input(prompt)
    print "But the illusion is shattered."
    print "Just before you reach safety, the bridge snaps completely."
    print "You manage to hang on to the cliff edge, but your friend plummets into the ravine."
    print "You climb up to safety as their dying scream echoes in your ears."
    raw_input(prompt)
    print "Your crew never suspects that you could have warned your friend and chose not to,"
    print "but you yourself know, and you suspect the truth will haunt you forever."
    global bestfriend_var
    bestfriend_var = False
    cave_treasure()

def cave_treasure():
    if not bestfriend_var:
        print "In the final cave you find fabulous treasure."
        print "You and your crewmembers take as much as you can carry."
        global treasure_var
        treasure_var = True
        leave_cave()
    else:
        print "In the cave ahead you see a glimmer of gold. There's treasure!"
        print "As you approach, rocks start to fall from the ceiling. The tunnel is caving in!"
        raw_input(prompt)
        cavein = randint(0,2)
        if cavein == 0:
            print "You and your crew manage to escape the falling rocks,"
            print "but the passage to the treasure cave is blocked."
            leave_cave()
        else:
            print "You and your crew escape the falling rocks and run into the treasure cave."
            print "You find fabulous treasure; each person takes as much as they can carry."
            treasure_var = True
            leave_cave()

def leave_cave():
    print "Luckily you find a secret exit so you don't have to go back the way you came."
    print "You and your crew members head back to your ship."
    privateers()

def privateers():
    print "As you're flying away from the planet, you spy another ship."
    print "This ship bears the mark of privateers!"
    print "Pirates and privateers are mortal enemies! Fight or flight?"
    battle = raw_input(prompt)
    if battle == "fight":
        priv_battle()
    elif battle == "flight":
        flee_priv()
    else:
        print misunderstand
        privateers()

def priv_battle():
    print "You prepare to fight the privateers."
    print "You have 10 chances to hit their ship. You must hit it 3 times to win."
    print "To take a shot, choose a number from 1 to 15. (Choose a number only once.)"
    hits = []
    for i in range(3):
        hit = randint(1,15)
        while hit in hits:
            hit = randint(1,15)
        hits.append(hit)
    for i in range(10):
        print "Shot", i + 1
        try:
            shot = int(raw_input(prompt))
        except ValueError:
            print "That's not even a number. Are you taking this seriously?"
            shot = 0
        if shot > 15 or shot < 1:
            print "The instructions were very clear! Pick a number from 1 to 15!"
        elif shot in hits:
            print "Direct hit!"
            hits.remove(shot)
        else:
            print "You missed the ship!"

        if len(hits) == 0:
            print "That's three hits! You win!"
            win_battle()

    print "You failed to hit the ship enough times. You lose."
    print "Play again? Or move on?"
    play_again = raw_input(prompt)
    if "play" in play_again:
        priv_battle()
    else:
        lose_battle()

def flee_priv():
    print "You don't feel like fighting today, so you try to outrun them."
    print "Your ship is fast, but there's always a chance theirs is faster."
    raw_input(prompt)
    escape = randint(0,1)
    if escape == 0:
        print "Unfortunately your gamble fails, and they are faster than you."
        print "You have no choice but to turn and fight."
        priv_battle()
    else:
        print "Today is your lucky day! They can't keep up with your superior ship."
        market()

def win_battle():
    print "As the winner of the battle, you get to plunder the loser's ship."
    print "They don't have much cargo, but ship parts are always useful."
    print "You strip the privateer ship for parts and leave them marooned."
    global shipparts_var
    shipparts_var = True
    raw_input(prompt)
    market()

def lose_battle():
    print "You have lost the battle. Many of your crew are injured, and a few are dead."
    print "A stray shot from the privateers comes out of nowhere!"
    print "Your ship is rocked by the blast, and a heavy piece of machinery topples."
    if not bestfriend_var:
        print "You turn, but you don't see it in time and it crushes you."
        print "If only your best friend were still alive, surely they would have warned you!"
        dead("You are brutally crushed to death.")
    else:
        print "Your best friend shouts a warning and you jump out of the way just in time!"
        print "You manage to escape the privateers by cleverly hiding behind an asteroid."
        raw_input(prompt)
        market()

def market():
    print "You decide to go to market to sell your treasure."
    if not treasure_var and not shipparts_var:
        print "Unfortunately you have no treasure!"
        broke_pirate()
    elif treasure_var and shipparts_var:
        print "You have a seriously good haul! A+ pirating!"
        rich_pirate()
    else:
        print "You have a decent haul, and your crew are eager to sell it off."
        rich_pirate()

def rich_pirate():
    print "You go to the nearest planet with a roaring black market trade."
    raw_input(prompt)
    if suspicion_var:
        print "As you're unloading the goods, you get hit over the head from behind!"
        print "When you come to, you realize your crew has absconded with all the treasure,"
        print "leaving you stranded and alone!"
        print "Probably because they didn't trust you after you abandoned your best friend."
        dead("You starve to death, alone and friendless.")
    if treasure_var and shipparts_var:
        print "You sell off most of your treasure and the ship parts you took,"
        print "keeping a few things for yourselves."
    elif treasure_var:
        print "You sell off most of your treasure, keeping a few things for yourselves."
    elif shipparts_var:
        print "You sell off most of the ship parts, keeping a few things for yourselves."
    print "You split the money evenly between all members of your crew"
    print "(you're a pirate, but not an unreasonable one)."
    raw_input(prompt)
    print "As you're celebrating in the local tavern, you overhear someone talking about"
    print "the most fantastic treasure known to man, beast, or alien."
    print "Your curiosity is piqued."
    print "Do you listen further or remain content with the riches you already have?"
    more_treasure = raw_input(prompt)
    if "listen" in more_treasure:
        zombie_legend()
    elif "content" in more_treasure:
        print "You ignore the conversation and keep celebrating your riches with your crew."
        win()
    else:
        print misunderstand
        rich_pirate()

def broke_pirate():
    print "You go to the nearest planet with a black market anyway."
    print "Maybe you'll be able to barter for something."
    print "As you're walking through market stalls, you overhear someone talking about"
    print "the most fantastic treasure known to human, beast, or alien."
    raw_input(prompt)
    print "Your curiosity is piqued."
    zombie_legend()

def zombie_legend():
    print "You look around and see the people you overheard: two ruffians."
    print "They're now talking about this fantastic treasure and how it's guarded"
    print "by a supernatural curse that raises the dead."
    raw_input(prompt)
    print "Space zombies! You scoff; you have faced much worse before."
    print "You keep listening discreetly and find out where this zombie-guarded treasure is."
    print "Once you have all you need, you hurry back to your crew and tell them."
    print "They agree to go after this fantastic treasure, and you all head off on your ship."
    raw_input(prompt)
    zombie_treasure()

def zombie_treasure():
    print "You get to the zombie treasure planet and get out to explore."
    print "There's a giant cave entrance that practically screams 'ZOMBIE GUARDED TREASURE'."
    print "You go inside and find two tunnels branching off to either side."
    print "Do you take the left or the right?"
    tunnel = raw_input(prompt)
    if tunnel == "left":
        fight_zombies()
    elif tunnel == "right":
        witch_cave()
    else:
        print misunderstand
        zombie_treasure()

def fight_zombies():
    print "At the end of a long tunnel you enter a large cavernous space."
    print "At first glance it appears empty, but then the ground begins to move beneath you!"
    print "Undead bodies start popping up out of the ground and lumbering towards you!"
    raw_input(prompt)
    if hook_var:
        print "You start slashing at them with your hook-arm."
        print "Your hook seems particularly effective at destroying the monsters!"
        zombie_game()
    else:
        print "You try to fight them off but they are very resilient."
        print "Desperately you fight to keep from being overwhelmed by the monsters."
        zombie_game()

def witch_cave():
    print "At the end of a long tunnel you enter a dimly-lit cavern."
    print "You see a witch cackling as they stir a cauldron."
    print "As you watch, a dead body nearby starts to move. It's being reanimated!"
    print "Do you stay to watch or book it out of there?"
    witch_spell = raw_input(prompt)
    if "stay" in witch_spell or "watch" in witch_spell:
        print "The witch sees you and casts a spell on you."
        dead("The witch's spell turns you into one of her undead minions.")
    elif "book" in witch_spell:
        fight_zombies()
    else:
        print misunderstand
        witch_cave()

def zombie_game():
    if hook_var:   # this makes the game easier if you have a hook
        startnum = 0
        endnum = 1
        instr = "either 0 or 1"
    else:
        startnum = 1
        endnum = 5
        instr = "a number from 1 to 5"
    print "There are 10 zombies coming at you! Luckily they come at you one at a time,"
    print "so you only have to fight them individually."
    print "You must kill at least 5 zombies."
    print "To fight each zombie choose %s." % instr
    deadzom_count = 0
    for i in range(10):
        print "Zombie %i approaches!" % (i + 1)
        deadzombie = randint(startnum,endnum)
        try:
            killzombie = int(raw_input(prompt))
        except ValueError:
            print "That's not even a number! Are you even taking this seriously?"
            killzombie = -1
        if killzombie > endnum or killzombie < startnum:
            print "The instructions were very clear! Pick %s!" % instr
        elif killzombie == deadzombie:
            print "You killed zombie %i! Nice one!" % (i + 1)
            deadzom_count += 1
        else:
            print "You failed to kill zombie %i!" % (i + 1)
    if deadzom_count > 6:
        print "You killed 7 or more zombies! Well done!"
        global zombonus_var
        zombonus_var = True
        zombie_win()
    elif deadzom_count >= 5:
        print "You killed at least 5 zombies! You win!"
        zombie_win()
    else:
        print "You failed to kill enough zombies. They're overwhelming you!"
        print "Play again or move on?"
        more_zombies = raw_input(prompt)
        if "play" in more_zombies:
            zombie_game()
        else:
            dead("The zombies mob you and tear you apart.")

def zombie_win():
    print "You are able to escape the remaining zombies and continue down the tunnel."
    print "You reach a cavern filled with gold!"
    print "How many bars of gold do you take?"
    try:
        carry_gold = int(raw_input(prompt))
    except ValueError:
        print "Oops! Type only numbers please."
        carry_gold = int(raw_input(prompt))
    while True:
        if carry_gold > 50:
            print "That's too much! You can't carry it all."
            carry_gold = int(raw_input(prompt))
        elif carry_gold < 1:
            print "Stop fooling around! How many bars of gold do you take?"
            carry_gold = int(raw_input(prompt))
        elif not zombonus_var and carry_gold > 25:
            print "When you try to carry your gold back through the tunnel,"
            print "the remaining zombies attack you!"
            print "You try to fight them off but you're weighed down by the gold!"
            dead("The zombies mob you and tear you apart.")
        elif not zombonus_var and carry_gold <= 25:
            print "When you carry your gold back through the tunnel,"
            print "the remaining zombies try to attack you but you manage to fight them off."
            print "You leave the planet and enjoy your modest wealth."
            win()
        elif zombonus_var:
            print "When you carry your gold back through the tunnel,"
            print "the remaining zombies try to attack you but you manage to fight them off."
            print "You leave the planet and become known far and wide as one of the richest"
            print "and most fortunate pirates to ever live."
            win()

def win():
    if not bestfriend_var:
        print "You live out the rest of your days in wealth and comfort."
        print "Except..."
        print "You are haunted by your best friend's death."
        print "In the end, your wealth is meaningless and food turns to ashes in your mouth."
        print "You think about how you should have saved them until your dying breath."
        dead("You die friendless and alone, cursing your very existence.")
    else:
        print "You live a long and happy life as a pirate, having many more adventures"
        print "and winning more treasure."
        print "Congratulations! You win!"
        exit(0)

def aliens_leave():
    print "The aliens vanish as suddenly as they appeared."
    print "You think the 'sacred song' must have something to do with the"
    print "mysterious cube and the song you heard when you touched it,"
    print "but you have no idea how to give the song back."
    print "Do you try to make a run for it or investigate the mysterious cube?"
    investigate = raw_input(prompt)
    if "run" in investigate:
        run_away()
    elif "investigate" in investigate:
        brainexp_sit()
    else:
        print misunderstand
        aliens_leave()

def run_away():
    print "You give the order to make for the outer reaches of the galaxy,"
    print "as fast as your ship will go."
    if promise_var:
        print "After three days of fleeing, you're hiding out on a remote planet."
        print "Suddenly the aliens appear before you!"
        print "How could you have been so foolish as to think you could outrun them?"
        print "As the aliens bear down on you,"
        print "at least you have the comfort of knowing your crew will be safe."
        dead("The aliens suck your brain out and you die.")
    else:
        print "After a day or so of fleeing, your crew can't take the stress."
        print "Your first mate (and best friend) comes to you,"
        print "and demands you turn yourself in to the aliens, or they'll mutiny."
        print "Should you turn yourself in or argue with your best friend?"
        coward = raw_input(prompt)
        if "turn" in coward:
            giveup_aliens()
        elif "argue" in coward:
            mutiny()
        else:
            print misunderstand
            run_away()

def mutiny():
    dead("Your crew mutinies and you're murdered by your best friend.")

def brainexp_sit():
    print "You tell your crew about the mysterious cube,"
    print "and say you want to investigate it to try and figure out how to give it back."
    print "Your first mate (and best friend) tells you they know about a brain expert,"
    print "who lives on a planet not too far from here."
    print "You go talk to this brain expert, who gives you two choices:"
    print "Try to recreate the song you heard from memory,"
    print "or try a cutting-edge brain scan that may be able to isolate the song in your brain."
    get_song = raw_input(prompt)
    if "recreate" in get_song or "memory" in get_song:
        memory_song()
    elif "scan" in get_song:
        brain_scan()
    else:
        print misunderstand
        brainexp_sit()

def brain_scan():
    print "You agree to the brain scan."
    print "After several hours, the brain expert tells you they have successfully"
    print "isolated where the song is within your brain!"
    print "Now however comes the truly dangerous part: Do you try to extract the song?"
    print "(The brain expert tells you there is only a 1 in 5 chance of success,"
    print "and there is a 1 in 3 chance the procedure kills you.)"
    danger_extract = raw_input(prompt)
    if danger_extract == "yes":
        song_extract()
    elif danger_extract == "no":
        print "You decide not to risk the procedure."
        print "Will you run away or turn yourself in to the aliens?"
        no_scans = raw_input(prompt)
        if "run" in no_scans:
            run_away()
        elif "turn" in no_scans:
            giveup_aliens()
        else:
            print misunderstand
            brain_scan()
    else:
        print misunderstand
        brain_scan()

def memory_song():
    print "You do your best to recreate the song from memory,"
    print "working with several musical geniuses."
    print "Unfortunately it proves to be an impossible task."
    print "Should you try the brain scan, run away, or turn yourself in to the aliens?"
    memory_fail = raw_input(prompt)
    if "scan" in memory_fail:
        brain_scan()
    elif "run" in memory_fail:
        run_away()
    elif "turn" in memory_fail:
        giveup_aliens()
    else:
        print misunderstand
        memory_song()

def song_extract():
    print "You decide to risk the procedure."
    print "Pick a number from 1 to 5:"
    guess_success = int(raw_input(prompt))
    while guess_success > 5 or guess_success < 1:
        print "Stop fooling around! Pick a number from 1 to 5:"
        guess_success = int(raw_input(prompt))
    print "Now pick a number from 1 to 3:"
    guess_survive = int(raw_input(prompt))
    while guess_survive > 3 or guess_survive < 1:
        print "Stop fooling around! Pick a number from 1 to 3:"
        guess_survive = int(raw_input(prompt))
    true_success = randint(1,5)
    true_survive = randint(1,3)
    if guess_survive == true_survive:
        dead("The extraction process turns your brain to mush and you die.")
    elif guess_success == true_success:
        print "Congratulations! The procedure was a success and you survived!"
        aliens_success()
    elif guess_success != true_success:
        print "You survive the procedure, but unfortunately it is unsuccessful."
        extractfail_choice()

def extractfail_choice():
    print "Will you return and face the aliens anyway, or run away?"
    extract_fail = raw_input(prompt)
    if "return" in extract_fail:
        giveup_aliens()
    elif "run" in extract_fail:
        run_away()
    else:
        print misunderstand
        extractfail_choice()

def aliens_success():
    print "You return to the aliens' planet with the extracted song."
    print "The aliens appear and you return the song to them."
    print "They are very grateful and allow you to keep the rest of the treasure."
    privateers()

def giveup_aliens():
    print "You go back to the aliens' planet to surrender yourself."
    print "As you approach the place on the planet's surface where you found the cube,"
    print "you are filled with trepidation."
    print "You desperately want your best friend to go with you."
    print "Will you ask them, or go alone?"
    friend_go = raw_input(prompt)
    if "ask" in friend_go:
        bestfriend_goes()
    elif "alone" in friend_go:
        go_alone()
    else:
        print misunderstand
        giveup_aliens()

def bestfriend_goes():
    print "You tell your best friend how scared you are and ask them to go with you."
    print "They agree immediately and give you a hug for support."
    print "The two of you go down to the planet's surface together,"
    print "leaving the rest of your crew on board."
    raw_input(prompt)
    print "The aliens appear, but when you try to walk towards them your friend"
    print "suddenly charges at the aliens and tries to fight them!"
    print "You watch in horror as the aliens easily throw your friend aside."
    print "They lay where they fall, quite still."
    print "You cry out in grief to the aliens, 'How could you?!'"
    if promise_var:
        print "'You promised you wouldn't harm any of my crew!'"
        print "Your friend still hasn't moved, and you fear they are dead."
        raw_input(prompt)
        print "The aliens say, 'We have broken our word. You returned as you promised,"
        print "and we have harmed a member of your crew. This must be remedied'"
        raw_input(prompt)
        print "They continue, 'However, we cannot allow you to keep the ____."
        print "We will give you 50 more years to return the ___ in exchange for"
        print "harming your crew member. In addition, we have the ability to heal them,"
        print "but you must give us something in return. Such as... that appendage there.'"
        print "The alien gestures to your left arm."
        print "Will you trade your left arm for the life of your best friend?"
        trade_arm = raw_input(prompt)
        if trade_arm == "yes":
            lose_arm()
        elif trade_arm == "no":
            bestfriend_dies()
        else:
            print "you typed something other than yes or no you nitwit"
    else:
        print "The aliens say, 'We care not for the friends of a lying thief.'"
        print "You rush over to where your friend lies, still not moving."
        print "Their breathing is very shallow and you can't detect a pulse."
        print "As you watch, your best friend dies."
        print "You are consumed with terrible grief as the aliens bear down on you."
        dead("The aliens suck out your brain and you die.")

def go_alone():
    print "You decide not to speak up, and go to meet the aliens alone."
    print "The aliens appear, and you stand helplessly terrified as they approach."
    dead("The aliens suck out your brain and you die.")

def lose_arm():
    print "You agree immediately, and one of the aliens waves over your left arm,"
    print "which vanishes up to the elbow."
    print "You turn back to your friend, who is sitting up. They look as good as new!"
    print "You thank the aliens for healing your friend, and together go back to your ship."
    raw_input(prompt)
    print "You decide to replace your arm with a hook (you are a pirate, after all)"
    print "and spend the rest of your 50 years seeking more adventure."
    print "In the meantime, you still have all this treasure!"
    global hook_var
    hook_var = True
    privateers()

def bestfriend_dies():
    print "You refuse. You can't imagine life without your left arm!"
    print "The aliens remain silent, and your best friend slowly dies before your eyes."
    print "The aliens warn you that you must return to surrender yourself in 50 years."
    print "You return to your ship without your best friend, and your crew notices."
    print "Do you tell them the truth or lie?"
    truth = raw_input(prompt)
    if "truth" in truth:
        mutiny_crew()
    else:
        lie_crew()

def mutiny_crew():
    print "You tell your crew what happened, and when they find out that you sacrificed"
    print "your best friend to keep your arm, any loyalty they had to you is gone."
    dead("Your crew mutinies and murders you in your sleep.")

def lie_crew():
    print "You're not stupid enough to tell them the truth!"
    print "You lie and say the aliens killed your best friend for no reason, but"
    print "you managed to barely escape with your life."
    global suspicion_var, bestfriend_var
    suspicion_var = True
    bestfriend_var = False
    privateers()

def dead(why):
    print why, "Game over!"
    exit(0)

start()
