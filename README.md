flaming-ironman
===============

Installazione
-------------

Per installare le dipendenze create un virtualenv nella cartella del clone del progetto:

```
$ virtualenv venv
```

Fatto questo si attiva il virutalenv:

```
# per bash:

$ source venv/bin/activate

# per fish:

$ source venv/bin/activate.fish
```

e si procede con l'installazione delle dipendenze, siccome cocos ha bisogno di pyglet alpha, ci sta che l'installazione vi fallisce, allora installare prima pyglet a mano:

```
$ pip install --upgrade http://pyglet.googlecode.com/archive/tip.zip

$ pip install -r requirements.txt
```

così dovrebbe funzionare..

per provare se va tutto:

```
$ python flaming-iroman.py 
```

enjoy!

