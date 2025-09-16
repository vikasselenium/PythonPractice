


class Sale:
    def __init__(self,amount):
        self.amount=amount

    @staticmethod
    def find_totol_sale(sales_list):
        total_sale = 0
        for sale in sales_list:
            total_sale = total_sale + sale.amount
        return total_sale

total= Sale.find_totol_sale([Sale(100),Sale(200)])
print(total)