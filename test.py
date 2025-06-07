import os

def show_tree(path, indent=0):
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        print("  " * indent + item)
        if os.path.isdir(item_path):
            show_tree(item_path, indent + 1)

root_path = r"C:\Users\Usuario\Documents\Proyectos-personales\plant_disease_app\models"
show_tree(root_path)
