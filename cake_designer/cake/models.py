import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3

    LEVELS_NUMBER_CHOICES = [
        (ONE, 1),
        (TWO, 2),
        (THREE, 3)
    ]

    CIRCLE = "Круг"
    SQUARE = "Квадрат"
    RECTANGLE = "Прямоугольник"

    LEVELS_SHAPE_CHOICES = [
        (CIRCLE, "Круг"),
        (SQUARE, "Квадрат"),
        (RECTANGLE, "Прямоугольник")
    ]

    VANILLA_BISCUIT = "Ванильный бискват"
    CHOCOLATE_BISCUIT = "Шоколадный бисквит"
    MARBLE_BISCUIT = "Мраморный бисквит"
    HONEY_BISCUIT = "Медовый бисквит"
    WITHOUT_BICUIT = "Без уровня"

    TIER_BASIS_CHOICES = [
        (WITHOUT_BICUIT, "Без уровня"),
        (VANILLA_BISCUIT, "Ванильный бискват"),
        (CHOCOLATE_BISCUIT, "Шоколадный бисквит"),
        (MARBLE_BISCUIT, "Мраморный бисквит"),
        (HONEY_BISCUIT, "Медовый бисквит"),
    ]

    WHITE_CREAM = "Белый"
    CHOCOLATE_CREAM = "Шоколад"
    CHEESE_CREAM = "Чиз"
    WITHOUT_CREME = "Без крема"

    BUTTERCREAM_CHOICES = [
        (WHITE_CREAM, "Белый крем"),
        (CHOCOLATE_CREAM, "Шоколадный крем"),
        (CHEESE_CREAM, "Крем чиз"),
    ]

    COATING_CREAM_CHOICES = [
        (WITHOUT_CREME, "Без крема"),
        (WHITE_CREAM, "Белый крем"),
        (CHOCOLATE_CREAM, "Шоколадный крем"),
        (CHEESE_CREAM, "Крем чиз"),
    ]

    WITHOUT_TOPPING = "Без топпинга"
    WHITE_SOUCE = "Белый соус"
    CARAMEL_SYRUP = "Карамелный сироп"
    MAPLE_SYRUP = "Кленовый сироп"
    MILK_CHOCOLATE = "Молочный шоколад"

    TOPPINGS_CHOICES = [
        (WITHOUT_TOPPING, "Без топпинга"),
        (WHITE_SOUCE, "Белый соус"),
        (CARAMEL_SYRUP, "Карамелный сироп"),
        (MAPLE_SYRUP, "Клетовый сироп"),
        (MILK_CHOCOLATE, "Молочный шоколад")
    ]

    WITHOUT_BERRIES = "Без ягод"
    BLACKBERRIES = "Ежевика"
    BLUEBERRIES = "Голубика"
    RASPBERRIES = "Малина"
    STRAWBERRIES = "Клубника"

    BERRIES_CHOICES = [
        (WITHOUT_BERRIES, "Без ягод"),
        (BLACKBERRIES, "Ежевика"),
        (BLUEBERRIES, "Голубика"),
        (RASPBERRIES, "Малина"),
        (STRAWBERRIES, "Клубника"),
    ]

    WITHOUT_DECOR = "Без декора"
    BEZE = "Безе"
    MARSMELO = "Маршмелоу"
    COCONUT = "Кокосовая стружка"
    SHAPED_COOKIES = "Фигурное печеье"
    PECAN = "Пекан"
    FISTACHIOS = "Фисташки"
    FOUNDUCK = "Фундук"

    DECOR_CHOICES = [
        (WITHOUT_DECOR, "Без декора"),
        (BEZE, "Безе"),
        (MARSMELO, "Маршмелоу"),
        (COCONUT, "Кокосовая стружка"),
        (SHAPED_COOKIES, "Фигурное печеье"),
        (PECAN, "Пекан"),
        (FISTACHIOS, "Фисташки"),
        (FOUNDUCK, "Фундук"),
    ]

    name = models.CharField(
        max_length=30,
        verbose_name="Имя клиента"
        )
    phone = models.CharField(
        max_length=30,
        verbose_name="Номер клиента"
        )
    levels_number = models.IntegerField(
        choices=LEVELS_NUMBER_CHOICES,
        default=ONE,
        verbose_name="Количество уровней"
        )
    levels_shape = models.CharField(
        max_length=30,
        choices=LEVELS_SHAPE_CHOICES,
        default=CIRCLE,
        verbose_name="Форма уровней"
        )
    first_tier_basis = models.CharField(
        max_length=30,
        choices=TIER_BASIS_CHOICES,
        default=VANILLA_BISCUIT,
        verbose_name="Основа для 1 уровня"
        )
    second_tier_basis = models.CharField(
        max_length=30,
        choices=TIER_BASIS_CHOICES,
        default=WITHOUT_BICUIT,
        verbose_name="Основа для 2 уровня"
        )
    third_tier_basis = models.CharField(
        max_length=30,
        choices=TIER_BASIS_CHOICES,
        default=WITHOUT_BICUIT,
        verbose_name="Основа для 3 уровня"
        )
    buttercream = models.CharField(
        max_length=30,
        choices=BUTTERCREAM_CHOICES,
        default=WHITE_CREAM,
        verbose_name="Крем для начинки"
    )
    coating_cream = models.CharField(
        max_length=30,
        choices=COATING_CREAM_CHOICES,
        default=WITHOUT_CREME,
        verbose_name="Крем для покрытия"
    )
    toppings = models.CharField(
        max_length=30,
        choices=TOPPINGS_CHOICES,
        default=WITHOUT_TOPPING,
        verbose_name="Топпинги"
    )
    berries = models.CharField(
        max_length=20,
        choices=BERRIES_CHOICES,
        default=WITHOUT_BERRIES,
        verbose_name="Ягоды"
    )
    decor = models.CharField(
        max_length=30,
        choices=DECOR_CHOICES,
        default=WITHOUT_DECOR,
        verbose_name="Декор"
    )
    cake_writing = models.CharField(
        max_length=250,
        default="",
        blank=True,
        verbose_name="Надпись на торте"
        )
    comment = models.TextField(
        verbose_name="Комментарий к заказу"
    )
    delivery_date = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False,
        default=timezone.now,
        verbose_name="Дата доставки"
        )
    delivery_address = models.CharField(
        max_length=250,
        blank=False, 
        default="",
        verbose_name="Адрес доставки"
        )
    
    def get_price(self):
        price = self.levels_number * 200

    
    def __str__(self):
        return f"Заказ {self.name}, {self.delivery_address}"
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    
