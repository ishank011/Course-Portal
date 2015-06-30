# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedCourseList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=150)),
                ('syllabus', models.CharField(max_length=2500)),
                ('credit', models.IntegerField(max_length=2)),
                ('semester', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedCourseTeaching',
            fields=[
                ('application_no', models.AutoField(serialize=False, primary_key=True)),
                ('semester', models.IntegerField(max_length=2)),
                ('course', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('elect_or_comp', models.IntegerField(max_length=1)),
                ('course_code', models.ForeignKey(to='collection.ApprovedCourseList')),
            ],
        ),
        migrations.CreateModel(
            name='dept',
            fields=[
                ('dept_code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('dept_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ForeignCourseList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=10)),
                ('credit', models.IntegerField()),
                ('course', models.ForeignKey(to='collection.ApprovedCourseList')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('prof_id', models.IntegerField(serialize=False, primary_key=True)),
                ('prof_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=3, choices=[(b'P', b'Professor'), (b'ASP', b'Assistant Professor'), (b'APT', b'Associate Professor')])),
                ('dept', models.ForeignKey(to='collection.dept')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programme_code', models.CharField(max_length=5)),
                ('programme_name', models.CharField(max_length=200)),
                ('duration', models.IntegerField(max_length=2)),
                ('branch', models.ForeignKey(to='collection.dept')),
            ],
        ),
        migrations.CreateModel(
            name='ProposedCourseList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=150)),
                ('syllabus', models.CharField(max_length=2500)),
                ('level_0_sign', models.IntegerField(max_length=1)),
                ('level_1_sign', models.IntegerField(max_length=1)),
                ('level_2_sign', models.IntegerField(max_length=1)),
                ('date_proposed', models.DateTimeField(auto_now=True)),
                ('level_0', models.ForeignKey(related_name='pro_level_0_list', blank=True, to='collection.Profile', null=True)),
                ('level_1', models.ForeignKey(related_name='pro_level_1_list', blank=True, to='collection.Profile', null=True)),
                ('level_2', models.ForeignKey(related_name='pro_level_2_list', blank=True, to='collection.Profile', null=True)),
                ('programme', models.ForeignKey(to='collection.programme')),
            ],
        ),
        migrations.CreateModel(
            name='ProposedCourseTeaching',
            fields=[
                ('application_no', models.AutoField(serialize=False, primary_key=True)),
                ('semester', models.IntegerField(max_length=2)),
                ('course', models.CharField(max_length=10)),
                ('level_0_sign', models.IntegerField(max_length=1)),
                ('level_1_sign', models.IntegerField(max_length=1)),
                ('level_2_sign', models.IntegerField(max_length=1)),
                ('course_code', models.ForeignKey(to='collection.ApprovedCourseList')),
                ('level_0', models.ForeignKey(related_name='pro_level_0_teaching', blank=True, to='collection.Profile', null=True)),
                ('level_1', models.ForeignKey(related_name='pro_level_1_teaching', blank=True, to='collection.Profile', null=True)),
                ('level_2', models.ForeignKey(related_name='pro_level_2_teaching', blank=True, to='collection.Profile', null=True)),
                ('prof_id', models.ForeignKey(to='collection.Professor')),
                ('programme', models.ForeignKey(to='collection.programme')),
            ],
        ),
        migrations.AddField(
            model_name='foreigncourselist',
            name='level_0',
            field=models.ForeignKey(related_name='for_level_0_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='foreigncourselist',
            name='level_1',
            field=models.ForeignKey(related_name='for_level_1_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='foreigncourselist',
            name='level_2',
            field=models.ForeignKey(related_name='for_level_2_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='foreigncourselist',
            name='programme',
            field=models.ForeignKey(to='collection.programme'),
        ),
        migrations.AddField(
            model_name='dept',
            name='head',
            field=models.ForeignKey(to='collection.Profile'),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='level_0',
            field=models.ForeignKey(related_name='app_level_0_teaching', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='level_1',
            field=models.ForeignKey(related_name='app_level_1_teaching', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='level_2',
            field=models.ForeignKey(related_name='app_level_2_teaching', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='prof_id1',
            field=models.ForeignKey(to='collection.Professor'),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='prof_id2',
            field=models.ForeignKey(related_name='prof_id2', blank=True, to='collection.Professor', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='prof_id3',
            field=models.ForeignKey(related_name='prof_id3', blank=True, to='collection.Professor', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='prof_id4',
            field=models.ForeignKey(related_name='prof_id4', blank=True, to='collection.Professor', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourseteaching',
            name='programme',
            field=models.ForeignKey(to='collection.programme'),
        ),
        migrations.AddField(
            model_name='approvedcourselist',
            name='level_0',
            field=models.ForeignKey(related_name='app_level_0_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourselist',
            name='level_1',
            field=models.ForeignKey(related_name='app_level_1_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourselist',
            name='level_2',
            field=models.ForeignKey(related_name='app_level_2_list', blank=True, to='collection.Profile', null=True),
        ),
        migrations.AddField(
            model_name='approvedcourselist',
            name='programme',
            field=models.ForeignKey(to='collection.programme'),
        ),
    ]
