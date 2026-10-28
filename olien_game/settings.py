class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (135,206,235)
        self.ship_speed = 1.5

        #子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,0,60)
        self.bullets_allowed = 5




