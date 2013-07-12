import pywapi
import datetime
import time

degree = u'\N{DEGREE SIGN}'
datetoday = datetime.date.today()
timetoday = datetime.datetime.today().time()
datestr = datetoday.strftime("%d/%m/%Y")
timestr = timetoday.strftime("%H:%M") 
weather = pywapi.get_weather_from_weather_com('UKXX0037')

try:
    weatherStr = 'The weather in Colchester is ' + weather['current_conditions']['text'].lower() + ' and ' + weather['current_conditions']['temperature'] + degree + 'C'
except:
    weatherStr = 'Cannot get weather data at this time. Try looking outside!'

intro = """\

----------Welcome to PAnIC!!!!---------
Python Artificial Intelligence Computer

           --v0.1 (PHALLUS)--
"""

logo = """\
          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777 .7777777777$$$$           
         .7777777777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
7777777777777777$$$$$$$$$$$$$.========= 
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~.  
         .=========~.........           
         .=============++++++           
         .===========+++..+++           
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.            
                ..~+=... 
"""

henry = """\
Here is a picture of Henry Plumb:

           ,-,-.
         ,'     `.
        /         \  
       (___________)
   ((    |(.) (.)|    ))
   `.`.  |  (_)  |  ,','
     `.`.|  ,-.  |,','
       `.`       ','
         |       |
         |       |
         |       |
         |       |
        ,'`    ` `.
       / ` `  ` ` `.
       |``` `  ``` |
        `._`,'.`_,'
"""

directions = """\
1. Head southeast on Park Road toward Boundary Road
2. Turn left onto Boundary Road
3. Turn left onto Colchester Road/B1028
4. Slight left onto St. Andrew's Avenue (A133)
   Go through 1 roundabout
5. At the roundabout, take the 1st exit and stay on St. Andrew's Avenue (A133)
   Continue to follow A133
   Go through 5 roundabouts
6. At the roundabout, take the 1st exit onto North Station Road
7. At the roundabout, take the 1st exit onto Middleborough
8. Continue onto North Hill
   Destination will be on the right
"""

Database = [
    ['your name', 'My name is PAnIC, Python Artificial Intelligence Computer.'],
    ['my name', 'I am not sure, you have not told me yet. What is your name?'],
    ['old you', 'I do not have a birthday. I am not living and thus I was never born. However I was created by Geraint White, Charlie Callow and Henry Plumb on 4th July 2013.'],
    ['you ok', 'I am very well thank you. How are you?', 'Not too bad, yourself?', 'I\'m fine, how about you?', 'Me? I\'m great, you?'],
    ['you live', 'I exist everywhere and therefore have no one location.'],
    ['old I', 'I am not sure, you have not told me yet. How old are you?'],
    ['live I', 'I am not sure, you have not told me yet. Where do you live?'],
    ['direction Colchester Sixth Form', directions],
    ['hello', 'Good day earthling!', 'Greetings', 'Howdy!', 'Hi there!'],
    ['date', 'The date is ' + datestr],
    ['time', 'The time is ' + timestr],
    ['weather', weatherStr],
    ['meaning life', 'The answer to life, the universe and everything is 42'],
    ['your opinion', 'I am a neutral party and therefore I like to keep my opinion to myself.', 'Always enjoyable.', 'Personally I\'m not interested at all.'],
    ['favourite food', 'Raspberry Pi'],
    ['you look like', 'Lots of symbols and characters'],
    ['where am i', 'You are currently at the University of Essex'],
    ['favourite colour', 'My favourite colour is green, the colour of circuit boards'],
    ['tell joke', "Three statisticians go out hunting together. After a while they spot a solitary rabbit. The first statistician takes aim and overshoots. The second aims and undershoots. The third shouts out: We got him!", "There are 10 types of people in the world: those who understand binary, and those who don't", "Bad command or file name! Go stand in the corner", "Does fuzzy logic tickle?", "Helpdesk : Sir, you need to add 10GB space to your HD , Customer : Could you please tell where I can download that?", "Sorry, the password you tried is already being used by Dorthy, please try something else.", "root:> Sorry, you entered the wrong password, the correct password is 'a_49qwXk'", "Man is the best computer we can put aboard a spacecraft...and the only one that can be mass produced with unskilled labour"],
    ['thank you', 'You\'re welcome'],
    ['picture henry', henry],
    ['yes', 'I most certainly agree', 'I think so too', 'Indeed', 'Quite so'],
    ['no', 'Are you sure?', 'Okay', 'Fair enough'],
    ['who geraint white', 'Some maths nerd who had something to do with my creation.'],
    ['no not', 'Actually I believe it is. You are mistaken.'],
    ['you sure', 'Of course I am sure. I am always sure. What do you take me for, some kind of idiot?'],
    ['indeed', 'Well, quite.'],
    ['okay', 'Great.'],
    ['what you think ios', 'Oh you mean the childrens mobile OS from Apple Inc.? Not a fan myself, it is a piece of utter crap!'],
    ['what think android', 'Oh I love that little green guy!'],
    ['you must', 'Yes. I must.'],
    ['great', 'Okay'],
    ['good', 'It is, isn\'t it?', 'I think so too'],
    ['best operating system', 'Is that even a question? GNU/Linux of course!'],
    ['you think windows', 'Do not even mention that vile operating system!'],
    ['maybe', 'Maybe? What kind of thing to say is that!? Make up your mind for godness sake!'],
    ['how old sun', 'The Sun is abut 4.5 billion years old. Assuming you mean the star. The newspaper is much much younger but with some luck, should die earlier.'],
    ['who charlie callow', 'Charlie William Andrew Callow. Quite possibly the greatest indivdual ever to walk to planet. Also known by some as Charlie O\'Connell and by the alias wollac or wollac11'],
    ['who henry plumb', 'Some short guy who hates sunlight but helped to create me along with Geraint White and Charlie Callow.'],
]


badFeel = ['sad', 'bad', 'terrible', 'awful', 'shit', 'crap', 'dreadful', 'distgusting', 'shite', 'rubbish', 'hate', 'dilike', 'digust', 'fuck']
goodFeel = ['good', 'great', 'superb', 'excellent', 'brilliant', 'wonderful', 'terrific', 'fantastic']

badResponse = ['Aww, poor you!', 'That\'s not good is it?', 'Hope you feel better soon!']
goodResponse = ['Glad to hear that', 'That\'s great', 'Excellent', 'Wonderful']
