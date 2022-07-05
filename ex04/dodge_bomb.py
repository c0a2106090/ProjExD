from weakref import ref
import pygame as pg
import sys
import random
       
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen=pg.display.set_mode((1600,900))
    bg=pg.image.load("C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex04/pg_bg.jpg")
    rect_bg=bg.get_rect()
    clock=pg.time.Clock()
    clock.tick(1000)

    tori_img=pg.image.load("C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex03/fig/8.png")
    tori_img=pg.transform.rotozoom(tori_img,0,2.0)
    tori_rect=tori_img.get_rect()
    tori_rect.center=900,400

    x=random.randint(10,1590)
    y=random.randint(10,890)
    bomb_img=pg.Surface((20,20))
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10) #第3引数:surfave内の座標
    bomb_rect=bomb_img.get_rect()
    bomb_rect.center=x,y
    bomb_img.set_colorkey((0,0,0))
    vx,vy=1,1
    reflectx=0
    reflecty=0

    while True:
        screen.blit(bg,rect_bg)
        screen.blit(tori_img,tori_rect)
        screen.blit(bomb_img,bomb_rect)
        pg.display.update() 
        bomb_rect.move_ip(vx,vy)
        if bomb_rect.right>1600 or bomb_rect.left<0:
            reflectx+=1
            vx=napier(reflectx)
        if bomb_rect.top<0 or bomb_rect.bottom>900:
            reflecty+=1
            vy=napier(reflecty)

        for event in pg.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == pg.QUIT:      # 閉じるボタンが押されたら終了
                return

        presskey=pg.key.get_pressed()
        if presskey[pg.K_LEFT] and tori_rect.left>=0:
            tori_rect.move_ip(-1, 0)
        if presskey[pg.K_RIGHT] and tori_rect.right<=1600:
            tori_rect.move_ip(1, 0)
        if presskey[pg.K_UP] and tori_rect.top>=0:
            tori_rect.move_ip(0, -1)
        if presskey[pg.K_DOWN] and tori_rect.bottom<=900:
            tori_rect.move_ip(0, 1)

        if tori_rect.colliderect(bomb_rect)==True:
            return

def napier(x):
    x-int(x)
    if x%2==0:
        y=(1+1/x)**x
    else:
        y=-((1+1/x)**x)
    return y


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()           # Pygameの終了(ないと終われない)
    sys.exit()