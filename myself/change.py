import pygame, sys

pygame.init()
screen = pygame.display.set_mode([400,600])
screen.fill([0, 0, 0])
ship = pygame.image.load('D:/linshishuju/beijing.jpg')
moon = pygame.image.load('D:/linshishuju/beijing.jpg')
ground = 540

start = 90
clock = pygame.time.Clock()
ship_mass = 5000.0
fuel = 5000.0
velocity = -100.0
gravity = 10
height = 2000
thrust = 0
delta_v = 0
y_pos = 90
held_down = False



class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([30, 10])
        image_surface.fill([128,128,128])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location



def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    delta_t = 1/fps #对应Pygame循环的一帧
    thrust = (500 - myThrottle.rect.centery) * 5.0 #将反推发动机精灵的y坐标转换为推力
    fuel -= thrust /(10 * fps) #根据推力减少燃料
    if fuel < 0: fuel = 0.0
    if fuel < 0.1: thrust = 0.0
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel)) #物理公式
    velocity = velocity + delta_v
    delta_h = velocity * delta_t
    height = height + delta_h
    y_pos = ground - (height * (ground - start) / 2000) - 90 #将高度转换为Pygame的y坐标



def display_stats():
    v_str = "velocity: %i m/s" % velocity
    h_str = "height: %.1f" % height
    t_str = "thrust: %i" % thrust
    a_str = "acceleration: %.1f" % (delta_v * fps)
    f_str = "fuel: %i" % fuel
    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str, 1, (255, 255, 255))
    screen.blit(v_surf, [10, 50])
    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255, 255, 255))
    screen.blit(a_surf, [10, 100])
    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255, 255, 255))
    screen.blit(h_surf, [10, 150])
    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, (255, 255, 255))
    screen.blit(t_surf, [10, 200])
    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255, 255, 255))
    screen.blit(f_surf, [60, 300])



def display_flames():
    flame_size = thrust / 15
    for i in range (2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        pygame.draw.polygon(screen, [255, 109, 14], [(startx, starty),
        (startx + 4, starty + flame_size),
        (startx + 8, starty)], 0)



myThrottle = ThrottleClass([15, 500]) #创建反推发动机对象
running = True
while running:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1: fps = 30
    if height > 0.01:
        calculate_velocity()
        screen.fill([0, 0, 0])
        display_stats()
        pygame.draw.rect(screen, [0, 0, 255], [80, 350, 24, 100], 2)
        fuelbar = 96 * fuel / 5000
        pygame.draw.rect(screen, [0,255,0],
        [84,448-fuelbar,18, fuelbar], 0) #燃料量
        pygame.draw.rect(screen, [255, 0, 0],
        [25, 300, 10, 200],0) #画出反推发动机滑块
        screen.blit(moon, [0, 500, 400, 100]) #画出月球
        pygame.draw.rect(screen, [60, 60, 60],
        [220, 535, 70, 5],0) #着陆点
        screen.blit(myThrottle.image, myThrottle.rect) #画出操纵杆
        display_flames()
        screen.blit(ship, [230, y_pos, 50, 90]) #画出飞船
        instruct1 = "Land softly without running out of fuel"
        instruct2 = "Good landing: < 15m/s Great landing: < 5m/s"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255, 255, 255))
        screen.blit(inst1_surf, [50, 550])
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst1_font.render(instruct2, 1, (255, 255, 255))
        screen.blit(inst2_surf, [20, 575])
        pygame.display.flip()



    else:
        display_final()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                myThrottle.rect.centery = event.pos[1]
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500
    pygame.quit()