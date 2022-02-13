from constant import CATEGORY, HIGH, MEDIUM, RATE, STANDARD, WATER ,LOW
import constant

class Price(object):
    #method to get corporation price
    @staticmethod
    def get_corporation_price(water):
        return constant.CORPORATION_RATE * water
    #method to get borewell price
    @staticmethod
    def get_borewell_price(water):
        return constant.BOREWELL_RATE * water
    @staticmethod
    def get_slab_price(slab,water):
        #calculate water in range
        waterinrange=water - CATEGORY[slab][WATER]
        #calculate price of the slab
        price = CATEGORY[slab][RATE] * waterinrange
        #reduce water amount to  apply next slab
        water= CATEGORY[slab][WATER]
        return (water,price)

    #method to get tangker price
    @staticmethod
    def get_tanker_price(water):
        #initialise price to zero
        price=0
        #if water amount is greater than 3000
        if water>CATEGORY[HIGH][WATER]  :
            water,cost=Price.get_slab_price(HIGH,water)
            price+=cost
        #if water amount is greater than 1500
        if water > CATEGORY[MEDIUM][WATER]  :
            water,cost=Price.get_slab_price(MEDIUM,water)
            price+=cost
        #if water amount is greater than 500
        if water > CATEGORY[STANDARD][WATER]  :
            water,cost=Price.get_slab_price(STANDARD,water)
            price+=cost
        #if water amount is less than 500
        if water <= CATEGORY[STANDARD][WATER]  :
            price+=CATEGORY[LOW][RATE] * water
        return price
