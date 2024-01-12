import pathlib
import toml
from pathlib import Path
from typing import Any, Dict, List
from .exceptions import FileNameConflict

actual_dir = pathlib.Path.cwd()

def get_manifest_file() -> Dict[str, Any]:
    """Função para coletar dados do manifest file"""
    config_file = list(actual_dir.glob('**/d1va.toml'))

    # Lista para contar a quantidade de arquivos com o mesmo nome
    count: List[Path] = [f for f in config_file]  
    if len(count) > 1:
        raise FileNameConflict('[Erro] >> 2 ou mais arquivos de configuração encontrados...')

    if config_file:
        config_file_path = config_file[0].as_posix()
        with open(config_file_path, 'r') as file_content:
            config = toml.load(file_content)
        
        return config
    else:
        raise FileNotFoundError("Arquivo de configuração 'd1va.toml' não encontrado.") 