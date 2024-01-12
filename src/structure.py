import pathlib
from utils import get_manifest_file, get_config_file, get_actual_path
from datetime import date
from typing import overload, Dict, Any, Union, List

# Code to create the directories and files
class ProjectBasicStructure:
    def __init__(self, package_name: str):
        self.package_name = package_name

        self._manifest = get_manifest_file()
        self._actual_dir = get_actual_path()
        
        # Read the config file, return the content of the file and pass it to the create project files method.
        content: List[str] | None = self._read_file(self.config_file)
        self._create_project_files(content)

    @property
    def config_file(self) -> Union[Dict[str, Any], Any, str]:
        try:
            config_file: Union[Dict[str, Any], Any, None] = get_config_file()
            return config_file
        except Exception as e:
            return f'Error: {e}'

    @property
    def manifest_file(self) -> Union[Dict[str, Any], str]:
        try:
            manifest_file: Dict[str, Any] = get_manifest_file()
            return manifest_file
        except Exception as e:
            return f'Error: {e}'

    @staticmethod
    def _read_file(f) -> Union[List[str], None]:
        if str(f).endswith('json') or str(f).endswith('toml'):
            with open(f, 'w') as f:
                file_content = f.readlines()
            return file_content
        else:
            return None
    
    @overload
    def _create_project_files(self, content: None) -> None: ...

    @overload
    def _create_project_files(self, content: List[str]) -> None:...

    def _create_project_files(self, content):
        if isinstance(content, list):
            for string in content:
                file_to_create = pathlib.Path(string)

                #Se o arquivo já existe, não faz nada.
                if file_to_create.exists():
                    pass

                # Se o arquivo não existe, cria o arquivo.
                else:
                    file_to_create.touch()
        else:
            all_files_and_dirs = list(self._actual_dir.iterdir())
            for names in all_files_and_dirs:
                print(names)

    
    def _create_config_file(self):
        content = f"""
        [package]
        name = "{self.package_name}"
        version = "0.1.0"
        edition = "{date.today().year}"

        [dependencies]
        """
        with open('D1va.toml', 'w+') as f:
            f.writelines(content)

main = ProjectBasicStructure('d1va')
main._create_project_files(None)
