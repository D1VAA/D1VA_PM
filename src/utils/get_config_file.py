from typing import Union, Dict, Any
from pathlib import Path
from .exceptions import FileNameConflict

actual_dir = Path.cwd()

def get_config_file() -> Union[Dict[str, Any], Any, None]:
    """Função para pegar o arquivo de configuração"""
    config_file = actual_dir.glob('**/d1va_config.*')
    count = [x for x in config_file]

    assert len(count) < 2, FileNameConflict('[Error] >> Encontrado dois ou mais arquivos de configuração.')
    
    config_file_path = next(config_file)
    if config_file_path.suffix == 'json':
        from json import load
        with open(config_file_path, 'r') as f:
            json_file = load(f)
        return json_file

    elif config_file_path.suffix == 'toml':
        from toml import load
        with open(config_file_path) as f:
            toml_file = load(f)
        return toml_file
    else:
        return None
