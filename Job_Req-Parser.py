from tkinter import filedialog
import re, tkinter, os, sys, traceback

def get_file_path():
    """
    Permet d'ouvrir une fenêtre d'explorateur de fichier et de charger un fichier csv dans le programme.
    Termine le programme si aucun fichier n'est chargée.
    """
    tkinter.Tk().withdraw()
    file = filedialog.askopenfile(initialdir=os.getcwd(), filetypes=[("Csv files", ".csv")])
    if file:
        return file
    else:
        raise KeyboardInterrupt

def list_04a5489ea4f0(string):
    """
    Fonction qui a l'air compliquée mais en fait pas vraiment.
    Transforme toutes les virgules en un string unique, ce qui permet de bien séparer chaque item du csv.
    `lever` permet de ne pas prendre en compte les virgules dans les strings du document qui ne sont pas des séparateurs.
    """
    string_list = [x for x in string]
    lever = True
    for i in range(len(string_list)):
        if string_list[i] == '"':
            lever = not lever
        if string_list[i] == "," and lever:
            string_list[i] = "04a5489ea4f0"
    return "".join(string_list).split("04a5489ea4f0")

def loop_file():
    """
    Permet de parcourir tout le fichier chargé.
    Regarder le code source pour voir des commentaires plus précis.
    """
    try:
        # testing_purpose = 0
        """
        Récupération du fichier sur lequel on va travailler.
        """
        f = get_file_path()

        """
        Initialisation et déclaration des variables.
        `regex_expression` va être utilisé pour déterminer si la ligne courant est une nouvelle entrée ou pas.
            On va donc chercher si la ligne commence par un id, i.e. une suite de chiffre.
        """
        line = "Wazaabii"
        regex_expression = r"^[0-9]+"
        current_data = list()
        current_id = ""
        header = ""
        secondary_lever = True
        lever_no_post = True
        lever_no_profile = True
        lever_no_br = True
        # Find header
        """
        Charge le header dans une variable.
        """
        with open("metadata_Job.csv", "r") as other_file:
            header = other_file.readline()
        working_header = list_04a5489ea4f0(header)
        """
        Commence a lire le fichier, ligne par ligne.
        """
        while True:
            # # *** Testing purpose ***
            # if testing_purpose > 50:
            #     raise KeyboardInterrupt
            # testing_purpose += 1
            # # *** --------------- ***

            line = f.readline()
            if not line:
                break
            # Skip Header
            """
            Saute la ligne si cette ligne est une ligne de type 'header'.
            """
            if re.compile("^Id,Id").match(line) != None:
                continue
            
            """
            Charge la ligne pour effectuer des traitements.
            """
            test_regex = re.compile(regex_expression).match(line)

            # Find first id
            """
            Permet de charger le premier id et de charger les données associées.
            (Initialisation du reste des variables)
            Ce test ne peut être effectué qu'une seule fois : `secondary_lever` est mit a `False` et n'est pas changé par la suite
            """
            if secondary_lever and test_regex != None:
                current_id = re.compile(regex_expression).findall(line)[0]
                current_data.append(line)
                secondary_lever = False
                continue

            # Check if line is new entry
            # test_regex = re.compile(regex_expression).match(line)
            # It is a new entry
            """
            Permet de savoir si la ligne courante correspond a un nouvel id.
            Si oui, alors on va charger toutes les informations précédement collectées dans un fichier, et recharger les variables avec les nouvelles informations.
            """
            if test_regex != None:
                """
                Shenanigan pour récupérer les informations `DescriptionPost` et `DescriptionProfil`
                """
                working_list = list_04a5489ea4f0("".join(current_data))
                my_dict = dict(zip(working_header, working_list))
                # Join the list and get only the Post and Profil
                description_post = my_dict["DescriptionPost"]
                description_profile = my_dict["DescriptionProfil"]
                """
                Shenanigan pour enlever les `"` (guillemets) s'ils existent.
                """
                try:
                    if description_post[0] == '"':
                        description_post = description_post[1:]
                except IndexError:
                    pass
                try:
                    if description_post[-1] == '"':
                        description_post = description_post[:-1]
                except IndexError:
                    pass
                """
                Voir 'Note 1' ci-dessous
                """
                if len(description_post.replace(" ","")) == 0:
                    lever_no_post = False
                    lever_no_br = False
                try:
                    if description_profile[0] == '"':
                        description_profile = description_profile[1:]
                except IndexError:
                    pass
                try:
                    if description_profile[-1] == '"':
                        description_profile = description_profile[:-1] 
                except IndexError:
                    pass
                """
                Note 1
                Ce morceau de code permet de savoir si on a :
                une DescriptionPost ET une DescriptionProfil, -> présence du `<br>`
                une DescriptionPost ET PAS de DescriptionProfil,
                PAS de DescriptionPost ET une DescriptionProfil,
                et de mettre ou pas le `<br>`

                Si aucune information de `DescriptionPost` et `DescriptionProfil` n'est récupérée, alors le fichier n'est pas crée
                """
                if len(description_profile.replace(" ","")) == 0:
                    lever_no_profile = False
                    lever_no_br = False
                if lever_no_profile or lever_no_post:
                    with open(f"ClobFiles\\{current_id}.txt", "w") as new_id_file:
                        if lever_no_post:
                            new_id_file.write(description_post)
                        if lever_no_br:
                            new_id_file.write("\n<br>\n")
                        if lever_no_profile:
                            new_id_file.write(description_profile)
                # Reset values
                """
                Rétablit les variables avec les valeurs de la ligne courante / par défaut
                """
                current_id = re.compile(regex_expression).findall(line)[0]
                current_data = list()
                lever_no_post = True
                lever_no_profile = True
                lever_no_br = True
            # It's not a new entry
            """
            Charge les informations de la ligne courante
            """
            current_data.append(line)
        f.close()
        """
        Gestion des erreur
        """
    except UnicodeDecodeError:
        print(line)
        f.close()
        print("Unexpected error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_exc())
    except:
        f.close()
        print("Unexpected error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_exc())
        
def clear_files():
    """
    Permet d'effacer tous les fichiers créés *dans le dossier courant*
    """
    for file in os.listdir(os.getcwd()):
        if re.compile("^[0-9]+.txt").match(file):
            os.remove(file)

def main():
    """
    Assure le bon déroulement du code
    Utiliser `h` pour affichier l'aide.
    """
    help_string = f"\
    [h] to display help\n\
    [l] to launch analysis\n\
    [c] to clear current directory : \n\t`{os.getcwd()}`\n\
    anything else to terminate program"
    print(help_string)
    while True:
        n = input("[h]elp, [l]oop files or [c]lear files : ")
        if n == "l":
            loop_file()
        elif n == "c":
            clear_files()
        elif n =="h":
            print(help_string)
        else:
            exit()

if __name__ == "__main__":
    try:
        main()
    except:
        exit()
    # loop_file()
    # clear_files()
    # while True:
    #     n = input("[l]oop files or [c]lear files : ")
    #     if n == "l":
    #         loop_file()
    #     elif n == "c":
    #         clear_files()
    #     else:
    #         exit()