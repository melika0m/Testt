# Generated by Django 5.0.3 on 2024-05-10 12:08

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeUniv',
            fields=[
                ('id_annee_univ', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('annee_univ', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_departement', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom_departement', models.CharField(max_length=40)),
                ('responsable_departement', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id_niveau', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('niveau', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AgentDeScolarite',
            fields=[
                ('id_agent_scolarite', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('numero_telephone', models.IntegerField()),
                ('poste_agent_scolarite', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutorisationDeReclamation',
            fields=[
                ('id_autorisation', models.AutoField(primary_key=True, serialize=False)),
                ('date_expiration', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_autorisation', models.DateTimeField(default=django.utils.timezone.now)),
                ('Etat', models.CharField(choices=[('OU', 'Ouvert'), ('FE', 'Fermé'), ('EX', 'Expiré')], default='OU', max_length=2)),
                ('AgentDeScolarite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.agentdescolarite')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('idF', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40)),
                ('date_creation', models.DateField()),
                ('domain', models.CharField(max_length=40)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('matricule', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('nni', models.BigIntegerField(blank=True, default=0)),
                ('sexe', models.CharField(max_length=4)),
                ('numero_telephone', models.BigIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('filiere', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='etudiant.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=30)),
                ('credit', models.IntegerField()),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id_inscription', models.AutoField(primary_key=True, serialize=False)),
                ('date_inscription', models.DateTimeField()),
                ('annee_univ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.anneeuniv')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.etudiant')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id_reclamation', models.AutoField(primary_key=True, serialize=False)),
                ('contenu', models.TextField()),
                ('preuve_reclamation', models.FileField(null=True, upload_to='documents/reclamations/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])),
                ('status', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30, null=True)),
                ('date_reclamation', models.DateField()),
                ('Matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.matiere')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('contenu', models.TextField()),
                ('date_notification', models.DateField()),
                ('delai', models.IntegerField()),
                ('agent_scolarite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.agentdescolarite')),
                ('reclamation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.reclamation')),
            ],
        ),
        migrations.CreateModel(
            name='ResultatParMatiere',
            fields=[
                ('id_res_element', models.AutoField(primary_key=True, serialize=False)),
                ('note_cc', models.FloatField()),
                ('note_ex', models.FloatField()),
                ('note_finale', models.FloatField()),
                ('note_rattrapage', models.FloatField()),
                ('validation', models.CharField(max_length=40)),
                ('annee_universitaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.anneeuniv')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id_semestre', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Semestre', models.CharField(max_length=25)),
                ('niveau_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='ResultatParMoyenGeneral',
            fields=[
                ('id_res_par_moy_g', models.AutoField(primary_key=True, serialize=False)),
                ('id_annee_diplome', models.CharField(max_length=40)),
                ('moy_g', models.FloatField()),
                ('annee_univ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.anneeuniv')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.etudiant')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='Semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiant.semestre'),
        ),
    ]
