# Generated by Django 3.2.17 on 2023-02-17 11:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import meinberlin.apps.votes.models


class Migration(migrations.Migration):
    dependencies = [
        ("a4modules", "0006_module_blueprint_type"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("meinberlin_votes", "0005_alter_votingtoken_token"),
    ]

    operations = [
        migrations.DeleteModel(
            name="VotingToken",
        ),
        migrations.DeleteModel(
            name="TokenVote",
        ),
        migrations.CreateModel(
            name="TokenPackage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.PositiveIntegerField()),
                ("downloaded", models.BooleanField(default=False)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a4modules.module",
                    ),
                ),
            ],
            options={
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="VotingToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        blank=True,
                        default=meinberlin.apps.votes.models.get_token_16,
                        editable=False,
                        max_length=40,
                    ),
                ),
                (
                    "token_hash",
                    models.CharField(editable=False, max_length=128, unique=True),
                ),
                ("allowed_votes", models.PositiveSmallIntegerField(default=5)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this token should be treated as active. Unselect this instead of deleting tokens.",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a4modules.module",
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meinberlin_votes.tokenpackage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TokenVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, editable=False, null=True, verbose_name="Modified"
                    ),
                ),
                ("object_pk", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "token",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meinberlin_votes.votingtoken",
                    ),
                ),
            ],
            options={
                "unique_together": {("content_type", "object_pk", "token")},
                "index_together": {("content_type", "object_pk")},
            },
        ),
    ]
