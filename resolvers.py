from ariadne import QueryType

query = QueryType()

@query.field("contract")
def resolve_contract(*_, name):
    return {
        "contractName": name,
        "code": "<CODE>",
        "methods": ["transfer", "transfer_from", "balanceOf"],
        "vars": ["balance", "token_supply", "owner"]
    }

