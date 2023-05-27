from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
import uvicorn

# Import resolvers and schema GraphQL denifed
from app.resolvers.queries import resolve_players, resolve_player, resolve_player_by_name, resolve_player_team_name
from app.resolvers.mutations import resolve_create_player, resolve_delete_player, resolve_update_player
from app.schema.types import type_defs

# Create object QueryType and register resolvers
query = QueryType()
mutation = MutationType()


query.set_field("players", resolve_players)
query.set_field("player", resolve_player)
query.set_field("playerByName", resolve_player_by_name)
query.set_field("playerByTeam", resolve_player_team_name)

mutation.set_field("createPlayer", resolve_create_player)
mutation.set_field("deletePlayer", resolve_delete_player)
mutation.set_field("updatePlayer", resolve_update_player)

# Create execute schema
schema = make_executable_schema(type_defs, query, mutation)

# Create instance of GraphQL
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    # Run server HTTP uvicorn
    uvicorn.run(app, port=8000)
