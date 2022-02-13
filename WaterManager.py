'''water management program'''
#loading modues
import constant
import math
from Price import Price

class WaterManager(object):
    '''WaterManager class'''
    #constructor
    def __init__(self):
        self.consumed_water=0
        self.cost=0
        self.guests=0
    
    #method to allot water to flates and among guests
    def allot_water(self,flat,corporation,borewell):
        #calculate water as per flat type
        water=constant.WATER_PER_PERSON * constant.PERSON_IN_FLAT[flat] * constant.MONTH
        #add water to total water
        self.consumed_water+=water
        #calculate portion of corporation water
        corporation_water = water * corporation/(corporation + borewell)
        #get price of corporation water
        self.cost += Price.get_corporation_price(corporation_water)
        #calculate portion of borewell water
        borewell_water = water * borewell /(corporation + borewell)
        #get borewell water price
        self.cost+=Price.get_borewell_price(borewell_water)
    #method to add guests
    def add_guest(self,guests):
        self.guests+=guests
    #method to calcuate bill
    def get_bill(self):
        #calcuate water for guests
        water=self.guests * constant.WATER_PER_PERSON * constant.MONTH
        #add to total water
        self.consumed_water+=water
        print(self.cost)

        #get tanker costs and add to tota cost
        self.cost+=Price.get_tanker_price(water)
        #print total water and cost
        print(self.cost)
        print(self.consumed_water,math.ceil(self.cost))
