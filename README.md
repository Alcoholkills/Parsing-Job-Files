# Job_Req-Parser

Job_Req-Parser permet de parser un document .csv et d'automatiquement charger les informations de `DescriptionPost` et `DescriptionProfil` associées à chaque `id`

1. [Lancement du code](#lancement-du-code)
2. [Lancement de l'environement virtuel](#lancement-de-l'environement-virtuel)
3. [Quelques informations supplémentaires](#quelques-informations-supplémentaires)
4. [Pydoc documentation](#pydoc-documentation)

## Lancement du code

Aucune dépendence n'est nécessaire pour lancer le code.
Il faut avoir python3 installé sur la machine.
Ce code a été testé sur Python 3.9.9.
Dans un terminal, taper, après le lancement de l'environement virtuel :
`python Job_Req-Parser.py`

### Lancement de l'environement virtuel

Dans un terminal, dans le dossier où est situé `Job_Req-Parser.py`, taper :
`python -m venv venv` pour initialiser l'environement virtuel
`./venv/Scripts/activate` pour lancer l'environement virtuel
`deactivate` pour le désactiver

## Quelques informations supplémentaires

`bodge.py` a été utilisé lorsque j'ai rencontré une erreur pendant le "parsing" du fichier, et qu'il était plus rapide de le faire à la main plutôt que de corriger cette errur.
Dans ce cas là, j'ai séparé le fichier initial en 3 fichiers :

- la ligne bloquante + toutes les informations de l'id correspondant
- toutes les lignes avant l'id bloquant
- toutes les lignes apres l'id bloquant

## Pydoc documentation
```
Help on Job_Req-Parser:

NAME
    Job_Req-Parser

FUNCTIONS
    clear_files()
        Permet de nettoyer le dossier en cours
    
    get_file_path()
        Permet d'ouvrir une fenÛtre d'explorateur de fichier et de charger un fichier csv dans le programme.
        Termine le programme si aucun fichier n'est chargÚe.
    
    list_04a5489ea4f0(string)
        Fonction qui a l'air compliquÚe mais en fait pas vraiment.
        Transforme toutes les virgules en un string unique, ce qui permet de bien sÚparer chaque item du csv.
        `lever` permet de ne pas prendre en compte les virgules dans les strings du document qui ne sont pas des sÚparateurs.
    
    loop_file()
        Permet de parcourir tout le fichier chargÚ.
        Regarder le code source pour voir des commentaires plus prÚcis.
    
    main()
        Assure le bon dÚroulement du code
        Utiliser `h` pour affichier l'aide.
```


