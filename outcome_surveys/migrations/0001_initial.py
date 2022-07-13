# Generated by Django 3.2.14 on 2022-07-07 13:33

import django.utils.timezone
import jsonfield.fields
import model_utils.fields
import opaque_keys.edx.django.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearnerCourseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user_id', models.IntegerField()),
                ('course_id', opaque_keys.edx.django.models.CourseKeyField(max_length=255)),
                ('data', jsonfield.fields.JSONField()),
                ('follow_up_date', models.DateField()),
                ('event_type', models.CharField(choices=[('edx.course.learner.passed.first_time', 'edx.course.learner.passed.first_time')], default='edx.course.learner.passed.first_time', max_length=255)),
            ],
        ),
        migrations.AddIndex(
            model_name='learnercourseevent',
            index=models.Index(fields=['follow_up_date'], name='outcome_sur_follow__a60cf0_idx'),
        ),
        migrations.AddIndex(
            model_name='learnercourseevent',
            index=models.Index(fields=['created'], name='outcome_sur_created_80c513_idx'),
        ),
    ]
