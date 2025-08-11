import dataclasses
from typing import List, Dict, Any, Optional

# Utilisation de @dataclasses.dataclass pour créer automatiquement
# les méthodes __init__, __repr__, etc. C'est plus propre.

@dataclasses.dataclass
class IDLookupConfig:
    """ Représente la configuration pour la recherche d'une entité existante. """
    lookup_endpoint: str
    lookup_query_param: str
    lookup_response_data_path: Optional[str] = None

@dataclasses.dataclass
class IntegrationStep:
    """ Représente une étape complète de synchronisation. """
    name: str
    source_file: str
    response_id_field: str
    lookup_key_column: str
    id_lookup_config: IDLookupConfig
    enabled: bool = True
    mode: str = "sync"  # "sync" ou "lookup_only"
    endpoint: Optional[str] = None
    payload_mapping: Optional[Dict[str, Any]] = None

    # Cette méthode sera utile plus tard pour créer un objet IntegrationStep
    # à partir d'un dictionnaire (ce que nous lirons du JSON).
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IntegrationStep':
        lookup_config_data = data.pop('id_lookup_config')
        id_lookup_config = IDLookupConfig(**lookup_config_data)
        return cls(id_lookup_config=id_lookup_config, **data)

@dataclasses.dataclass
class Config:
    """ Représente l'ensemble du fichier de configuration. """
    api_base_url: str
    integration_steps: List[IntegrationStep]
    global_headers: Optional[Dict[str, str]] = None
    use_id_cache: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Config':
        steps_data = data.pop('integration_steps')
        steps = [IntegrationStep.from_dict(step_data) for step_data in steps_data]
        return cls(integration_steps=steps, **data)