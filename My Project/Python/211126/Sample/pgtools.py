import pygame as pg
from random import randint


def randomRGB():
    r, g, b = 0, 0, 0
    while r + g + b < 384:
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return (r, g, b)


class Ball(pg.sprite.Sprite):
    def __init__(self, surface, radius, x_start, y_start, vx_start, vy_start, color=None):
        super().__init__()
        self.maxh, self.maxw = surface.get_height(), surface.get_width()
        self.image = pg.Surface((radius * 2, radius * 2))
        self.image.set_colorkey((0, 0, 0))
        self.color = color or randomRGB()
        pg.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (x_start, y_start)
        self.vx, self.vy = vx_start, vy_start
        self.vx_start, self.vy_start = vx_start, vy_start
        self.radius = radius
        self.iscollided = False

    def update(self):
        self.rect.move_ip(self.vx, self.vy)

    def start(self):
        self.vx, self.vy = self.vx_start, self.vy_start

    def stop(self):
        self.vx, self.vy = 0, 0

    def inelasticCollide(self, group, x=True, y=True, collide=pg.sprite.collide_rect, kill=False, default=True):
        if not default:
            default = not self.iscollided
        result = pg.sprite.spritecollide(self, group, kill, collide)
        if result and default:
            self.iscollided = True
            if x:
                self.vx *= -1
            if y:
                self.vy *= -1
        return result

    # ball should exchange their valocity
    def elasticCollide(self, target, default=True):
        if not default:
            default = not self.iscollided
        result = pg.sprite.collide_circle(self, target)
        if result and default:
            x1, y1 = self.rect.center
            x2, y2 = target.rect.center
            rvx, rvy = target.vx - self.vx, target.vy - self.vy
            value = 10000
            c0 = (self.radius + target.radius) ** 2
            xr, yr = 0, 0
            for i in range(5):
                x, y = x2 - x1 - i * rvx / 5, y2 - y1 - i * rvy / 5
                temp = abs(x ** 2 + y ** 2 - c0)
                if temp < value:
                    value = temp
                    xr, yr = x, y
            nv = pg.math.Vector2(xr, yr)
            # nv = pg.math.Vector2(x2 - x1, y2 - y1) just for simple
            v = pg.math.Vector2(self.vx, self.vy).reflect(nv)
            self.vx, self.vy = v.x, v.y
        return result

    def specialCollide(self, target, x=True, y=True, sensitivity=5, default=True):
        if not default:
            default = not self.iscollided
        result = pg.sprite.collide_rect(self, target)
        if result and default:
            self.iscollided = True
            if x:
                self.vx *= -1
                ratio = (self.rect.centery - target.rect.centery) / (target.rect.height / 2)
                self.vy = sensitivity * ratio
            if y:
                self.vy *= -1
                ratio = (self.rect.centerx - target.rect.centerx) / (target.rect.width / 2)
                self.vx = sensitivity * ratio
        return result

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Bat(pg.sprite.Sprite):
    def __init__(self, surface, width, height, x_start, y_start, color=None):
        super().__init__()
        self.maxh, self.maxw = surface.get_height(), surface.get_width()
        self.image = pg.Surface((width, height))
        self.color = color or randomRGB()
        pg.draw.rect(self.image, self.color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x_start, y_start)
        self.k_up, self.k_down = pg.K_UP, pg.K_DOWN
        self.k_left, self.k_right = pg.K_LEFT, pg.K_RIGHT

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 0:
            if self.k_up != None and pressed_keys[self.k_up]:
                self.rect.move_ip(0, -20)
        if self.rect.bottom < self.maxh:
            if self.k_down != None and pressed_keys[self.k_down]:
                self.rect.move_ip(0, 20)
        if self.rect.left > 0:
            if self.k_left != None and pressed_keys[self.k_left]:
                self.rect.move_ip(-20, 0)
        if self.rect.right < self.maxw:
            if self.k_right != None and pressed_keys[self.k_right]:
                self.rect.move_ip(20, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class EndLine(pg.sprite.Sprite):
    def __init__(self, surface, direction, pos, color=None):
        super().__init__()
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        if direction == "vertical":
            self.image = pg.Surface((1, self.maxh))
            self.rect = self.image.get_rect()
            self.rect.top, self.rect.left = 0, pos
        elif direction == "horizontal":
            self.image = pg.Surface((self.maxw, 1))
            self.rect = self.image.get_rect()
            self.rect.top, self.rect.left = pos, 0
        self.image.fill(color or (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
