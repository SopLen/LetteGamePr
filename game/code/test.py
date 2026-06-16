import pgzrun

WIDTH = 1920
HEIGHT = 1080

# Weltgröße
WORLD_WIDTH = 3000
WORLD_HEIGHT = 300


# Spieler
spieler = Actor("spieler_front")
spieler.pos = (0, 0)
animations ={"up": ["spieler_back", "spieler_back_step1", "spieler_back", "spieler_back_step2"],
             "down":  ["spieler_front", "spieler_front_step1", "spieler_front", "spieler_front_step2"],
             "left": ["spieler_left", "spieler_left_step1", "spieler_left", "spieler_left_step1"],  
             "right": ["spieler_right", "spieler_right_step1", "spieler_right", "spieler_right_step2"]}

direction = ""

# Lootbox
lootbox = Actor("test_lottbox")
lootbox.pos = (800, 600)

background = Actor("test_background")
background.pos = (0,0)


# Kamera
camera_x = 0
camera_y = 0


def draw():
    screen.clear()
    screen.fill("darkblue")

    screen.blit("test_background", (lootbox.x - camera_x, lootbox.y - camera_y))

    # Weltobjekte mit Kamera zeichnen
    screen.blit(
        background.image,
        (background.x - camera_x, background.y - camera_y)
    )
    screen.blit(
        lootbox.image,
        (lootbox.x - camera_x, lootbox.y - camera_y)
        )

    screen.blit(
        spieler.image,
        (spieler.x - camera_x, spieler.y - camera_y)
    )

    # Text wenn nah
    if spieler.colliderect(lootbox):
        screen.draw.text(
            "Druecke E",
            (lootbox.x - camera_x, lootbox.y - camera_y - 40),
            color="white",
            fontsize=40
        )


def update():
    global camera_x, camera_y, frame, direction

    moving = False
    SPEED = 5

    if keyboard.left:
        if spieler.x > 10:
            spieler.x -= SPEED
        direction = "left"
        moving = True

    if keyboard.right:
        if spieler.x < WORLD_WIDTH -10:
            spieler.x += SPEED
        direction = "right"
        moving = True

        spieler.image = "spieler_right"
    if keyboard.up:
        if spieler.y >10:
            spieler.y -= SPEED
        direction = "up"
        moving = True
    if keyboard.down:
        if spieler.y < WORLD_HEIGHT -10:
            spieler.y += SPEED
        direction = "down"
        moving = True

    if moving:
        frame +=0.2
        frames = animations[direction]
        spieler.image = frames[int(frame) % len(frames)]
    else:
        spieler.image = "spieler_front"
        frame = 0

    
    # Kamera folgt Spieler
    camera_x = spieler.x - WORLD_WIDTH // 2
    camera_y = spieler.y - WORLD_HEIGHT // 2



    # Loot öffnen
    if keyboard.e and spieler.colliderect(lootbox):
        print("LOOT GEÖFFNET!")


    getInfo()



def getInfo():
    if keyboard.i:
        print(spieler.width)
        print(spieler.height)

pgzrun.go()