import pygame as pg
import sys
import random
import time
import math

dif = 0
#スクリーン用クラス
class Screen:
    def __init__(self, title, wh: tuple, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(img).convert()
        self.bg_x = 0

#<C0A21022>
    #ゲームオーバー表示
    def game_over_screen(self, dif):
        font = pg.font.Font(None, 150)
        txt = font.render("GameOver", True, (255, 0, 0))
        self.text(txt, (540, 350))
        font = pg.font.Font(None, 40)
        txt = font.render("Press R KEY TO RESTART", True, (0, 0, 0))
        self.text(txt, (640, 650))
        font = pg.font.Font(None, 40)
        txt = font.render("Press Esc KEY TO CLOSE", True, (0, 0, 0))
        self.text(txt, (640, 700))
        font = pg.font.Font(None, 100)
        text = font.render("SCORE: " + str(dif),True,(64,155,63))
        self.text(text, (560, 500))
        pg.display.update()
#</C0A21022>

    def blit(self):
        #背景を動かして描画
        self.sfc.blit(self.bg_sfc, [self.bg_x - self.rect.width, 0])
        self.sfc.blit(self.bg_sfc, [self.bg_x, 0])
        self.bg_x = (self.bg_x - 5) % self.rect.width
#<C0B21180>
    def text(self,text, p: tuple):
        self.sfc.blit(text,[p[0], p[1]])
#</C0B21180>


#こうかとん用クラス
class Bird:
    def __init__(self, img, size: float, screen: Screen):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.center = self.rect.width, (screen.rect.height - self.rect.height) // 2
        self.gy = 0

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        #スペースキーを押した時にジャンプする部分
        key = pg.key.get_pressed()
        if self.rect.y >= 750:
            self.rect.y = 750
            if key[pg.K_SPACE]:
                self.gy = -25
        #重力の計算
        self.gy += 1
        if self.gy > 15:
            self.gy = 15
        self.rect.y += self.gy 
        self.blit(screen)


#障害物用クラス
class Obstacle:
    def __init__(self, img, size: float, speed, height: tuple, screen: Screen):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.x = screen.rect.width + self.rect.width
        self.rect.y = screen.rect.height - self.rect.height - random.randint(height[0], height[1])
        self.vx = -1 * speed
        self.vy = 0

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        self.rect.move_ip(self.vx, self.vy)
        self.blit(screen)


def main():
    global dif
    #fpsのカウント開始
    pg.init()
    clock = pg.time.Clock()
    sc = Screen("飛べ！こうかとん", (1600, 900), "ex04/bg_sabaku.jpg")
    tori = Bird("ex03/fig/8.png ", 2.0, sc)

#<C0A21006>
    obs = Obstacle("data\サボテンver01.png", 4.0, 10, (0, 0), sc)
    obs2 = Obstacle("data\サボテンver02.png", 2.0, 12, (0, 0), sc)
    obs_tori = Obstacle("data\鳥ver01.png", 2.0, 8, (50, 200), sc)
#</C0A21006>

#<C0B21180>
    start = time.time()
#</C0B21180>

    #描画
    while True:
        
        sc.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()

        tori.update(sc)
        obs.update(sc)
        if dif >= 5:
            obs2.update(sc)
        if dif >= 10:
            obs_tori.update(sc)

        collision(tori.rect, obs.rect, sc)
        collision(tori.rect, obs2.rect, sc)
        collision(tori.rect, obs_tori.rect, sc)

        respawn(obs, (0, 0), sc)
        respawn(obs2, (0, 0), sc)
        respawn(obs_tori, (50, 200), sc)

#<C0B21180>
        end = time.time()
        dif = end - start 
        dif = math.floor(dif)
        font = pg.font.Font(None,100)
        text = font.render(str(dif),True,(64,255,63))
        sc.text(text, (10,5))
#</C0B21180>

        pg.display.update()
        clock.tick(120)

#衝突処理
def collision(tori, obs, screen: Screen):
    if tori.colliderect(obs):
        screen.game_over_screen(dif)
        quit()

#<C0A21060>
#衝突後のリスタート等の処理
def quit():
    END_flg=True
    while END_flg==True:
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                END_flg = False
            elif pg.key.get_pressed()[pg.K_r]:
                END_flg = False
                main()
    pg.quit()
    sys.exit()
#</C0A21060>

#障害物が画面外に出たときに再配置する
def respawn(obs: Obstacle, height: tuple, screen: Screen):
    if obs.rect.x <  -1 * random.randint(obs.rect.width, obs.rect.width * 5):
            obs.rect.x = screen.rect.width + obs.rect.width
            obs.rect.y = screen.rect.height - obs.rect.height - random.randint(height[0], height[1])

if __name__ == "__main__":
    main()