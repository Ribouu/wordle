# Wordle
Just a little project to see if I can apply what I learn everyday in class.

This is the wordle game (motus in french), in terminal. I plan to try to create the game with pygame soon. Feel free to use the code.

## Setup and Run

Requires **Python 3.7+**. You can download the latest version of Python [here](https://www.python.org/downloads/).

You'll need to install [ansicon](https://github.com/adoxa/ansicon).

    pip install ansicon

This package provides ANSI escape sequences, to display colors and to correctly delete lines in terminal.

To run it in a terminal :

    python main.py


If you don't have python or have troubles to install it but you want to try it anyway, I made a executable. You'll find it at build/wordle : wordle.exe.
To access it in terminal :

**Linux**

    build/wordle/wordle.exe

**Windows**

    build\wordle\wordle.exe

If you want to do it by yourself, install the package cx_Freeze :

    python pip install cx_Freeze

Then, modify the script setup.py (I commented it so you can understand what to do.) Finally,
execute it with the following command :

    python setup.py build


## Credits
Created by Ribou ([Twitter](ribou.fr/twitter), [Twitch](ribou.fr/twitch))

I got the data from [David Louapre](github.com/scienceetonnante) in his [WordleSutom project](github.com/scienceetonnante/WordleSutom), as I couldn't find any other list of words on the internet.

I learned from [this article](https://www.journaldunet.fr/web-tech/developpement/1441101-comment-convertir-un-programme-python-py-en-executable-exe/) how to convert a Python .py program into an .exe executable, from Journal Du Net. The script setup.py is from there.

Game obviously inspired from [Wordle](https://www.nytimes.com/games/wordle/index.html), and the French games [Sutom](https://sutom.nocle.fr/#) and [Le Mot](https://wordle.louan.me/).

