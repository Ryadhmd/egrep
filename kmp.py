
# Calcul du Carry Over
def calcul_carryOver(pattern):
    letter = [x for x in pattern]
    cpt = 0
    prefix = [letter[0]]
    lps = [-1,0]
    
    for l in range(len(letter)-1) :
        if letter[l+1] == prefix[cpt] :
           
            cpt = cpt + 1
            prefix.append(letter[cpt])
            lps.append(cpt)
        else :
            if letter[l+1] == prefix[0] :
                cpt = 1
            else :
                cpt = 0
            lps.append(cpt)
           
    return lps

# check if a string contains the pattern 

def match(lps,pattern,string):

    letter = [x for x in string]
    j=0
    idx =0 

    while (j < len(pattern) and idx < len(string)):
        #print(j)
        if pattern[j] != string[idx] and j==0 :
            idx=idx+1

        elif pattern[j] != string[idx] and j!=0:
            j=pattern.index(pattern[lps[j]])

        elif pattern[j] == string[idx]:
            j=j+1
            idx=idx+1 
        

    #print("index:"+str(idx))
    #if idx >= len(string) and j != len(pattern):
        #print("Pas trouve :'(")
    if j == len(pattern): 
        return True 
    return False


# Optimisation du Carry Over
def optimize_carryOver(lps,pattern) :
    for i in range(len(lps)-1) :
        if pattern[i] == pattern[lps[i]] and lps[lps[i]] == -1 :
            lps[i] = -1
        elif pattern[i] == pattern[lps[i]] and lps[lps[i]] != -1 :
            lps[i] = lps[lps[i]]
    return lps

def main():
    with open('41011-0.txt', 'r') as fichier:
    # Itérez à travers chaque ligne du fichier
        for ligne in fichier:
        # La variable 'ligne' contient la ligne courante du fichier
        # Vous pouvez traiter cette ligne comme une chaîne de caractères
        # Cette ligne affiche la ligne sans ajouter de saut de ligne
            l=calcul_carryOver("Chihuahua")
            lps=optimize_carryOver(l,"Chihuahua")
            if match(lps,"Chihuahua", ligne):
                print(ligne)


if __name__ == "__main__":
    main()