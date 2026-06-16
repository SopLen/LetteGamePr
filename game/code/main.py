import pgzrun

WIDTH = 1920
HEIGHT = 1080

spieler =Actor("spieler")

lootbox = Actor("lottbox")
lootbox.pos = (600, 500)
lootbox.scale = 0.1

def draw():
    screen.clear()

    screen.fill("darkblue")

    lootbox.draw()
    spieler.draw()
    


    

def update():


    SPEED = 5

    if keyboard.left:
        if spieler.x > 10:
            spieler.x -= SPEED
        spieler.image = "spieler_left"
    if keyboard.right:
        if spieler.x < WIDTH -10:
            spieler.x += SPEED
        spieler.image = "spieler_right"
    if keyboard.up:
        if spieler.y >10:
            spieler.y -= SPEED
        spieler.image = "spieler_back"
    if keyboard.down:
        if spieler.y < HEIGHT -10:
            spieler.y += SPEED
        spieler.image = "spieler"

    if keyboard.e:
        if spieler.colliderect(lootbox):
            print("YEEEEEES")
        else: print("NOOOOOOOOO")



pgzrun.go()