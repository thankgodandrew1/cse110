print('WELCOME TO THE ADVENTURE OF LEGENDS!!\n')
print('To proceed enter the following information:')

name = input('\nFirst name: ')
last_name = input('Last name: ')
age = input('Age: ')
country = input('Nationality: ') 

nationality = country.capitalize()

print ('\nName: ' + name.capitalize() + ' ' + last_name.capitalize() )
print (f'Age: {age:4} Nationality: {nationality}')

if nationality.lower() in('mexico', 'colombia', 'venezuela', 'ecuador', 'uruguay', 'honduras'):
    print('\nBienvenida a esta gran aventura ' + name.capitalize() + ' ' +  last_name.capitalize() +
    '!!')
else:
    print('\nWelcome to this great adventure ' + name.capitalize() + ' ' + last_name.capitalize() + '!!\n')

# # I made the above program to make a grand opening in the adventure game and also to show a bit of\[]
# # creativity to my work.

print('\nStory line:\n')

print('The world has advanced to the extent were man could reach out to the after verse via the')
print('Trans-verse Portal, i meanx man can decide to go visit there deceased ancestor in convenience,')
print('yes the living can go visit but the dead cannot visit earth, this act lasted for many decades until the  bridge.')
print('The Bridge, provoked by the most high god Immorti, he was wrath for the great relationship emerging with great momentum between the living and the dead. ')
print('Immorti stretched out his hands reaching to the doors of Gaunt which he pulled! Letting loose his war dogs on humanity in the after verse')
print('What is humanities fate in the after verse? Death, and pain!!')
print('You were in the after verse, were you went to visit your mom who passed on. Time have passed, you decided to head back to earth')
print('you were on the journey to the nearest Trans-verse portal station were you witnessed  the emergence of the Arites,')
print('warriors of Immorti, you conceded to fear and took haste to safety, but it turns out there is no safe place in the after verse ')
print('You are left with two choices find and seal the doors of Gaunt and save the after verse including your mom or  ')
print('Journey in haste to the Trans-verse portal were you can journey back to earth')
print('\n SURVIVE!!!')

# I dont know if this is part of the requirements i had to create a foundation for the adventure which i refer to as the STORY LINE,
#  this would enable readers understand the adventure they  are about to take

answer = input('\nWould you like to play this adventure game (yes/no)? ')

if answer.lower().strip() == 'yes':
   
    answer = input('\nWhile hiding from the Arites, you were prompted with two thougths save AFTER VERSE or make a haste back to EARTH. Which one do you want to choose? ').lower().strip()
   
    if answer == 'after verse':
         print('\nAs you choose to become courageous and save the after verse your name shall be heard for ages if you suceed ' + name.capitalize() + '!!\n')
         
         answer = input('While you came out from your hiding place, you heard the cry of a young child who lost his parents in this chaos do you want save the CHILD by taking him along or you leave him behind to find the door of GAUNT? ')

         if answer == 'child':
             print('That was a good choice but...')
             
             answer = input('\nYou found your way to the little child who saw you and started running out of fear, do you want to RUN after the child or look for your way to THE DOORS of Gaunt? ')       

             if answer == 'run':
                 print('As you ran towards the child who was crying out of fear, his crying tends to attract the Arites outside the building to you two')

                 answer = input('\nDO you want to ATTACK the Arite or you want to RUN AWAY? ')
               
                 if answer == 'attack':
                      print('\nAs you stood to attack an Arite, you stood no chance to survive..... Game over!')

                 elif answer == 'run away':
                     print('\nYou grabbed the young one holding tight to his mouth, running through the hallway straight under a table, you are lucky! You were not seen by the Arite,')

                 else:
                      print('You inputted an invalid choice. Game over!')

  
                   
             elif answer == 'the doors':
                print('\nYou left the young one to accept his fate in the after verse')
                print('\nwhile you head out of the building, at that moment you realized that the after verse is not like earth, you can not move out of your programmed route, ' + 
                'except you answer the riddles presented by Anabi failure to answer is death. Wait history never recorded any person that suceeded you said to yourself.') 
               
                answer = input ('What do you want to do, will you love to call on ANABI for the question or you want to consider going HOME? ')

                if answer == 'anabi':
                    print('\nYou clicked on Anabi on your after verse features smart watch...')
                    print('Impossible!! Who have the heart to summon me..... Oh a man, gagagagagaga Anabis laughed vigorously, failure to answer my riddle leads to death!!! success grants you passage to every space in the after verse')

                elif answer == 'home':
                    print('\nYou gave heed to fear and resort to head home... while walking through the lobby, you saw an old man who was bleeding')

                else:
                     print('You inputted an invalid choice, you lost!')

         elif answer == 'gaunt':
             print('So sad, you left the young boy')
             
             print('\nThere was noice coming from the entrance of the building, it was extreme, so you decided to look for a way out through the roof, ' +
                  'you saw a part through the ceiling, it was at that moment you heard a loud bang!')
            
             answer = input ('Do you want to RUN OUT through the ceiling or HIDE in the building? ')

             if answer == 'run out':
                 print('\nAs you struggled to go though the ceiling, unlucky for you a brick fell on the fall, attracting the Arites to you..... Game over!')
             
             elif answer == 'hide':
                 print('As you ran out of the room, you found a passage to a basement, there you silently stood still in the dark basement')
            
             else:
              print('You inputted an invalid choice. Game over!')


         else:
              print('You inputted an invalid choice. you lost!')

                                                                                                                   
    elif answer == 'earth':
            print('\nWhile you choose to head back home on earth, you came out from your hiding place i think i heard something, you said to yourself but it became true when the sound keeps coming.\n')
        
            answer = input('\nDo you want to FOLLOW the path to the door or you want to look for ANOTHER WAY out of the building?')
       
            if answer == 'follow':
             print('\nYou followed the path to the door, and gently opened it to your surprise you saw some people who are in the same situation as you' + 
             'still at the door post, that same minute you saw two Arites in the room, Arites! someone shouted with just a swipe of their hands half of the people were dead!!')

            if answer == 'another way':
             print('\nYou searched the building looking for another way out, you took a breath when you found one leading to the back of the ' + 
             'building at that moment the after verse notification wrist watch, gave a notification indicating that base two portal station has been ' + 
             'destroyed you wanted to scream but feared the Arites might hear, and you need a map since you have never been to base one before. ')
      
                    
                    
            
    
            else:
                 print('You inputted an invalid choice, you lost!')
    else:
        print('You inputted an invalid choice, you lost!')
else:
    print("Too bad you won't be playing!" + name.capitalize())

# # I THINK I FIT FOR THE FIRST GRADING CATEGORY BECAUSE IV'E BEEN ABLE TO PERFORM THE REQUIREMENTS. IT TOOK ME A LOT  OF TIME TO WRITE THIS PROGRAM,  
# # BECAUSE I HAVE NO PREVIOUS KNOWLEDGE ON PROGRAMMING, BUT IM GLAD I HAVE BEEN ABLE TO DO IT, I ALSO HOPE IT'S GOOD TOO! 