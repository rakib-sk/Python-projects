class Customer:
    cupons = {
        "ALFI": 20,
        "SANJIDHA": 30,
    }
    
    def __init__(self,id,buget,coupon):
        self.id = id
        self.buget = buget
        self.coupon = coupon
        
    def byProducts(self, price):
        couponValue = self.cupons.get(self.coupon, 0)
        discountPrice = price * (100 - couponValue) / 100
        self.buget = self.buget - discountPrice
        
        
c1 = Customer(1, 1000, "ALFI")
    
c1.byProducts(1000)

cus = [
    f"id: {c1.id}",
    f"buget: {c1.buget}",
    f"Use coupon: {c1.coupon}"
]

for c in cus:
    print(c)
