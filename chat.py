#!/usr/bin/python

import string
import random

#EmoChat
#Chatbot from the persepctive a totally apathetic teenager
#who is somewhat rude and could care less that he/she is
#in a conversation.

def respond(s,v):
        if 'need' in s:
                choice =  random.randint(0,len(v[0])-1)
                response = v[0][choice]
                return response
        if 'i am' in s:
                choice =  random.randint(0,len(v[1])-1)
                response = v[1][choice]
                return response
        if 'are you' in s:
                choice =  random.randint(0,len(v[2])-1)
                response = v[2][choice]
                return response
        if 'what' in s:
                choice =  random.randint(0,len(v[3])-1)
                response = v[3][choice]
                return response
        if 'how' in s:
                choice =  random.randint(0,len(v[4])-1)
                response = v[4][choice]
                return response
        if 'happy' in s:
                choice =  random.randint(0,len(v[5])-1)
                response = v[5][choice]
                return response
        if 'you are' in s:
                choice =  random.randint(0,len(v[6])-1)
                response = v[6][choice]
                return response
        if 'bot' in s:
                choice =  random.randint(0,len(v[7])-1)
                response = v[7][choice]
                return response
        if '?' in s:
                choice =  random.randint(0,len(v[8])-1)
                response = v[8][choice]
                return response
        if '.' in s:
                choice =  random.randint(0,len(v[9])-1)
                response = v[9][choice]
                return response
        if 'quit' in s:
                choice =  random.randint(0,len(v[11])-1)
                response = v[11][choice]
                return response
        else:
                choice = random.randint(0,len(v[10])-1)
                response = v[10][choice]                  
                return response

options = [
          ["need",
          [     "Who cares about that?  ",
                "Why would anyone need that?  "]],     

          ["i am",             
          [     "That is literally the most boring thing I have ever heard...  ",
                "Stop talking about yourself...  ",    
                "If I were that way would people care about me?  "]],

          ["are you",     
          [     "Why do you care?  ",                  
                "Maybe I am, what of it?  ",
                "No one understands me!  "]],

          ["what",
          [     "Ugh...why are you still here?  ",
                "...  ",       
                "What does it matter?",
                "Does that make you feel better about yourself?  "]],

          ["how",              
          [     "How would I know?  ",
                "Like...whatever...  ",                
                "If you have to ask, you will never know.  "]],

          ["happy",       
          [     "What would I know about happiness?  "]],

          ["you are",          
          [     "Why am I?  ",
                "I bet you would like it if I was...  "]],

          ["bot",              
          [     "Robots don't FEEL like I do...the sadness...*tear*  "]],

          ["?",
          [     "Why do you care about that?  ",
                "Like...whatever I guess...  ",
                "What?  ",
                "You would know...  "]],

          [".",        
          [     "I mean, if you say so...  ",       
                "I don't care.  ",      
                "Gah...  ",    
                "Ugh...  ",
                "Only a robot would say something like that.  ",
                "Just go away.  ",                        
                "STOP TALKING TO ME NERD!  ",
                "It's too bright in here...  ",
                "Whatever helps you sleep at night.  "]],

          ["",
          [     "Duh...whatever... ",                  
                "Just go away already... ",
                "Go away... ", 
                "This is getting painful... ",
                "I bet you're a chatbot... ",          
                "Why won't you leave me alone?! ",
                "So dark in here... ",
                "I wish it would rain... ",
                "... ",                                
                "As if... ",                
                "What's the point of talking to you? "]],


          ["quit",
          [     "Yeah...whatever...don't come back.  ",
                "Ugh...it's about time.  "]]
          ]

values = map(lambda x:x[1],options)

name = raw_input('Hi, I guess...What\'s your name? Not that I care... \n')
print 'Ugh...whatever, ', name, '...\n'
print 'Please say "quit" as soon as possible so I can stop talking to you...\n'
line = raw_input("What's up? \n")

while line !="quit":
        line = line.lower()    
        reply = respond(line,values)
        line = raw_input(reply + '\n')
