import sys
import re
from kmp import calcul_carryOver, match, optimize_carryOver
import nfa_to_dfa

import regex_to_nfa
from visual_utils import draw_dfa

def is_Regex(input_string):
    # Define a regular expression pattern that matches any of the characters ()|.*
    pattern = r'[()|.*]'
    
    # Use the re.search() function to check if the pattern exists in the input string
    if re.search(pattern, input_string):
        return True
    else:
        return False
    
def grep_string_in_file(pattern: str, file_path):
    try:
        with open(file_path, 'r') as file:
            if is_Regex(pattern):
                print()
                print("*****************************************************")
                print("Generating NFA from the regex...")
                print("*****************************************************")
                nfa = regex_to_nfa.regex_to_nfa(pattern)
                print()
                print("*****************************************************")
                print("Generating DFA from NFA...")
                print("*****************************************************")
                dfa = nfa_to_dfa.nfa_to_dfa(nfa)
                print()
                print("*****************************************************")
                print("Generating the graph...")
                print("*****************************************************")
                draw_dfa(dfa, pattern)
                for line_number, line in enumerate(file, start=1):
                    words = line.split()
                    for word in words: 
                        if nfa_to_dfa.is_accepted_by_dfa(dfa, dfa["initial_state"],word,re.search(re.escape('.'),pattern)):
                            print(f"{file_path}:{line_number}: {line.strip()}")
            else: 
                for line_number, line in enumerate(file, start=1):
                        l=calcul_carryOver(pattern)
                        lps=optimize_carryOver(l,pattern)
                        if match(lps,pattern, line):
                            print(f"{file_path}:{line_number}: {line.strip()}")

    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas été trouvé.")
    #except Exception as e:
        #print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python grep_similaire.py <chaîne> <fichier>")
    else:
        pattern = sys.argv[1]
        file_path = sys.argv[2]
        grep_string_in_file(pattern, file_path)