# tests/test_validation.py

from src.validation import validate_move_contract

def test_valid_contract():
    # A minimal valid contract example
    contract_code = """
    module TestModule {
        public fun test_function() {}
    }
    """
    result = validate_move_contract(contract_code)
    assert result["valid"] is True
    assert result["errors"] == []

def test_invalid_contract():
    # An invalid contract missing the module declaration
    contract_code = "public fun test_function() {}"
    result = validate_move_contract(contract_code)
    assert result["valid"] is False
    assert "Missing 'module' declaration." in result["errors"]