# Introduction

If JARVIS had a trial version this would be it. 

Meet Olympia. She's an open-source, modular personal assistant. While Olympia boasts many built-in features, anyone can easily add their own features in, quite effortlessly.

So far, she can only cope with Windows. However, head over to testing-branch if you want to help change that.


# Installation

### Note: this has only been tested on Windows. testing-branch is the cross-platform version but still under development

0. Download Python (https://www.python.org/downloads/) if you haven't already. Any version above 3.2 should be fine.

1. Download the repository as a zip file. Extract the zip file to any location

2. Navigate to the Olympia-master file in cmd/Terminal

3. run: pip install -r requirements.txt

4. run: python setup.py

5. Navigate to the Olympia-master/code file

6. run: python main.py (scroll down to troubleshooting if you're getting any errors)

7. Enjoy!


## Quick-start guide

After spending about an hour ironing out errors with libraries, you should finally be able to run Olympia. To activate Olympia, simply say "Olympia". Wait for the single beep, and then speak your command. When you hear a double-beep, that means Olympia is processing what you just said.


## Features

### Currently, the personal assistant can do the following:

-Tell you the weather  

-Answer a question (e.g "What is a tree?" , or "what is astronomy")

-Answer any general-knowledge question - activated by saying "Can I ask you a question?" and when prompted, ask the question (e.g "How far away is the Sun from the Earth?", or "Who is the CEO of Github?")

-Define, spell and find synonyms of a word

-Give you the news

-Tell you a joke

-Stream some music

-Answering math questions - what's 2+2, factorials, square roots, you get the idea.

-Reminders, alarms, to-do lists, etc.

-Showing you a random XKCD

### Things I'm currently working on:

-World domination

-Fixing bugs

-Having a basic conversational skills ("How are you?", "Have a nice day", etc.)

-Allowing you to translate a word from English to any other language


### Things I'm thinking on working on:

-Natural Language Processing instead of looking for 'activation words'

-Using twilio to send text alerts

-Integrating it with Philips Smart Lights to turn lights on and off

-Sports news

-Making Olympia able to communicate and comprehend multiple languages.


## Modularity

To add a new module, it's just a matter of adding 3-4 lines of code in determiner.py file, which will help Olympia determine if your module is being activated, and coding the actual module itself - the module must take the form of a function that takes in inputs from the calling program (e.g what the user said) and returns what Olympia should "say" in return.

1. Write your module in the 'code' file. It should be in the form of a single function (which can contain multiple functions within it), and take userinput (which is what the user said) and return an output (what Olympia should say or do in return)

2. Open code\determiner.py. Under the function "whichModule", write your own function which will return a unique keyword if a specific action word is detected (e.g. for music, an action word could be "play"). If no action word is detected, the function should just return. The function name should be "about(what your function is about)" (e.g. aboutMusic)

3. Go down until you find the declaration of a list called modules. Append that list with the name of your function, e.g. Music. Leave out the "about"

4. Go up to the very top, to a function called conflict resolution. Append conflict_dict your previously chosen unique keyword along with the priority your module should have in the event of two modules having their keywords activated. The higher the number you assign to your module, the more preferable it will be in the event of a clash.

5. Go to main.py, and under the line "whatToRun=determine(choice)", add an if (or elif) statement which reads: "elif whatToRun==[unique keyword]:" and then write the code that should be executed. Usually, this includes importing the module you wrote previously, running it and voiceOutputting the result


## Commands (you must say "Olympia" before each command and wait for the beep)

"Play (song name)"

"Give me the headlines"

"Give me the news from the (BBC/Washington Post/Fox News/CNN/Huffington Post)"

"What's the weather like tomorrow?"

"What's the weather like today?"

"What's the weather like in x days" (note: x cannot be larger than 10)

"Tell me a joke"

"What is (thing)"...."Tell me more about (thing)" [searches wikipedia for (thing)]

"Define (word)"

"What's the synonym of (word)?"

"Spell (word)"

"Can I ask you a question?" (wait for confirmation) (question)

"Show me an xkcd"

"What's (maths question)"

"Set a reminder for the (date)"

"Set an alarm for (time in P.M./A.M.) on the (date)"

"Set a timer for 30 minutes"


## Troubleshooting

# OSError: [WinError 126] The specified module could not be found: (VLC)

1. Install VLC (https://www.videolan.org/vlc/index.html)

2. Search for libvlc.dll in the start menu

3. Open the containing folder of libvlc.dll

4. Copy the directory (e.g. C:\Users\Python Tutorials\Downloads\vlc-2.2.6-win64\vlc-2.2.6)

5. Go back to your start menu, search for "Edit environment variables for your account"

6. Edit the "PATH" variable, add a semicolon to the end of the variable value and paste the directory

7. Press Ok twice

# Error while installing pygame:

Try running: python -m pip install --upgrade pip

If that doesn't work, try this: https://stackoverflow.com/questions/41153444/installing-pygame-with-pip-command-python-setup-py-egg-info-failed-with-error

Re-run steps 2 and 3 of installation process
