from __future__ import annotations
from src.facades.config.config_reader import ConfigReader
from src.helpers.file.file_finder import FileFinder
from src.delegators.image_delegator import ImageDelegator
from tqdm import tqdm

class AppDelegator:
    def apply_config(self) -> AppDelegator:
        for key, value in ConfigReader.read().items():
            setattr(self, f'_{key}', value)
            print('[%s]: %s' % (key, value))
        return self
    
    def read_files(self) -> AppDelegator:
        print('reading files')
        self.files = FileFinder.all_files_recursive(self._directory_path, file_type=self._from_format)
        return self
    
    def convert_files(self) -> AppDelegator:
        print('converting files')
        for _, file_path in tqdm(self.files):
            ImageDelegator(
                file_path=file_path
            ) \
                .read_file() \
                .save_file(path=file_path[:-len(self._from_format) - 1] , file_format=self._to_format)
        return self
