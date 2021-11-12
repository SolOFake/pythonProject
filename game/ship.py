import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen

        # self.settings = ai_game.settings # какой то вахуй

        # Это позволяет разместить корабль в нужной позиции экрана.
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        # Меняет размер изображения.
        self.image = pygame.transform.scale(self.image, (60, 60))
        # Это дял позиционирования корабля.
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана по центру.
        self.rect.midbottom = self.screen_rect.midbottom
        # Позволяет сохранять вещественные координаты центра корабля. Можно нырнуть в 'x' и все поймешь.
        self.x = float(self.rect.x)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

        # Скорость перемещения
        self.ship_speed = 1.5

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут x, не rect.

        # Думает что корабль еще не достиг края и из за это го не вылазит за пределы
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
