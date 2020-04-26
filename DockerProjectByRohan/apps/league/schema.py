import graphene
from graphene_django.types import DjangoObjectType
from .models import league
from .models import match
from .models import player
from .models import season
from .models import team



class MessageType(DjangoObjectType):
    class Meta:
        model = league.League

class BessageType(DjangoObjectType):
    class Meta:
        model = match.Match

class QessageType(DjangoObjectType):
    class Meta:
        model = player.Player

class PessageType(DjangoObjectType):
    class Meta:
        model = player.PlayerInTeam

class NessageType(DjangoObjectType):
    class Meta:
        model = season.Season

class LessageType(DjangoObjectType):
    class Meta:
        model = team.Team

class SessageType(DjangoObjectType):
    class Meta:
        model = team.TeamSeason


class Query(graphene.AbstractType):
    all_messages = graphene.List(MessageType)
    all_matches = graphene.List(BessageType)
    all_teams = graphene.List(LessageType)
    all_players = graphene.List(QessageType)
    all_seasons = graphene.List(NessageType)
    all_playersinteam = graphene.List(PessageType)
    all_teamseasons = graphene.List(SessageType)

    def resolve_all_messages(self, args):
        return league.League.objects.all()

    def resolve_all_matches(self, args):
        return match.Match.objects.all()
    
    def resolve_all_teams(self, args):
        return team.Team.objects.all()
    
    def resolve_all_players(self, args):
        return player.Player.objects.all()
    
    def resolve_all_seasons(self, args):
        return season.Season.objects.all()
    
    def resolve_all_playersinteam(self, args):
        return player.PlayerInTeam.objects.all()
    
    def resolve_all_teamseasons(self, args):
        return team.TeamSeason.objects.all()
