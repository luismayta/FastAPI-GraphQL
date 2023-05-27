from app.models.player import Player
from sqlalchemy.orm import Session
from graphql import GraphQLError
from fastapi import status


def delete_player(playerId, db: Session):
    try:
        player = db.query(Player).get(playerId)

        if player is None:
            raise GraphQLError("Player not found in database",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        db.delete(player)
        db.commit()
    except Exception as error:
        raise Exception(f"Error deleting player from database {error}")


def get_player_by_team(teamName, db: Session):
    try:
        player = db.query(Player).order_by(Player.name) \
            .filter(Player.team.ilike(f'%{teamName}%')) \
            .all()

        if not player:
            raise GraphQLError("Player not found in database",
                        extensions={"code": status.HTTP_404_NOT_FOUND})

        return player
    except Exception as error:
        raise Exception(f"Could not find player {error}")


def get_player_by_name(playerName, db: Session):
    try:
        player = db.query(Player) \
            .filter(Player.name.like(f'%{playerName}%')) \
            .all()

        if not player:
            raise GraphQLError("Player not found in database")

        return player
    except GraphQLError as error:
        raise GraphQLError(f"Error occurred in database {error}")


def create_player(player_input, db: Session):
    try:
        # Create instance of player with data
        player = Player(name=player_input.get('name')
                        , number=player_input.get('number')
                        , team=player_input.get('team'))

        # Add player of session and confirm changes on database
        db.add(player)
        db.commit()

        # Return object type Player
        return player
    except Exception as e:
        raise GraphQLError("Could not create player: " + str(e),
                           extensions={"code": status.HTTP_500_INTERNAL_SERVER_ERROR})


def get_players(db: Session):
    try:
        players = db.query(Player).all()

        if not players:
            raise GraphQLError("The database does not contain players",
                               extensions={"code": status.HTTP_404_NOT_FOUND})
        return players
    except Exception as error:
        raise GraphQLError(f"Could not from the database {error}")


def update_players(db: Session, playerId, player_input):
    try:
        player = db.query(Player).get(playerId)

        if not player:
            raise GraphQLError("The database does not contain players",
                               extensions={"code": 404})

        for key, value in player_input.items():
            if hasattr(player, key) and value is not None:
                setattr(player, key, value)

        db.commit()

        return player
    except Exception as error:
        raise Exception(f"Occurred during from database {error}")


def get_player_by_id(playerId, db: Session):
    try:
        player = db.query(Player).get(playerId)

        if not player:
            raise GraphQLError("Player does not exist in database",
                               extensions={"code": status.HTTP_404_NOT_FOUND})
        return player
    except Exception as error:
        raise Exception(f"Occurred when trying to {error}")
