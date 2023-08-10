import json
import cenerator
from packmock import patch_pack, JsonCompare, DATA_BASE


class TestMinimalPack:

    @patch_pack
    def test_empty_pack(self):
        pack = cenerator.Pack('test_pack', 'test', 'Empty pack')

        assert cenerator.Pack.open.get_files() == {
            'pack.mcmeta': JsonCompare({
                'pack': {
                    'pack_format': 7,
                    'description': 'Empty pack',
                },
            }),
        }
        assert cenerator.Pack.open_data.get_files() == DATA_BASE


class TestFunc:

    @patch_pack
    def test_simple_func(self):
        pack = cenerator.Pack('test_pack', 'test', 'Simple pack')
        
        @pack.func()
        def test_func(c):
            c('say Test')

        assert cenerator.Pack.open_data.get_files() == {
            **DATA_BASE,
            'test/functions/test_func.mcfunction': 'say Test\n',
        }

    @patch_pack
    def test_named_func(self):
        pack = cenerator.Pack('test_pack', 'test', 'Simple pack')
        
        @pack.func(name='test_named')
        def test_func(c):
            c('say Test')

        assert cenerator.Pack.open_data.get_files() == {
            **DATA_BASE,
            'test/functions/test_named.mcfunction': 'say Test\n',
        }

    @patch_pack
    def test_tagged_func(self):
        pack = cenerator.Pack('test_pack', 'test', 'Simple pack')
        
        @pack.func(tags=['minecraft:load'])
        def test_load(c):
            c('say Test')
        
        @pack.func(tags=['test:tag'])
        def test_tag(c):
            c('say Test')

        assert cenerator.Pack.open_data.get_files() == {
            **DATA_BASE,
            'minecraft/tags/functions/load.json': JsonCompare({
                'values': ['cenerator:scoreboard','test:test_load'],
            }),
            'test/tags/functions/tag.json': JsonCompare({
                'values': ['test:test_tag'],
            }),
            'test/functions/test_load.mcfunction': 'say Test\n',
            'test/functions/test_tag.mcfunction': 'say Test\n',
        }

