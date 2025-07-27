import os
import json

# Dossier racine contenant les sous-dossiers d'images
root_dir = "images"

# Dictionnaire final à écrire dans le JSON
images_data = {}

# On parcourt tous les sous-dossiers de 'images/'
for category in os.listdir(root_dir):
    cat_path = os.path.join(root_dir, category)
    if os.path.isdir(cat_path):
        # Filtrer uniquement les fichiers image (jpg, jpeg, png)
        images = [
            f for f in os.listdir(cat_path)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
        # On trie pour l’ordre si besoin
        images.sort()
        images_data[category] = images

# Écriture du fichier JSON
with open("images.json", "w", encoding="utf-8") as f:
    json.dump(images_data, f, indent=2, ensure_ascii=False)

print("✅ Fichier images.json généré avec succès.")
