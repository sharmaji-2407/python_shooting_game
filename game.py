import pygame, random , math

#path
path = "begin_game"


#initialising pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800,600))
#backgroung
#back = pygame.transform.scale(pygame.image.load(path+'/data/background.png'),(800,1200))
#backX = 0

    

#Title and icon
pygame.display.set_caption("SHARMAJI")
icon = pygame.image.load(path+'/data/spaceship.png')
pygame.display.set_icon(icon)







#player
player_image = pygame.image.load(path+'/data/player.png')
player_smk = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(path+'/data/smk.png'), (200, 115)),90)
playerX = 368
playerY = 480
player_movement = 0.5
playerX_change = 0
#player function
def player(x,y):
    
    screen.blit(player_smk,(x-30, y+45))
    screen.blit(player_image,(x, y))
#score
score_val = 0
font = pygame.font.Font(path+'/data/spaceinvaders.ttf',20)
textX = 600
textY = 550

def show_score(x,y):
    score = font.render("Score : "+str(score_val),True,(255,255,255))
    screen.blit(score, (x,y))







#enemy
num_enemy = 5
enemy_image =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range (num_enemy):
    enemy_image.append(pygame.image.load(path+'/data/meteor.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    enemy_movement = 0.5
    enemyX_change.append(enemy_movement)
    enemyY_change.append(10)
def enemy(x,y,i):
   
    screen.blit(enemy_image[i],(x, y))






#bullet

bullet_image = pygame.transform.scale(pygame.image.load(path+'/data/bullet.png'),(15, 20))
bulletX = 0
bulletY = 480
bullet_state = "ready"  # ready -> bullet ready to fire (non-visible) and fire -> bullet is fired (visible)
bulletY_change = 2.5
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16, y+10))
    #when player increases to level 2 or get's a 1up
    #screen.blit(bullet_image,(x+25, y+10))

#collision
def isCollision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    if dist <= 27:
       return True
    else:
        return False 
   

    

   
    
# game loop
control = "mouse"
running = True

while running:
    

    screen.fill((12,9,17))

    #background
    #for i in range(100):
    #    backX+=0.8
    #screen.blit(back, (0,backX))
    #if backX>= 800:
    #    backX=-800

        

    


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    control = "keyboard"
                if event.key == pygame.K_m:
                    control = "mouse"
        
        if control == "keyboard":
            playerY = 480
            #if key stroke is pressed check wether is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = -player_movement
                    
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = player_movement
                    
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    if bullet_state is "ready":
                        bulletX = playerX
                        fire_bullet(bulletX,bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_w:
                    playerX_change = 0
            
        if control == "mouse":    
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if bullet_state is "ready":
                                bulletX = playerX
                                bulletY = playerY
                                fire_bullet(bulletX,bulletY)
                                
            mouse_pos = pygame.mouse.get_pos()
            playerX = mouse_pos[0] - 32
            if mouse_pos[1] >=450:
                playerY = mouse_pos[1] - 32
            elif mouse_pos[1] <450:
                playerY = 450-32

                
                
                
    
    #player movement
    playerX += playerX_change

    # setting boundaries
    if playerX <=-4:
        playerX = 0
    elif playerX >=740:
        playerX = 736
    


    #enemy movement 
    for i in range (num_enemy): 
        enemyX[i] += enemyX_change[i]
        # setting boundaries
        if enemyX[i] <=-4:
            enemyX_change[i] = enemy_movement
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >=740:
            enemyX_change[i] = -enemy_movement
            enemyY[i]+=enemyY_change[i]
        #collision    
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        
        if collision and bullet_state == "fire":
            bulletY = 480
            bullet_state = "ready"
            score_val += 10
            
            enemyX[i] = 900 #random.randint(0,736)
            enemyY[i] = 700 #random.randint(0,150)
        if enemyY[i] >=480:
            
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(0,150)
        enemy(enemyX[i],enemyY[i],i)
        

    
    


    #BulletMovement
    if bulletY <=0:
        bulletY=480
        bullet_state = "ready"
    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    
        
    
    player(playerX,playerY)
    show_score(textX,textY)
    
    
    pygame.display.update()