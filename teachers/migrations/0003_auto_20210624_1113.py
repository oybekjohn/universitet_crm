# Generated by Django 3.2.4 on 2021-06-24 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0002_auto_20210624_0951"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacherfile",
            name="file",
            field=models.FileField(default=" ", upload_to="file/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="teacherfile",
            name="type",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="type",
                to="teachers.filetype",
            ),
            preserve_default=False,
        ),
    ]
