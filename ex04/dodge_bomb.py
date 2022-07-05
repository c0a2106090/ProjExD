import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen=pg.display.set_mode((1600,900))
    bg=pg.image.load("C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex04/pg_bg.jpg")
    rect_bg=bg.get_rect()
    clock=pg.time.Clock()
    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()