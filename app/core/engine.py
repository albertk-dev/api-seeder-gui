import json
import pandas as pd
from pathlib import Path
from typing import Dict, Any

from .models import Config, IntegrationStep

class SeederEngine:
    def __init__(self):
        self.config: Config | None = None
        self.id_cache: Dict[str, Dict[str, Any]] = {} # Pour stocker les ID trouvés

    def load_config_from_file(self, filepath: str | Path) -> None:
        """
        Charge la configuration depuis un fichier JSON et la valide
        en utilisant les modèles de données.
        """
        print(f"Chargement de la configuration depuis : {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                config_data: Dict[str, Any] = json.load(f)
            
            self.config = Config.from_dict(config_data)
            
            print("Configuration chargée et validée avec succès.")
        except Exception as e:
            print(f"ERREUR lors du chargement de la configuration : {e}")
            raise

    def run(self) -> None:
        """
        Point d'entrée principal pour lancer le processus de synchronisation.
        """
        if not self.config:
            print("ERREUR: La configuration n'a pas été chargée. Impossible de démarrer.")
            return

        print("\n--- Début du processus de synchronisation ---")
        for step in self.config.integration_steps:
            if not step.enabled:
                print(f"\nÉtape '{step.name}' ignorée (désactivée).")
                continue
            
            print(f"\n>>> Traitement de l'étape : '{step.name}'")
            self._process_step(step)
        
        print("\n--- Processus de synchronisation terminé ---")

    def _process_step(self, step: IntegrationStep) -> None:
        """
        Traite une seule étape d'intégration : lit le fichier source
        et prépare les données.
        """
        try:
            # Construire le chemin complet vers le fichier source.
            # On suppose que le fichier config.json est à la racine du projet.
            source_path = Path('../') / step.source_file
            
            print(f"  - Lecture du fichier source : {source_path}")
            df = pd.read_excel(source_path)

            # Validation simple : vérifier que la colonne clé existe
            if step.lookup_key_column not in df.columns:
                print(f"  - ERREUR: La colonne clé '{step.lookup_key_column}' est introuvable dans le fichier '{source_path}'.")
                return

            print(f"  - {len(df)} ligne(s) trouvée(s) dans le fichier.")
            
            # Pour l'instant, nous allons simplement afficher le contenu
            # pour vérifier que la lecture fonctionne.
            print("  - Aperçu des données :")
            print(df.head().to_string(index=False))

        except FileNotFoundError:
            print(f"  - ERREUR: Le fichier source '{source_path}' n'a pas été trouvé.")
        except Exception as e:
            print(f"  - ERREUR inattendue lors du traitement de l'étape '{step.name}': {e}")

