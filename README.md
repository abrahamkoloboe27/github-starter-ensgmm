# GitHub Starter Guide : Concepts de Base Git/GitHub

Ce repo est un guide d'introduction aux concepts fondamentaux de Git et GitHub. Vous y trouverez les principes essentiels pour démarrer avec le versioning de code.

## 📚 Concepts Clés

### Git vs GitHub
- **Git** : Système de contrôle de version distribué (DVCS) pour tracker les modifications de code [4][5]
- **GitHub** : Plateforme cloud hébergeant des repos Git avec outils de collaboration [4][5]

### Architecture GitHub
- **Frontend** : HTML/CSS/JavaScript pour l'interface utilisateur
- **Backend** : Ruby on Rails + base de données MySQL distribuée [6]
- **Microservices** : Architecture modulaire avec Docker/Kubernetes [6]

### Composants Principaux
| Terme | Définition | Commande Associée |
|-------|------------|-------------------|
| **Repository** | Dossier projet avec historique complet | `git init` [2] |
| **Commit** | Instantané des modifications | `git commit -m "msg"` [3] |
| **Branche** | Ligne de développement isolée | `git checkout -b feat` [2] |
| **Pull Request** | Proposition de fusion de code | GitHub Web Interface [8] |
| **Merge** | Intégration de changements | `git merge` [2][8] |

## 💻 Commandes Essentielles

```
# Initialiser un repo
git init

# Cloner un repo distant
git clone https://github.com/user/repo.git

# Ajouter des modifications
git add fichier.py
git add .  # Tous les fichiers

# Commiter
git commit -m "Description des changements"

# Push vers remote
git push origin main

# Récupérer les mises à jour
git pull origin main

# Gestion des branches
git checkout -b nouvelle-fonction
git merge branche-secondaire
```

## 🔄 Workflow de Contribution
1. **Forker** le repo via GitHub [7]
2. **Cloner** en local : `git clone [URL]`
3. Créer une **branche** : `git checkout -b amelioration`
4. Faire des **commits** descriptifs
5. **Pusher** : `git push origin amelioration`
6. Ouvrir **Pull Request** sur GitHub [8]
7. **Révision** + **Merge** des changements [8]

## 📚 Ressources
- [Documentation Officielle GitHub](https://docs.github.com) [2][5]
- [Guide Visuel Git](https://www.pierre-giraud.com) [4]
- [Commandes Avancées](https://www.simplilearn.com) [9]
