from msilib.schema import Class
import pygame as pg
import sys
import random

class Screen:
    def __init__(self,title,size,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size) # Surface
        self.rct = self.sfc.get_rect() 
        self.bgi_sfc = pg.image.load(file) # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    def __init__(self,file,bairitsu,xy): # xy:初期座標
        self.sfc=pg.image.load(file)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, float(bairitsu))
        self.rct=self.sfc.get_rect()
        self.rct.center=xy
    def blit(self,SCobj):
        SCobj.sfc.blit(self.sfc, self.rct)
    def update(self,SCobj):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        if check_bound(self.rct, SCobj.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(SCobj)

class Bomb:
    def __init__(self,color,r,v,SCobj): # v:x方向速度とy方向速度のタプル
        self.sfc=pg.Surface((20, 20))
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc, color, (10, 10), r)
        self.rct=self.sfc.get_rect()
        self.rct.centerx = random.randint(0, SCobj.rct.width)
        self.rct.centery = random.randint(0, SCobj.rct.height)
        self.vx=+int(v[0])
        self.vy=+int(v[1])
    def blit(self,SCobj):
        SCobj.sfc.blit(self.sfc, self.rct)
    def update(self,SCobj):
        self.rct.move_ip(self.vx, self.vy)
        # 外枠に触れると-1を返す(yokoかtate)
        yoko, tate = check_bound(self.rct, SCobj.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(SCobj)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

def main():
    clock = pg.time.Clock()
    screen=Screen("逃げろ！こうかとん",(1600, 900),"ex04/pg_bg.jpg")
    bird=Bird("ex03/fig/8.png",2.0,(900,400))
    bomb=Bomb((255,0,0),10,(1,1),screen)

    while True:
        screen.blit()
        bird.update(screen)
        bomb.update(screen)
        for event in pg.event.get(): # イベントキューからキーボードやマウスの動きを取得
            if event.type == pg.QUIT: # 閉じるボタンが押されたら終了
                return 
        if bird.rct.colliderect(bomb.rct): # 爆弾に触れたら終了
            return 
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()