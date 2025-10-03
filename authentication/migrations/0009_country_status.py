from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_city_options_city_id_department_user_id_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
