# -*- coding: utf-8 -*-

"""
Le language de programmation python compte 33 mots-clés a savoir:

False       as        continue    else        from        in            not           return      yield
None        assert    def         except      global      is            or            try
True        break     del         finally     if          lambda        pass          while
and         class     elif        for         import      nonlocal      raise         with

ces mots sont déjà réservés et nous ne pouvons pas créer de variables ou de fonctions portant qui est le nom d'un mot-clé

Mais également l'identation est très important pour le compilateur python
car celui-ci se sert de cela pour bien éxecuter notre programmme donc lorsque vous codez respecter cette norme.

L'instantation de variable en python se faire au moyen de l'opérateur d'égalié "="
Il existe plusieur type de base en python.
Et chaque type de donnée est considére comme un  type particulier d'objet.
chaque type d'objet possède pas défaut son lot de fonction et de proprièté par défaut
que nous pouvons utilisé.
Voici les types de base natives de python:

bool          Boolean value
int           integer (arbitrary magnitude)
float         floating-point number
list          mutable sequence of objects
tuple         immutable sequence of objects
str           character string
set           unordered set of distinct objects
frozenset     immutable form of set class
dict          associative mapping (aka dictionary)

*immutable ===== non-modifiable
*mutable   ===== modifiable

set, dict et tuple sont immutables.

Lorsque l'on désire appelé une méthode on utilise l'opérateur "."

ex: response.lower().startswith('y') # si nous considérons une variable response de type str

Pour les methodes il en existe deux types : 
    
    -Les accessors( acceseurs ) : Qui permet de récupèré la(les) valeur(s) de(s) instance(s) de notre objet
    -Les mutators( mutateurs ) : Qui permet de modifié la(les) valeur(s) de notre instance d'objet

*bool donc les valeur sont 0 et 1 c'est à dire entre False et True
    NB:  dans d'autres languages on utiliserais 0 et 1 mais pas le cas en python
    Le constructeur par défaut des booeléen est bool()
    ex: bool(response) # return true ou false
        response = True 
    
    
*int Pour reprenseter les nombres sans la partie décimal
    Le constructeur des int est int()
    NB: 0b1011 Pour la répresentation des nombres binaire "0b" == "binaire".
        0o52 Pour la répresentation des nombres octal "0o" == "octal".
        Pour la representation des nombres héxadecimale 0x7f "0x" == "héxadecimale".
        dans une base int(nb, base) #base entre 2 et 16
        par défaut base égale "=" 10
        si nb est un decimal on retourne seulement la partie entière du nombre
        int('137') # retourne 137
        int('Hello') #génère une erreur de type ValueError
        
*float pour les décimaux.
    Le constructeur des float est float()
    float(2) #retourne 2.0
    float('3.15') # génère une erreur de type ValueError

##Types de séquence: les classes list, tuple et str
Ce sont des objets itérable ===> que l'on peux accéder à chaque séquence de la liste indépendemment

*list Pour stocker une séquence d'objet
    Le premier index est 0 et va jusqu'à n-1 (n == longueur de la liste)
    On utilise les '[ ]' pour delimité une liste
    nb = [ 1, 2, 3] ou nb = list(1,2,3) #avec le constructeur
    C'est un objet itérable ===> que l'on peux accéder à chaque séquence de la liste indépendemment
    
*tuple Pareil que pour les liste mais l'on utilise () comme delimiteur et aussi tuple comme constructeur

*str Pour les chaînes de caractères
    Nous pouvons utilisé '' ou "" comme délimiteur, le constructeur str()
    Mais aussi 3*' ou 3*" === ''' ou """ pour les chaînes de caractères multiligne
    """ peut-être utilisé pour faire les commentaire multiligne lorsque que nous l'utilisons pas pour l'affectation
    
*set de Python représente la notion mathématique d'un ensemble, à savoir une collection d'éléments, sans doublons et sans ordre inhérent à ces éléments.
    avec set() ou {} comme délimiteur
    
*frozenset est une forme immuable du type set
    avec frozenset()
    
*dict représente un dictionnaire, ou mappage, à partir d'un ensemble de clés distinctes aux valeurs associées.
    y = {'ga':'Irish','de':'German'}
    pairs = [('ga','Irish'),('de','German')]

################################################################################################""
####Expressions, opérateurs et priorité
###############################################################################################""

*Logique

not               unary negation
and               conditional and
or                conditional or

unary ==== opération sur un seul élément
Il ne faudrais pas que les objet visés soit  de type NoNe

*Egalité

is                      same identity (même type)
is not                  different identity (typr différent)
==                      equivalent
!=                      not equivalent (pas équivalent)


*Comparaison

<                       less than
<=                      less than or equal to
>                       greater than
>=                      greater than or equal to

Une exception est lèvée si les types sont incomparables

*Arithmetique

+                         addition
−                         subtraction
*                         multiplication
/                         true division
//                        integer division
%                         the modulo operator

*Opérateur binaire

∼ complément binaire équivalent a un not pur les binaires (unary operator)
& equivalent à and
| equivalent à or
ˆ equivalent à exclusive-or(XOR ou ou-exclusive)
<< déplacement à gauche, remplace avec les 0
>> déplacement à droite, remplace avec les bits signé

*Sequence Operators
        
        + Pour str, tuple, and list
        
            s[j]                            élément avec l'index j
            [start:stop]                    slice incluant les indices start a stop -1 [start,stop)
            s[start:stop:step]              slice incluant les indices start, start + step, start + 2 step, . . . , pas saut de step jusqu'à stop
            s+t                             Concatenation de sequences
            k*s                             Autre manière de faire s + s + s + ... (k fois)
            val in s                        Vérifie si val est contenu dans s
            val not in s                    Vérifie si val n'est pas contenu dans s

            Nb: Nous pouvons utiliser les indices négatives qui represente la position d'un élément par rapport a l'index de fin.
                del s[j] pour effectuer une suppression de donnée
                les comparaison sont basées sur l'ordre lexicographique
                
            s == t equivalent (element by element)
            s != t not equivalent
            s < t lexicographically less than
            s <= t lexicographically less than or equal to
            s > t lexicographically greater than
            s >= t lexicographically greater than or equal to
        
        + Pour Set and Dictionaires
                key in s containment check
                key not in s non-containment check
                s1 == s2 s1 is equivalent to s2
                s1 != s2 s1 is not equivalent to s2
                s1 <= s2 s1 is subset of s2
                s1 < s2 s1 is proper subset of s2
                s1 >= s2 s1 is superset of s2
                s1 > s2 s1 is proper superset of s2
                s1 | s2 the union of s1 and s2
                s1 & s2 the intersection of s1 and s2
                s1 − s2 the set of elements in s1 but not s2
                s1 ˆ s2 the set of elements in precisely one of s1 or s2
    
                *Operateur supplémentaire
                        d[key] value associated with given key
                        d[key] = value set (or reset) the value associated with given key
                        del d[key] remove key and its associated value from dictionary
                        key in d containment check
                        key not in d non-containment check
                        d1 == d2 d1 is equivalent to d2
                        d1 != d2 d1 is not equivalent to d2
                        
*Priorité des opérateurs
        Type                                            Symbols
1       member                                          access expr.member
2       function/method calls                           expr(...)
        container subscripts/slices expr[...]
3       exponentiation                                  **
4       unary operators                                 +expr, −expr, ˜expr
5       multiplication, division                        *, /, //, %
6       addition, subtraction                           +, −
7       bitwise shifting                                <<, >>
8       bitwise-and                                     &
9       bitwise-xor                                     ˆ
10      bitwise-or                                      |
11      comparisons                                     is, is not, ==, !=, <, <=, >, >=
        containment                                     in, not in
12      logical-not                                     not expr
13      logical-and                                     and
14      logical-or                                      or
15      conditional                                     val1 if cond else val2
16      assignments                                      =, +=, −=, =, etc.

"""
