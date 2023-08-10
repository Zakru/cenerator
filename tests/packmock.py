from io import StringIO
import json
from typing import Dict
from unittest.mock import patch

import cenerator


class MockFile(StringIO):

    def __init__(self):
        super().__init__()
        self.final_data = None

    def close(self):
        self.closed_data = self.getvalue()
        super().close()


class MockOpen:

    def __init__(self):
        self.files: Dict[str, MockFile] = {}

    
    def __call__(self, path):
        file = MockFile()
        self.files[path] = file
        return file
    
    def get_files(self) -> Dict[str, str]:
        return { path: file.closed_data for path, file in self.files.items() }


def patch_pack(target):
    return patch.object(cenerator.Pack, 'open', MockOpen())(
        patch.object(cenerator.Pack, 'open_data', MockOpen())(target))


class JsonCompare:

    def __init__(self, data):
        self.data = data
    
    def __eq__(self, other):
        return True if json.loads(other) == self.data else NotImplemented
    
    def __repr__(self):
        return repr(json.dumps(self.data))


DATA_BASE = {
    'cenerator/functions/scoreboard.mcfunction': 'scoreboard objectives add _cen dummy\n',
    'minecraft/tags/functions/load.json': JsonCompare({
        'values': ['cenerator:scoreboard'],
    }),
}
