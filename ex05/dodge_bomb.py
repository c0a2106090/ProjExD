from msilib.schema import Class
import pygame as pg
import sys
import random

class Screen:
    def __init__(self,title,size,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size) # Surface
        self.rct = self.sfc.get_rect() 
        self.bgi_sfc = pg.image.load(file)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
#    key_delta=
    def __init__(self,file,bairitsu,xy):
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
        

def main():
    clock = pg.time.Clock()
    screen=Screen("逃げろ！こうかとん",(1600, 900),"ex04/pg_bg.jpg")
    bird=Bird("ex03/fig/8.png",2.0,(900,400))

    # 練習5：爆弾
    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect() # Rect
    bmimg_rct.centerx = random.randint(0, screen.rct.width)
    bmimg_rct.centery = random.randint(0, screen.rct.height)
    vx, vy = +1, +1 # 練習6

    while True:
        screen.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        bird.blit(screen)
        bird.update(screen)

        # 練習6
        bmimg_rct.move_ip(vx, vy)
        # 練習5
        screen.sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習7
        yoko, tate = check_bound(bmimg_rct, screen.rct)
        vx *= yoko
        vy *= tate

        # 練習8
        if bird.rct.colliderect(bmimg_rct): return 

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()