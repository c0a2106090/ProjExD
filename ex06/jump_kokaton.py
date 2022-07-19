import pygame as pg
import sys
import random
import numpy as np

#スクリーン用クラス
class Screen:
    def __init__(self, title, wh: tuple, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(img).convert()
        self.bg_x = 0

    def blit(self):
        #背景を動かして描画する
        self.sfc.blit(self.bg_sfc, [self.bg_x - self.rect.width, 0])
        self.sfc.blit(self.bg_sfc, [self.bg_x, 0])
        self.bg_x = (self.bg_x - 5) % self.rect.width

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
    def __init__(self, img, size: float, speed, screen: Screen):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.x = screen.rect.width + self.rect.width
        self.rect.y = screen.rect.height - self.rect.height
        self.vx = -1 * speed
        self.vy = 0

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        self.rect.move_ip(self.vx, self.vy)
        self.blit(screen)


def main():
    #fpsのカウント開始
    clock = pg.time.Clock()
    sc = Screen("飛べ！こうかとん", (1600, 900), "../fig/bg_sabaku.jpg")
    tori = Bird("../fig/2.png", 2.0, sc)
    obs = Obstacle("../fig/sabo_ver02.png", 4.0, 10, sc)
    obs2 = Obstacle("../fig/sabo_ver02.png", 2.0, 12, sc)

    #描画
    while True:
        
        sc.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tori.update(sc)
        obs.update(sc)
        obs2.update(sc)

        if tori.rect.colliderect(obs.rect) or tori.rect.colliderect(obs2.rect):
            Quit(sc)
            

        #障害物が画面外に出たときに再配置する
        if obs.rect.x <  -1 * random.randint(obs.rect.width, obs.rect.width * 5):
            obs.rect.x = sc.rect.width + obs.rect.width
        if obs2.rect.x <  -1 * random.randint(obs2.rect.width, obs2.rect.width * 5 ):
            obs2.rect.x = sc.rect.width + obs2.rect.width
        pg.display.update()
        clock.tick(120)

def Quit(sc): #リスタート機能(C0A21060)
    END_flg=True
    #font1 = pg.font.SysFont(None, 40)
    #text1 = font1.render("GAME OVER", False, (255,255,255))
    #text2 = font1.render("Press Any Key to Re-Start", False, (255,255,255))
    while END_flg==True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                END_flg = False
            elif event.type == pg.KEYDOWN: # もしも何かしらのキーが押されたら
                END_flg = False # メイン関数を呼び出す(=やり直し)
                main()
    pg.quit()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()