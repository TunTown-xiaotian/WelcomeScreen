import os
import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.moving_right = False
        self.moving_left = False



        """加载飞船图像并获取外接矩形"""
        image_path = os.path.join("images", "ship.bmp")
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性x中存储一个浮点数
        self.x = float(self.rect.x)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x



    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
