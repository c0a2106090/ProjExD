import pygame as pg
import sys
import random
bg_x=0
class Screen:
    def __init__(self,title,size,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size) # Surface
        self.rct = self.sfc.get_rect() # Rect
        self.bgi_sfc = pg.image.load(file).convert() # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self): # 背景をスクロールさせる
        global bg_x
        self.sfc.blit(self.bgi_sfc, [bg_x - self.rct.width, 0])
        self.sfc.blit(self.bgi_sfc, [bg_x, 0])
        bg_x = (bg_x - 5) % self.rct.width


class Bird:
    def __init__(self,file,bairitsu,xy): # xy:初期座標
        self.sfc=pg.image.load(file)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, float(bairitsu))
        self.rct=self.sfc.get_rect()
        self.rct.center=xy
        self.gy=0

    def blit(self,SCobj):
        SCobj.sfc.blit(self.sfc, self.rct)

    def update(self,SCobj):
        key_states = pg.key.get_pressed()
        if self.rct.bottom >= 600:
            self.rct.bottom = 600
            if key_states[pg.K_SPACE]:
                self.gy = -25
        self.gy += 1
        if self.gy > 15:
            self.gy = 15
        self.rct.y += self.gy
        self.blit(SCobj)


class Trap:
    def __init__(self,file,bairitsu,xy,v): # xy:初期座標
        self.sfc=pg.image.load(file)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, float(bairitsu))
        self.rct=self.sfc.get_rect()
        self.rct.center=xy
        self.vx=-v

    def blit(self,SCobj):
        SCobj.sfc.blit(self.sfc, self.rct)

    def update(self,SCobj):
        self.rct.move_ip(self.vx,0)
        self.blit(SCobj)


def main():
    clock = pg.time.Clock()     
    screen=Screen("逃げろ！こうかとん",(1600, 900),"ex04/bg_sabaku.jpg")
    bird=Bird("ex03/fig/8.png",2.0,(200,600))
    trap=Trap("data\サボテンver01.png",2.0,(1600,600),6) # 速度6

    while True:
        screen.blit()
        bird.update(screen)
        trap.update(screen)

        if trap.rct.x <  -1 * random.randint(100,400): #障害物x座標ランダム-400~-100で
            trap.rct.x = screen.rct.width + trap.rct.width #右端に移動
        for event in pg.event.get(): # イベントキューからキーボードやマウスの動きを取得
            if event.type == pg.QUIT: # 閉じるボタンが押されたら終了
                return 
        if bird.rct.colliderect(trap.rct): # 障害物に触れたら終了
            return 
        
        pg.display.update()
        clock.tick(1000)

  
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()