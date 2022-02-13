import unittest
from geektrust import WaterManager
from Price import Price

class TestWaterManager(unittest.TestCase):
    def setUp(self):
        manager=WaterManager()
    def test_get_corporation_price(self):
        self.assertEqual(Price.get_corporation_price(1),1)
    def test_get_borewell_price(self):
        self.assertEqual(Price.get_borewell_price(1),1.5)
    def test_get_tanker_price(self):
        self.assertEqual(Price.get_tanker_price(4000),19500)
    def test_allot_water(self):
        manager=WaterManager()
        manager.allot_water(2,1,2)
        self.assertEqual(manager.cost,1200)
    def test_add_guest(self):
        manager=WaterManager()
        manager.add_guest(5)
        self.assertEqual(manager.guests,5)
    def test_get_bill(self):
        manager=WaterManager()
        manager.get_bill()
        self.assertEqual(manager.cost,0)
    