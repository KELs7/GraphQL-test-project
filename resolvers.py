def resolve_contract(_, info):
    return {
        "code": "<CODE>",
        "methods": ["transfer", "transfer_from", "balanceOf"],
        "vars": ["balance", "token_supply", "owner"]
    }