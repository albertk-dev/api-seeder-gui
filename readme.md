<div align="center">

# 🖥️ API Seeder GUI

**Application de bureau graphique (Desktop GUI) propulsée par PySide6 (Qt) pour orchestrer et visualiser l'ingestion de données Excel vers API REST.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![GUI](https://img.shields.io/badge/GUI-PySide6%20(Qt)-41CD52.svg?logo=qt&logoColor=white)](https://www.qt.io/)
[![CLI Companion](https://img.shields.io/badge/Companion-API%20Seeder%20CLI-orange.svg)](https://github.com/albertk-dev/api-seeder)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📌 Présentation

**API Seeder GUI** est l'interface graphique officielle pour le moteur [API Seeder](https://github.com/albertk-dev/api-seeder). Conçue avec **PySide6 (Qt for Python)**, elle permet aux équipes techniques et métiers de :
* Sélectionner et configurer intuitivement les fichiers Excel sources et endpoints API.
* Visualiser en temps réel la progression de la synchronisation étape par étape.
* Examiner les rapports d'erreurs et logs d'exécution sans passer par le terminal.

---

## 🚀 Installation & Lancement

### 1. Cloner le projet & créer l'environnement

```bash
git clone https://github.com/albertk-dev/api-seeder-gui.git
cd api-seeder-gui

python -m venv venv

# Sur Linux / macOS :
source venv/bin/activate
# Sur Windows :
.\venv\Scripts\activate
```

### 2. Installer les dépendances (Qt / PySide6)

```bash
pip install -r app/requirements.txt
```

### 3. Lancer l'application graphique

```bash
python app/main.py
```

---

## 🔗 Projet Associé

* Moteur en ligne de commande (CLI) : 👉 **[api-seeder](https://github.com/albertk-dev/api-seeder)**

---

## 👤 Auteur & Contact

* **Albert Kameni** (*"Le débogueur"*) — Software Engineer
* **GitHub** : [@albertk-dev](https://github.com/albertk-dev)
* **LinkedIn** : [albertk-linked](https://www.linkedin.com/in/albertk-linked)
