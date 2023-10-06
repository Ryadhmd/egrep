import pytest
from nfa_to_dfa import nfa_to_dfa,is_accepted_by_dfa
from regex_to_nfa import regex_to_nfa


# Define some test cases for is_accepted_by_dfa with different regex and input strings
@pytest.mark.parametrize("regex, input_string, match_all, expected_result", [
    ("a.*b", "acccb", True, True),
    ("a|b", "ab", False, False),      
    ("a(b|c)", "abc", False, False),  
    ("x|y|z*", "xyz", False, False),
    ("x|y|z*","zzzzzzz",False,True),  
    ("fo.b", "foxb", True, True), 
    ("c.*e", "cdfe", True, True),
])
def test_is_accepted_by_dfa(regex, input_string, match_all, expected_result):
    nfa = regex_to_nfa(regex)
    dfa = nfa_to_dfa(nfa)
    initial_state = dfa["initial_state"]
    result = is_accepted_by_dfa(dfa, initial_state, input_string, match_all)
    assert result == expected_result

if __name__ == '__main__':
    pytest.main()

