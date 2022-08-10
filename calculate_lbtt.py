class PurchasePriceBands:
    def __init__(self, low, high, rate):
        self.low = low
        self.high = high
        self.rate = rate


def calculate_lbtt_first_time_buyer(property_value):
    pass

def calcultate_lbtt_previous_buyer(property_value):
    price_bands = [PurchasePriceBands(0, 145000, 0), PurchasePriceBands(145001, 250000, 0.02), PurchasePriceBands(250001, 325000, 0.05), PurchasePriceBands(325001, 750000, 0.10), PurchasePriceBands(750001, float('inf'), 0.12)]
    bands = []
    tax = 0

    for band in price_bands:
        if band.low < property_value:
            bands.append(band)

    for band in bands:
        if band.high < property_value:
            tax += (band.high - band.low)*band.rate
        
        else:
            tax += (property_value - band.low)*band.rate
    
    return round(tax)

property_value = float(input("Enter home price: "))
tax = calcultate_lbtt_previous_buyer(property_value)
print(tax)
