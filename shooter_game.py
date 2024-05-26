
#подключение нужных модулей
from pygame import * 
from random import randint 
from time import time as timer 

class GameSprite(sprite.Sprite):
    #конструктор класса 
    def __init__(self, xcor, ycor, width, height, speed, picture): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(picture),(width,height)) 
        self.rect = self.image.get_rect() 
        self.rect.x = xcor 
        self.rect.y = ycor 
        self.speed = speed 

    #метод перемещения игрока с клавиатуры
    def hero_run(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x >0: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x <850: 
            self.rect.x += self.speed 
 
    def enemy_go(self): 
        self.rect.y += self.speed 
     
    def bullet_go(self): 
        self.rect.y -= self.speed 
        if self.rect.y < -10: 
            self.kill() 
             
    def reset(self): 
        window.blit(self.image,(self.rect.x, self.rect.y)) 
 
# настройка игрового окна
window = display.set_mode((900,600)) 
display.set_caption('Шутер') 
background = transform.scale(image.load('galaxy.jpg'),(900,600)) 
 
'''mixer.init() 
mixer.music.load('space.ogg') 
mixer.music.play(-1)''' 

# создание игровых обьектов
hero = GameSprite(450,500,50,50,10,'rocket.png') 
enemy = GameSprite(randint(50,850),0,50,50,randint(5,10),'ufo.png') 
enemy2 = GameSprite(randint(50,850),0,50,50,randint(5,10),'asteroid.png') 
enemy3 = GameSprite(randint(50,850),0,50,50,randint(5,10),'ufo.png') 
enemy4 = GameSprite(randint(50,850),0,50,50,randint(5,10),'asteroid.png') 
enemy5 = GameSprite(randint(50,850),0,50,50,randint(5,10),'asteroid.png') 
enemy6 = GameSprite(randint(50,850),0,50,50,randint(5,10),'asteroid.png') 
 
lives = 3 # счетчик жизней  
killed = 0
seconds = 60
# создаем шрифт 
font.init() 
font1 = font.Font(None, 42) 
 
lives = 15
killed = 0
 
enemies = [enemy, enemy2, enemy3, enemy4, enemy5, enemy6] 
bullets = sprite.Group() 
 
start = timer()

game = True
#игровой цикл 
while game: 
    stop = timer() 

    window.blit(background, (0,0)) 
    lives_text = font1.render('Жизни:'+ str(lives), 1, (255,255,255)) 
    window.blit(lives_text, (750,50)) 
    killed_text = font1.render('Убийств:' + str(killed),1,(255,255,255))
    window.blit(killed_text, (10,60))
    second_text = font1.render('Время:'+ str(seconds), 1, (255,255,255))
    window.blit(second_text, (750,250))

    if stop - start > 1:
        seconds -= 1 
        start = stop

    for ev in event.get(): 
        if ev.type == QUIT: 
            game = False 
        if ev.type == KEYDOWN: 
            if ev.key == K_r: 
                lives = 3 
                killed = 0
                seconds = 60
                for enemy in enemies: 
                    enemy.rect.y = - 10 
                    enemy.rect.x = randint(50,850) 
                    enemy.speed = randint(6,11) 
            if ev.key == K_SPACE: 
                bullet = GameSprite(hero.rect.x + 20, hero.rect.y, 10, 20, 15, 'bullet.png') 
                bullets.add(bullet) 
 
    if enemy.rect.y > 600: 
        enemy.rect.y = 10 
        enemy.rect.x = randint(50,850) 
        enemy.speed = randint(6,11) 
    if enemy2.rect.y > 600: 
        enemy2.rect.y = 10 
        enemy2.rect.x = randint(50,850) 
        enemy2.speed = randint(6,11) 
    if enemy3.rect.y > 600: 
        enemy3.rect.y = 10 
        enemy3.rect.x = randint(50,850) 
        enemy3.speed = randint(6,11) 
    if enemy4.rect.y > 600: 
        enemy4.rect.y = 10 
        enemy4.rect.x = randint(50,850) 
        enemy4.speed = randint(6,11) 
    if enemy5.rect.y > 600: 
        enemy5.rect.y = 10 
        enemy5.rect.x = randint(50,850) 
        enemy5.speed = randint(6,11) 
    if enemy6.rect.y > 600: 
        enemy6.rect.y = 10 
        enemy6.rect.x = randint(50,850) 
        enemy6.speed = randint(6,11) 
     
    for enemy in enemies: 
        if sprite.collide_rect(hero, enemy): 
            lives -= 1 
            killed += 1
            enemy.rect.x = randint(50,850) 
            enemy.rect.y = 10 
             
    for bullet in bullets: 
        bullet.bullet_go() 

# оформление победы и проигрыша 
    if lives <= 0: 
        lose_text = font1.render('ВЫ ПРОИГРАЛИ', 1, (255, 255, 255)) 
        window.blit(lose_text, (325, 300)) 
        seconds = 60 
        for enemy in enemies: 
            enemy.speed = 0 
        hero.speed = 0
        for bullet in bullets:
            bullet.kill()
     
    if seconds <= 0:
        if killed >= 100:
            win_text = font1.render('ВЫ ПРОИГРАЛИ', 1, (255, 255, 255))
            window.blit(win_text, (325, 300))        
        seconds = 60 
        for enemy in enemies:
            enemy.speed = 0
        hero.speed = 0
        for bullet in bullets:
            bullet.kill()
     
    for enemy in enemies: 
        for bullet in bullets: 
            if sprite.collide_rect(enemy, bullet): 
                enemy.rect.x = randint(50,850) 
                enemy.rect.y = 10 
                enemy.speed = randint(6,11) 
                bullet.kill()
                killed  = killed + 1 
    hero.hero_run() 
    enemy.enemy_go() 
    enemy2.enemy_go() 
    enemy3.enemy_go() 
    enemy4.enemy_go() 
    enemy5.enemy_go() 
    enemy6.enemy_go() 
    hero.reset() 
    enemy.reset() 
    enemy2.reset() 
    enemy3.reset() 
    enemy4.reset() 
    enemy5.reset() 
    enemy6.reset() 
    bullets.draw(window) 
    display.update() 
    time.delay(50)