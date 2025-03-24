def validate_move_contract(contract_code: str) -> dict:
    error = []

    if "module" not in contract_code:
        error.append("missing 'module' declaration")

    if "public fun" not in contract_code:
        error.append("no public function found; ensure at least one public function is defined.")

    is_valid = len(error) == 0

    return {"valid": is_valid, "error": error}