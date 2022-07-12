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

def main():
    clock = pg.time.Clock()
    screen=Screen("逃げろ！こうかとん",(1600, 900),"ex04/pg_bg.jpg")
    screen.blit()

    # 練習3：こうかとん
    kkimg_sfc = pg.image.load("ex03/fig/8.png")    # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  # Surface
    kkimg_rct = kkimg_sfc.get_rect()          # Rect
    kkimg_rct.center = 900, 400

    # 練習5：爆弾
    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect() # Rect
    bmimg_rct.centerx = random.randint(0, screen.rct.width)
    bmimg_rct.centery = random.randint(0, screen.rct.height)
    vx, vy = +1, +1 # 練習6

    while True:
        screen.sfc.blit(screen.bgi_sfc, screen.bgi_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # 練習4
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        # 練習7
        if check_bound(kkimg_rct, screen.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
        screen.sfc.blit(kkimg_sfc, kkimg_rct)

        # 練習6
        bmimg_rct.move_ip(vx, vy)
        # 練習5
        screen.sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習7
        yoko, tate = check_bound(bmimg_rct, screen.rct)
        vx *= yoko
        vy *= tate

        # 練習8
        if kkimg_rct.colliderect(bmimg_rct): return 

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