# Generated by Django 2.0.5 on 2018-06-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20180627_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='Abdomen',
            field=models.CharField(blank=True, default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Abdominalleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Abdominalright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Ankleleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Ankleright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BCleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BCright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BulkLeft12',
            field=models.CharField(blank=True, default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BulkRight12',
            field=models.CharField(blank=True, default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='CVS',
            field=models.CharField(blank=True, default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Cremastricleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Cremastricright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Fingerflexionleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Fingerflexionright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HOffmansLeft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HOffmansRight',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HangGripleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HangGripright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='JPSleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='JPSright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kneeleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kneeright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PlantarLeft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PlantarRight',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='RespiratorySystem',
            field=models.CharField(blank=True, default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Section4Name',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionleft1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abnormalmovementsright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abornmalmovementsleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionleft1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bicepsleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bicepsright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ehlleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ehlright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eversionleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eversionright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft2',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft3',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft4',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright2',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright3',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright4',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='fingerNoseTextleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='fingerNoseTextright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft2',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft3',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft4',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright2',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright3',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright4',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='inversionleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='inversionright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='kneeHelltestleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='kneeHelltestright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbleft1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='othersLeft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='othersRight',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pectoralLeft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pectoralRight',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pendularKneeJerkleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pendularKneeJerkright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rombers',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='supinatorleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='supinatorright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneleft1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tricepsleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tricepsright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkleft1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbleft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbleft1',
            field=models.CharField(blank=True, default='None', max_length=102, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbright',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbright1',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='vibrationLeft',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='vibrationRight',
            field=models.CharField(blank=True, default='None', max_length=120, null=True),
        ),
    ]
