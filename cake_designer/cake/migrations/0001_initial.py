# Generated by Django 4.2.3 on 2023-07-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('levels_number', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('levels_shape', models.CharField(choices=[('Круг', 'Круг'), ('Квадрат', 'Квадрат'), ('Прямоугольник', 'Прямоугольник')], default='Круг', max_length=30)),
                ('first_tier_basis', models.CharField(choices=[('Ванильный бискват', 'Ванильный бискват'), ('Шоколадный бисквит', 'Шоколадный бисквит'), ('Мраморный бисквит', 'Мраморный бисквит'), ('Медовый бисквит', 'Медовый бисквит')], default='Ванильный бискват', max_length=30)),
                ('second_tier_basis', models.CharField(choices=[('Ванильный бискват', 'Ванильный бискват'), ('Шоколадный бисквит', 'Шоколадный бисквит'), ('Мраморный бисквит', 'Мраморный бисквит'), ('Медовый бисквит', 'Медовый бисквит')], default='Ванильный бисквит', max_length=30)),
                ('third_tier_basis', models.CharField(choices=[('Ванильный бискват', 'Ванильный бискват'), ('Шоколадный бисквит', 'Шоколадный бисквит'), ('Мраморный бисквит', 'Мраморный бисквит'), ('Медовый бисквит', 'Медовый бисквит')], default='Ванильный бисквит', max_length=30)),
                ('buttercream', models.CharField(choices=[('Белый', 'Белый крем'), ('Шоколад', 'Шоколадный крем'), ('Чиз', 'Крем чиз')], default='Белый', max_length=30)),
                ('coating_cream', models.CharField(choices=[('Без крема', 'Без крема'), ('Белый', 'Белый крем'), ('Шоколад', 'Шоколадный крем'), ('Чиз', 'Крем чиз')], default='Без крема', max_length=30)),
                ('toppings', models.CharField(choices=[('Без топпинга', 'Без топпинга'), ('Белый соус', 'Белый соус'), ('Карамелный сироп', 'Карамелный сироп'), ('Кленовый сироп', 'Клетовый сироп'), ('Молочный шоколад', 'Молочный шоколад')], default='Без топпинга', max_length=30)),
                ('berries', models.CharField(choices=[('Без ягод', 'Без ягод'), ('Ежевика', 'Ежевика'), ('Голубика', 'Голубика'), ('Малина', 'Малина'), ('Клубника', 'Клубника')], default='Без ягод', max_length=20)),
                ('decor', models.CharField(choices=[('Без декора', 'Без декора'), ('Безе', 'Безе'), ('Маршмелоу', 'Маршмелоу'), ('Кокосовая стружка', 'Кокосовая стружка'), ('Фигурное печеье', 'Фигурное печеье'), ('Пекан', 'Пекан'), ('Фисташки', 'Фисташки'), ('Фундук', 'Фундук')], default='Без декора', max_length=30)),
                ('cake_writing', models.CharField(blank=True, default='', max_length=250)),
                ('comment', models.TextField()),
            ],
        ),
    ]
