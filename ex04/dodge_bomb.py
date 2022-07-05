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

    make_bomb()
    vx,vy=1,1


    while True:
        screen.blit(bg,rect_bg)
        screen.blit(tori_img,tori_rect)
        screen.blit(bomb_img,bomb_rect)
        pg.display.update() 
        bomb_rect.move_ip(vx,vy)
        if bomb_rect.right>1600 or bomb_rect.left<0:
            vx*=-1
        if bomb_rect.top<0 or bomb_rect.bottom>900:
            vy*=-1

        for event in pg.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == pg.QUIT:      # 閉じるボタンが押されたら終了
                return

        presskey=pg.key.get_pressed()
        if presskey[pg.K_LEFT]:
            tori_rect.move_ip(-1, 0)
        if presskey[pg.K_RIGHT]:
            tori_rect.move_ip(1, 0)
        if presskey[pg.K_UP]:
            tori_rect.move_ip(0, -1)
        if presskey[pg.K_DOWN]:
            tori_rect.move_ip(0, 1)
        
        if tori_rect.colliderect(bomb_rect)==True:
            return

def make_bomb():
    global bomb_rect,bomb_img
    x=random.randint(10,1590)
    y=random.randint(10,890)
    bomb_img=pg.Surface((20,20))
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10) #第3引数:surfave内の座標
    bomb_rect=bomb_img.get_rect()
    bomb_rect.center=x,y
    bomb_img.set_colorkey((0,0,0))


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()           # Pygameの終了(ないと終われない)
    sys.exit()