from django.db import models
from django_extensions.db.models import TimeStampedModel


class Match(TimeStampedModel):
    WICKET_CHOICES = (
        (1, '0'),
        (2, '1'),
        (3, '2'),
        (4, '3'),
        (5, '4'),
        (6, '5'),
        (7, '6'),
        (8, '7'),
        (9, '8'),
        (10, '9'),
        (11, '10')
    )

    runs_host = models.FloatField(
            help_text='runs',
    )
    wickets_host = models.PositiveSmallIntegerField(
        choices=WICKET_CHOICES,
    )
    runs_guest = models.FloatField(
            help_text='runs',
    )
    wickets_guest = models.PositiveSmallIntegerField(
        choices=WICKET_CHOICES,
    )

    host = models.ForeignKey(
        'league.TeamSeason',
        on_delete=models.PROTECT,
        related_name='+',
    )
    guest = models.ForeignKey(
        'league.TeamSeason',
        on_delete=models.PROTECT,
        related_name='+',
    )
    match_date = models.DateTimeField()


    def __str__(self):
        return f'{self.host} ({self.get_score_display()}) {self.guest}'
