# Egrep

Ce script Python permet de rechercher une chaîne de caractères (y compris les expressions régulières) dans un fichier texte. Il propose également une option pour générer un graphe représentant un automate fini déterministe (DFA) correspondant à une expression régulière donnée.

## Comment ça marche

Le script utilise plusieurs modules Python pour effectuer les opérations suivantes :

1. **Recherche de motifs (Patterns)** : Le script utilise le module `re` pour vérifier si la chaîne de recherche contient des caractères spéciaux tels que `()|.*`, ce qui indiquerait une expression régulière.

2. **Conversion Regex en NFA (Non-deterministic Finite Automaton)** : Si le motif est une expression régulière, le script utilise le module `regex_to_nfa` pour convertir l'expression en un NFA.

3. **Conversion NFA en DFA (Deterministic Finite Automaton)** : Ensuite, il convertit le NFA en DFA en utilisant le module `nfa_to_dfa`.

4. **Recherche et Affichage** : Le script ouvre le fichier spécifié et parcourt chaque ligne. Pour chaque ligne, il recherche si le mot correspondant au motif est accepté par le DFA. Si c'est le cas, il affiche la ligne correspondante.

5. **Option de Graphe** : Si l'option `--graph` est activée, le script génère un graphe du DFA correspondant à l'expression régulière.

6. **Cas d'un motif qui n'est pas une expression régulière** : Dans le cas où la chaine à recherche n'est pas une RegEx alors le programme utilise l'algorithme de `Knuth-Morris-Pratt` pour déterminer si les lignes
du fichier contiennent le motif recherché.

## Comment l'utiliser

1. Assurez-vous d'avoir Python installé sur votre système.

2. Clonez ce repository :
```shell
   git clone https://github.com/Ryadhmd/egrep.git
   cd egrep/
```

3. Installez les dépendances du projet:
   ```shell
   pip3 install -r requirements.txt

4. Installez le package graphviz :
   ```shell
   sudo apt install graphviz
   
5. Utilisez le script en exécutant la commande suivante depuis le terminal :

   ```shell
   python grep.py [motif] [chemin_du_fichier] [--graph]

6. Si vous voulez executer les tests :
   ```shell
   cd tests/
   pytest 
