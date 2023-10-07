import pytest
from kmp import calcul_carryOver, match, optimize_carryOver

@pytest.mark.parametrize("pattern, string, expected", [
    ("abc", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at abc nulla. Nullam vehicula leo ac abc justo. Fusce abc eget ante aabc velit", True), 
    ("abc", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at nulla. Nullam vehicula leo ac justo. Fusce eget ante velit", False),
    ("Lor", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at abc nulla. Nullam vehicula leo ac abc justo. Fusce abc eget ante aabc velit", True),
    ("xyz", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at abc nulla. Nullam vehicula leo ac abc justo. Fusce abc eget ante aabc velit", False),
    ("ghi", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ghi nulla. Nullam vehicula leo ac ghi justo. Fusce ghi eget ante aabc velit", True),              
])
def test_match(pattern, string, expected):
    l=calcul_carryOver(pattern)
    lps=optimize_carryOver(l,pattern)
    assert match(lps,pattern, string) == expected
