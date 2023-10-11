from Entities import *
from definialas import *
from variables import *
from threading import Thread
money = 0

x = Thread(target=xp, daemon=True)
x.start()
x.join()



