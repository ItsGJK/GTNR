'''
Gabe the Needy Robot v0.321a
*This code is optimized for Python Ver 3.5.2

Welcome to Gabe the Needy Robot! This code was created by Gabriel
CONTACT: https://github.com/ItsGJK/GTNR (please all requests etc. through github)

For anyone using GTNR from Google Drive, I will soon stop uploading to Google Drive and use GitHub instead. (link: https://github.com/ItsGJK/GTNR)

The following is the code for this game. If you don't want to install Python 3 to your computer, you can
go to the website https://repl.it/languages/python3 and copy & paste this code
into the text field then press "run".

This code is open for free use. Edit freely as long as you credit:
"Code credits to Gabriel (webgjk.weebly.com)" as a comment or code content.
Code below, do not edit unless you know what you're doing!

CHANGELOGS (0.2a --> 0.3a): (THIS IS A BIG UPDATE!)
 - Added easter eggs (what easter eggs? you didn't hear anything about an easter egg, did you?)
 - Made game automatically restart instead of user having to close/open program
 - Fixed possible times when game would not kill Gabe when he was supposed to die (that sounds dramatic)
 - Switched order of stats/what what happened today notifications to make it easier on the eyes (+ stats will reflect current statistics and not last round stats)
 - Proper module loading (for slow computers)
 - You can no longer get "sicker" when contracting a disease in the same day (prioritization glitch)
 - An action can now be cancelled if Gabe is too tired (tired > 5 has a 1/6 action cancel chance)
 - Death detection detects death more often to help prevent daily stats for round before death (however there may be times when some messages print before dying in the same round)
 - Being too hungry will now kill you
 - Added in version 0.31a: Sleeping can give you -1 or -2 tiredness
 - Added in version 0.31a: Fixed print glitch: will now tell you when you choose to make Gabe eat
 - Added in version 0.32a: Added wait time for game to restart
 - Added in version 0.32a: The easter rabbit took one of the easter eggs and edited it a 'lil bit. Don't worry, no candy inside was harmed.
 - Added in version 0.32a: More commenting on code (and edited comments) to make code easier to understand for beginners & people in general
 - Added in version 0.32a: Boredom can now go down automatically by doing things constantly (waiting in the doctor's office for 2 hours for medicine is fun!)
 - Added in version 0.32a: Gabe will get sick (it's a long story) if he gets too happy. (If Gabe gets too happy, lock him up.)
 - Added in version 0.321a: Uploaded to GitHub! Polished everything, is ready for a public release. Next version will be beta.
 - Added in version 0.321a: No more secrets. The world shall know what ds means. (very useless, please disregard and throw in a fire)

Alpha version for this game is almost complete. Contact me if you'd like to help with graphics (in python3, please. I don't want to switch to a different language. (no html, js, etc.)
'''


# Module importing (loading screen for extremely slow computers to let them know Python isn't dead. It's quite useless, but still...
print("Importing modules, please wait (0/2)")
import time
print("Importing modules, please wait (1/2)")
import random
print("Importing modules, please wait (2/2)")
print("Module import finished.\n")
# Version, do not change
ver = "v0.32a"
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
        chance = random.randint(1,13)
        if sick > 0:
            chance5=random.randint(0,3)
            if chance5==1:
                sick = sick+1
                ds=1
                print("Gabe is becoming sicker. Sickness is now %s" % (sick))
        if chance==10 or chance==11:
            sick = sick + 1
            ds=1
            print("Gabe has now contracted a disease. Sickness is now %s" % (sick))
        elif chance==12 or chance==13:
            sick = sick + 1
            ds=1
            print("Gabe has now contracted a disease. Sickness is now %s" % (sick))
        elif chance==1 or chance==2:
            sick = sick + 2
            ds=1
            print("Gabe has contracted a major disease. Sickness is now %s" % (sick))
        chance1 = random.randint(1,2)
        if chance1 == 1:
            hungry = hungry + 1
            ds=1
            print("Gabe has now became hungry. Hungriness is now %s" % (hungry))
        if sick > 3:
            chance2 = random.randint(0,1)
            if chance2==1:
                happy = happy-1
                ds=1
                print("Gabe is now becoming depressed since he is sick. Happiness is now %s" % (happy))
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
            chance6=random.randint(1,8)
            if chance6==1:
                tired=tired-2
                ds=1
                print("Gabe somehow catchs a powernap and regains his bearings. Tired is now %s" % (tired))
        if sick > 5:
            chance6=random.randint(1,10)
            if chance6==1:
                bored=bored+1
                ds=1
                print("Since you're stuck in bed being extremely sick, you're getting bored. Bored is now %s" % (bored))
        if tired < -1:
            bored=bored+2
            ds=1
            print("Gabe has been sleeping too much. Boredness is now %s" % (bored))
        if didAction>4 and bored>2:
            ds=1
            bored=bored-1
            print("Gabe finds interest in the things you've been making him do. Boredness is now %s" % (bored))
        if happy>10:
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
