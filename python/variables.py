from classes import *

player = characters()


fakard = weapon('fakard (1)', 1, 0)
marvanykard = weapon(name='márványkard (3)', damage=3, price=35)
vaskard = weapon(name='vaskard (6)', damage=6, price=55)
obszidianel = weapon(name='obszidiánél (11)', damage=11, price=110)

fapancel = armor(name='fapáncél (1)', shield=1, price=55)
marvanypancel = armor(name='marvanypáncél (2)', shield=2, price=105)
vaspancel = armor(name='vaspáncél (5)', shield=5, price=210)
obszidianpancel = armor(name='obszidianpáncél (11)', shield=11, price=320)

fapajzs = shield(name='fapáncél (1)', shield=1, price=25)
marvanypajzs = shield(name='marvanypáncél (2)', shield=2, price=55)
vaspajzs = shield(name='vaspáncél (5)', shield=5, price=105)
obszidianpajzs = shield(name='vaspáncél (11)', shield=11, price=210)

goblin = Enemies(name='goblin', hp=5, strength=4, speed=2, shield=5)
ogre = Enemies(name='ogre', hp=10, strength=7, speed=4, shield=10)
bandit = Enemies(name='bandit', hp=7, strength=11, speed=5, shield=12)
cerberus = Enemies(name='cerberus', hp=15, strength=16, speed=3, shield=8)
vampir = Enemies(name='vampir', hp=20, strength=14, speed=2, shield=11)

mineboss = Enemies(name='Bánya boss', hp=50, strength=20, speed=4, shield=25)
forestboss = Enemies(name='erdő boss', hp=100, strength=25, speed=2, shield=35)
fieldboss = Enemies(name='mező boss', hp=75, strength=23, speed=6, shield=30)
dragon = Enemies(name='sárkány', hp=250, strength=45, speed=10, shield=50)



money = 0
nowplace = 'city'
hour = 6
minute = 0
day = 0
Palvolt = False
lo = False

WEAPON = [
    fakard,
    marvanykard,
    vaskard,
    obszidianel
]

ARMOR = [
    fapancel,
    marvanypancel,
    vaspancel,
    obszidianpancel
]

SHIELD = [
    fapajzs,
    marvanypajzs,
    vaspajzs,
    obszidianpajzs,
]

Cshield = [

]

Cweapon = [
    fakard
]

Carmor = [

]

inv = [

]

BOSSES = [
    'mineBoss',
    'forestboss',
    'kazamatboss',
    'dragonlayerboss',
    'fieldboss',
    'dragon'
]

QUESTS = [
    'pénzgyűjtés fegyverre',
    'vadászat',
    'gyűjtőgetés',
    'ogrevadászat',
    'király kísérés'
]

universialquest = [
    'özvegy néni férje',
    'lovagi torna',
    'kard a kőben',
    'elaltatni a sárkányt',
    'meglopni a sárkányt'
]

Dquest = [

]

PAL = [
    'opál',
    'kapál',
    'kalimpál',
    'kalapál',
    'gyepál',
    'pálca',
    'pálinka',
    'pálma',
    'pálmafa',
    'pálfordulás',
    'pumpál',
    'nepál',
    'bepáll',
    'pipál',
    'kupál',
    'bekrepál',
    'strapál',
    'rúgkapál',
    'kupál'
]

pal = [
    'opál',
    'kapál',
    'kalimpál',
    'kalapál',
    'gyepál',
    'pálca',
    'pálinka',
    'pálma',
    'pálmafa',
    'pálfordulás',
    'pumpál',
    'nepál',
    'bepáll',
    'pipál',
    'kupál',
    'bekrepál',
    'strapál',
    'rúgkapál',
    'kupál'
]

PLACE = [
    'mine',
    'mountain'
    'forest',
    'kazamata',
    'dragonlayel',
    'field',
    'city'
]

aranyBoundle = [
    'szén',
    'vas',
    'szén',
    'vas',
    'arany'
]

vasBoundle = [
    'arany',
    'szén',
    'arany',
    'arany',
    'vas'
]

szenBoundle = [
    'szén',
    'vas',
    'szén',
    'vas',
    'arany'
]

currentquest = QUESTS[1]

# OPICÓS LISTÁK

opcio4 = ['0', '1', '2', '3', '4']
opcio5 = ['0', '1', '2', '3', '4', '5']
opcio6 = ['0', '1', '2', '3', '4', '5', '6']