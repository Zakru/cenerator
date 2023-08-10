import json
import cenerator
from packmock import patch_pack, DATA_BASE


class TestExecute:

    @patch_pack
    def test_simple_execute(self):
        pack = cenerator.Pack('test_pack', 'test', 'Simple pack')
        
        @pack.func()
        def test_func(c):
            c('say Outside')
            with c.ex('as @a') as c:
                c('say Inside')

        assert cenerator.Pack.open_data.get_files() == {
            **DATA_BASE,
            'test/functions/test_func.mcfunction': 'say Outside\nexecute as @a run function test:ex_1\n',
            'test/functions/ex_1.mcfunction': 'say Inside\n',
        }

