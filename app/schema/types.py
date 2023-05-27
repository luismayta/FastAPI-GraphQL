from ariadne import gql

type_defs = gql("""
    type Player {
        id: Int
        name: String
        number: Int
        team: String
    }
    
    input PlayerInput {
        name: String
        number: Int
        team: String
    }
    
    type Query {
        players: [Player]
        player(playerId: ID!) : Player
        playerByName(playerName: String) : [Player]
        playerByTeam(teamName: String) : [Player]
    }
    
    
    type Mutation {
        createPlayer(player_input: PlayerInput): Player
        deletePlayer(playerId: Int): String
        updatePlayer(playerId: ID!, player_input: PlayerInput): Player
    }""")


