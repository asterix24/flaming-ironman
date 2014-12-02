flaming-ironman
===============

Installazione
-------------

Per installare le dipendenze create un virtualenv nella cartella del clone del progetto:

<code>
$ virtualenv venv
</code>

Fatto questo si attiva il virutalenv:

per bash:

<code>
$ source venv/bin/activate
</code>

per fish:

<code>
$ source venv/bin/activate.fish
</code>

e si procede con l'installazione delle dipendenze, siccome cocos ha bisogno di pyglet alpha, ci sta che l'installazione vi fallisce, allora installare prima pyglet a mano:

<code>
$ pip install --upgrade http://pyglet.googlecode.com/archive/tip.zip

$ pip install -r requirements.txt
</code>

così dovrebbe funzionare..

per provare se va tutto:

<code>
$ python flamming-iroman.py 
</code>

enjoy!

