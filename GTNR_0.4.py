'''
Gabe the Needy Robot v0.4
*This code is optimized for Python Ver 3.5.2

Welcome to Gabe the Needy Robot! This code was created by Gabriel
CONTACT: https://github.com/ItsGJK/GTNR (please all requests etc. through github)


The following is the code for this game. If you don't want to install Python 3 to your computer, you can
go to the website https://repl.it/languages/python3 and copy & paste this code
into the text field then press "run".

This code is open for free use. Edit freely as long as you credit:
"Code credits to Gabriel (webgjk.weebly.com)" as a comment or code content.
Code below, do not edit unless you know what you're doing!

CHANGELOG (0.4): (I've made sickness less of an importance for Gabe. He'll get sick less frequently, allowing you to focus on some other things ;) )
 - Gabe will get sick less frequently
 - Gabe can get +2 hunger in one turn
 - Changed small things with bored check, notice bored being a bit bigger role

In the future, I plan on recoding Gabe the Needy Robot in C#! Contact me at on my website if you'd like to help.

'''


# Module importing (loading screen for extremely slow computers to let them know Python isn't dead. It's quite useless, but still...
print("Importing modules, please wait (0/2)")
import time
print("Importing modules, please wait (1/2)")
import random
print("Importing modules, please wait (2/2)")
print("Module import finished.\n")
# Version, do not change
ver = "v0.4"
# Start
print("Gabe the Needy Robot %s\n" % (ver))
print("Keep him alive! Gabe will die if any of the following happens to him:\n - Happiness reaches 0\n - Sickness reaches 10\n - Hunger reaches 10\n - Boredom reaches 10\n - Tiredness reaches 10\n")
# Game Data Resetting
while True: #All functions reset when Gabe dies and game restarts
    day = 0
    happy = 10
    bored = 0
    tired = 0
    sick = 0
    hungry = 0
    ds = 0
    didAction = 0
# Game start
    a = input("Press enter to play the game!")
    if a=="generic easter egg":
        print("A GENERIC EASTER EGG HAS APPEARED! A GENERIC EASTER EGG KILL YOU!")
        time.sleep(1)

    while True: # Day repetition 
# The following is what happens every day:
        day = day+1 # SCORE COUNTER
        time.sleep(0.6)
# 1st Death Check
        if happy<1:
            print("\n\nGabe died! He's too depressed.")
            break
        elif bored>9:
            print("\n\nGabe died! He's too bored.")
            break
        elif tired>9:
            print("\n\nGabe died! He's too tired.")
            break
        elif sick>9:
            print("\n\nGabe died! He's too sick.")
            break
        elif hungry>9:
            print("\n\nGabe died! He's too hungry.")
            break

        print("\n\n\n**WHAT HAPPENED TODAY:**\n")
        chance = random.randint(0,15)
        if sick > 0:
            chance5=random.randint(0,4)
            if chance5==1:
                sick = sick+1
                ds=1
                print("Gabe is becoming sicker. Sickness is now %s" % (sick))
        if chance==10 or chance==11:
            sick = sick + 1
            ds=1
            if sick>1:
              print("Gabe has contracted another disease. Sickness is now %s" % (sick))
            else:
              print("Gabe has now contracted a disease. Sickness is now %s" % (sick))
        elif chance==12 or chance==13:
            sick = sick + 1
            ds=1
            if sick>1:
              print("Gabe has contracted another disease. Sickness is now %s" % (sick))
            else:
              print("Gabe has now contracted a disease. Sickness is now %s" % (sick))
        elif chance==1:
            sick = sick + 2
            ds=1
            print("Gabe has contracted a major disease. Sickness is now %s" % (sick))
        chance1 = random.randint(1,2)
        if chance1 == 1:
            hungry = hungry + 1
            ds=1
            print("Gabe has now became hungry. Hungriness is now %s" % (hungry))
        else:
          extraHungerChance = random.randint(1,9)
          if extraHungerChance==1:
            ds=1
            hungry = hungry + 2
            print("Suddenly, Gabe becomes very hungry. Hungriness is now %s" % (hungry))
        if sick > 3:
            chance2 = random.randint(0,1)
            if chance2==1:
                happy = happy-1
                ds=1
                print("Gabe is now becoming depressed since he is sick. Happiness is now %s" % (happy))
        if sick>7:
          print("Is there any hope for Gabe? Will he live? Is Gabe going to die to sickness?")
        if bored > 5:
            chance3=random.randint(0,2)
            if chance3==1:
                happy = happy-1
                ds=1
                print("Gabe is very bored. He is getting sad. Happiness is now %s" % (happy))
        if tired > 6:
            chance4=random.randint(0,1)
            if chance4==1:
                happy=happy-1
                ds=1
                print("Gabe is becoming sad because he is tired. Happiness is now %s" % (happy))
        if tired > 5:
