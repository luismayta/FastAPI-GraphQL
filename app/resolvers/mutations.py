from ariadne import MutationType
from app.config.db import SessionLocal
from app.repository import player_repository

session = SessionLocal()

mutation = MutationType()


@mutation.field("createPlayer")
def resolve_create_player(obj, info, player_input):
    player = player_repository.create_player(player_input, session)
    return player


@mutation.field("deletePlayer")
def resolve_delete_player(obj, info, playerId):
    player_repository.delete_player(playerId, session)
    return {"status: Player deleted successfully"}


@mutation.field("updatePlayer")
def resolve_update_player(obj, info, playerId, player_input):
    player = player_repository.update_players(session, playerId, player_input)
    return player


mutation_resolvers = {
    "createPlayer": resolve_create_player,
    "deletePlayer": resolve_delete_player,
    "updatePlayer": resolve_update_player,
}
