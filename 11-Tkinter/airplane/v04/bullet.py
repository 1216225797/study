'''
    子弹类
'''
from airplanewar import AirplaneWar
from readconfig import myconfig
import tkinter

class Bullet(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height, x_dir, y_dir):
        super().__init__(canvas,x,y,position,tag,width,height)
        # 移动速度
        self.step = [myconfig.bullet_x_step,myconfig.bullet_y_step]
        # 移动方向
        self.x_dir = x_dir
        self.y_dir = y_dir
        # 实例化图片
        self.bullet_img_path = myconfig.bullet_img_path
        self.bullet_img = tkinter.PhotoImage(file=self.bullet_img_path)


    def move(self):
        x = self.step[0] * self.x_dir
        y = self.step[1] * self.y_dir
        # print(x,y)
        # 调用父类移动方法
        # print(self.tag)
        self.enemy_move(self.tag,x,y)
