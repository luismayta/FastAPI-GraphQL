from ariadne import QueryType
from app.config.db import SessionLocal
from app.repository import player_repository

query = QueryType()
session = SessionLocal()


@query.field("players")
def resolve_players(obj, info):
    players = player_repository.get_players(session)
    return players


@query.field("player")
def resolve_player(obj, info, playerId):
    player = player_repository.get_player_by_id(playerId, session)
    return player


@query.field("playerByName")
def resolve_player_by_name(obj, info, playerName):
    player = player_repository.get_player_by_name(playerName, session)
    return player


@query.field("playerByTeam")
def resolve_player_team_name(obj, info, teamName):
    player = player_repository.get_player_by_team(teamName, session)
    return player
