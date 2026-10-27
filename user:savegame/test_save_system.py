import unittest
from pathlib import Path
import send2trash
from save_system import save_game


class TestSaveSystem(unittest.TestCase):
    def setUp(self):
        base_dir=Path(__file__).parent
        with open(base_dir/'savegame_slot1.json','w',encoding="utf-8")as f:
            f.write("{}")
        with open(base_dir / 'savegame_slot2.json', 'w', encoding="utf-8") as f:
            f.write("{}")

    def tearDown(self):
        base_dir = Path(__file__).parent
        send2trash.send2trash(base_dir / 'savegame_slot1.json')
        send2trash.send2trash(base_dir / 'savegame_slot2.json')

    def test_save_system(self):
        base_dir = Path(__file__).parent
        player = {
            "level": 5,
            "hp": 85,
            "gold": 1200,
            'mp':50,
            "inventory": ["铁剑", "治疗药水", "地图"]
        }
        result = save_game(player, slot=1)
        self.assertTrue(result)
        slot1_file = base_dir / "savegame_slot1.json"
        self.assertTrue(slot1_file.exists())

if __name__ == '__main__':
    unittest.main()
