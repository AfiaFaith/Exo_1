import os

def create_project_structure():
    project_path = 'data_analysis_project'
    remote_repository_url = 'https://github.com/AfiaFaith/Exo_1.git'

    # Check if the project directory already exists
    if not os.path.exists(project_path):
        os.makedirs(os.path.join(project_path, 'data', 'cleaned'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'data', 'raw'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'docs'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'models'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'notebooks'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'reports'), exist_ok=True)
        os.makedirs(os.path.join(project_path, 'src'), exist_ok=True)

        # Éditer les fichiers à l'intérieur de l'arborescence
        with open(os.path.join(project_path, 'notebooks', 'main_notebook.ipynb'), 'w') as nb_file:
            nb_file.write('Notebook Content')
        
        with open(os.path.join(project_path, 'src', 'utils.py'), 'w') as utils_file:
            utils_file.write('Utility functions')

        # Initialiser le dépôt
        os.system('git init')

        # Ajouter tous les fichiers de l'arborescence
        os.system('git add .')

        # Faire un commit
        os.system('git commit -m "Initial commit"')

        # Lier le dépôt local au dépôt distant
        os.system(f'git remote add origin {remote_repository_url}')

        # Pousser les changements vers le dépôt distant
        os.system('git push -u origin master')
    else:
        print("The project directory already exists. Please choose a different name or delete the existing directory.")

create_project_structure()
