import csv:
class Stock:
    def __init__(self,name,symbol,exchange,price)
    self.name=name
    self.symbol=symbol
    self.exchange=exchange
    self.price=price
def __str__(self):
    return f"{self.name},{self.symbol},{self.exchange},{self.price}"
try:
    with open("stock_price.csv") as f:
        data=csv.DictRaeder(f,delimiter=",")
        stock-lsr=[]
        line=0
        for d in data:
            if line==0:
                line+=1
                continue
            stock_lst.append(Stock(*d))
    for s in stock_lst:
        if "K" in s.price:
            s.price=float(s.price.replacr("K",""))*1
        else:
            s.price=float(s.price.strip())
            print(s)
    except Exception as e:
        print('Exception number:{},value{!r}'.format)

    def show_stock_by_price:
        st_lst=clean_init_get_stocks()
        f=filter(lambda x:x.price <= price,st_lst)
        if f:
            show-stock_info(list(f))
            