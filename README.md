# Projet_Preprod_Food
Scraper Python pour récupérer les informations nutritionnelles des aliments via Open Food Facts et les sauvegarder dans un fichier CSV.

## Fichiers
- `food.py` - la classe Food avec toutes ses fonctions
- `get_food.py` - le script principal à lancer
- `test_food.py` - les tests unitaires

## Installation
```bash
pip install requests
```

## Utilisation
```bash
python get_food.py -f tomate
```

## Tests
Les tests vérifient que les fonctions de la classe Food fonctionnent correctement, notamment les getters/setters et la détection des aliments gras.
```bash
python -m unittest test_food.py
```