#a cookie appeared
            chance6=random.randint(1,9)
            if chance6==1:
                tired=tired-2
                ds=1
                print("Gabe somehow catchs a powernap and regains his bearings. Tired is now %s" % (tired))
        if sick > 5:
            chance6=random.randint(1,10)
            if chance6==1:
                bored=bored+1
                ds=1
                print("Since Gabe is stuck in bed being extremely sick, he's getting bored. Bored is now %s" % (bored))
        if tired < -1:
            bored=bored+2
            ds=1
            print("Gabe has been sleeping too much. Boredness is now %s" % (bored))
        if happy>11:
            ds=1
            sick=sick+2
            happy=6
            print("Gabe started jumping around the house filled with excitement and joy. He's too happy. He kissed his cat and got sick. Sickness is now %s and happiness is now %s" % (sick, happy))
        if ds==0:
            print("Nothing happened! Lucky you!")
        ds=0 #DS MEANS didSomething I'M JUST VERY BAD AT MAKING VARIABLE NAMES (and too lazy to change them)
# 2nd Death Check
        if happy<1:
            print("\n\nGabe died! He's too depressed.")
            break
        elif bored>9:
            print("\n\nGabe died! He's too bored.")
            break
        elif tired>9:
            print("\n\nGabe died! He's too tired.")
            break
        elif sick>9:
            print("\n\nGabe died! He's too sick.")
            break
        elif hungry>9:
            print("\n\nGabe died! He's too hungry.")
            break
# Statistics Msg
        print("\n**CURRENT STATS:**\n\nScore: %s\nHappy: %s/10\nBored: %s/10\n Tired: %s/10\nSick: %s/10\nHungry: %s/10" % (day, happy, bored, tired, sick, hungry))
# Actions - what to do daily
        print("\n**WHAT TO DO:**\n")
        print("1 = Get Medicine (sickness - 1, tired + 1)\n2 = Play (happiness + 1, tired + 1, bored - 1)\n3 = Sleep (tired - 1 OR tired - 2, bored + 1)\n4 = Eat (hungriness - 1, tired + 1)")
        opt = str(input(" > "))
        if opt=="1":
            if tired > 5:
                chance8 = random.randint(0,5)
                if chance8==1:
                    didAction=0
                    print("Gabe is too tired. Your option was cancelled.")
                else:
                    sick = sick-1
                    tired=tired+1
                    didAction = didAction+1
                    print("You chose to make Gabe get medicine.")
                    if sick < 0:
                        print("\n\nGabe died of overdosing. Such a horible way to die.")
                        break
            else:
                sick = sick-1
                tired=tired+1
                didAction = didAction+1
                print("You chose to make Gabe get medicine.")
                if sick < 0:
                    print("\n\nGabe died of overdosing. Such a horible way to die.")
                    break
        elif opt=="2":
            if tired > 5:
                chance8 = random.randint(0,5)
                if chance8==1:
                    didAction=0
                    print("Gabe is too tired. Your option was cancelled.")
                else:
                    bored=bored-1
                    tired=tired+2
                    happy=happy+1
                    didAction = didAction+1
                    print("You chose to make Gabe play.")
            else:
                bored=bored-1
                tired=tired+2
                happy=happy+1
                didAction = didAction+1
                print("You chose to make Gabe play.")
        elif opt=="3":
            chance10 = random.randint(1,3)
            if chance10==1 or chance10==2:
              tired=tired-1
              bored=bored+1
              didAction=0
              print("You chose to make Gabe sleep. His sleep quality was decent.")
            else:
              tired=tired-2
              bored=bored+1
              didAction=0
              print("You chose to make Gabe sleep. His sleeping quality was excellent.")
        elif opt=="4":
            if tired > 5:
                chance9 = random.randint(0,5)
                if chance9==1:
                    didAction=0
                    print("Gabe is too tired. Your option was cancelled.")
                else:
                    hungry=hungry-1
                    tired=tired+1
                    didAction = didAction+1
                    print("You chose to make Gabe eat.")
            else:
                hungry=hungry-1
                tired=tired+1
                didAction = didAction+1
                print("You chose to make Gabe eat.")
        elif opt=="iamretarded":
            name = input("What is your name?")
            print("Gabe died because %s was too retarded for him." % (name))
            break
        elif opt=="friedchicken":
            print("I like fried chicken, too! (hunger + 10)")
            hungry=10
        elif opt=="-hack 9001": #???
            print("It's over 9,000!")
            hungry=9001
            tired=9001
            sick=9001
            bored=9001
            happy=-9001
            time.sleep(1)
            print("Want to see what I just did? ;)")
            time.sleep(4)
            print("\n**CURRENT STATS:**\n\nScore: %s\nHappy: %s/10\nBored: %s/10\n Tired: %s/10\nSick: %s/10\nHungry: %s/10" % (day, happy, bored, tired, sick, hungry))
            time.sleep(5)
            print("Once you press enter Gabe will die. rip.")
            time.sleep(0.1)
            print("Don't do it...")
            a=input("")
            print("Gabe died due to /ERRORS/ILLUMINATI/333_UNKNOWN_ERROR/BLAME_THE_ALIENS") #  #blamethealiens 
            time.sleep(5)
            print("INVALID EXCEPTION: UNKNOWN ERROR")
            while True:
                print(random.randint(111111111111,99999999999999),random.randint(111111111111,99999999999999),random.randint(111111111111,99999999999999),random.randint(111111111111,99999999999999))
            break
        else:
            print("Invalid input, assuming Gabe did nothing. (bored + 1) (error 1)\nTIP: Type in the number (option) to choose then press [ENTER]")
            bored = bored+1
            didAction = 0

# Game over screen, "break" skips to this
    print("\nG A M E  O V E R! Your score was: %s" % (day))
    time.sleep(1)
    # now goes back to top /\
