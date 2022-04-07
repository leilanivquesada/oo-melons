import random as rand
import datetime

"""Classes for melon orders. AbstractMelonOrder is base class for DomesticMelonOrder and InternatiommalMelonOrder"""
class AbstractMelonOrder:
    """" melon order superclass"""
    def __init__(self, species, qty, country_code,order_type,tax):
        
        if qty > 100:
            raise TooManyMelonsError()
        
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = ""
        self.tax = 0
        
        
    def get_base_price(self):

        # date = datetime.date()
        # weekday = date.weekday()
        # time = datetime.time()
        # print(date)

        """random number betwen 5-9"""
        base_price = rand.randrange(5,10)

        return base_price
        
        
    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        
        #price adjustment added for Christmas melons at 1.5x base price
        if self.species == "Christmas":
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        #flat fee of $3 added to all int orders with less than 10 melons shipped
        if self.country_code != "USA" and self.qty < 10:
            total += 3
            
        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True
        
    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "USA", "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code, "international", 0.17)
        
class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order (no tax, domestic)"""
    def __init__(self,species,qty):
        super().__init__(species,qty,"USA", "domestic", 0)
        self.passed_inspection = False
        
    def mark_inspection(self,passed):
        if passed == True:
            self.passed_inspection = True

class TooManyMelonsError(ValueError):
    """creates an error when melon orders > 100"""
    def __init__(self):
        super().__init__("No more than 100 Melons Allowed!")
        # try:
        #     self.qty < 100
        # except ValueError:
           