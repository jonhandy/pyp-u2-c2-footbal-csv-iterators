import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        
                
    def all(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                yield player
            
            raise StopIteration()


    def keep_player(self, country, year, player):
        #return True if player object contains defined parameters 
        param_values = {
            'year':year,
            'country':country,
            #'age':age,
            #'position':position
        }
        
        params = ['country', 'year'] #, 'age', 'position'
        
       
        
        for param in params:
            value = param_values[param]
            if value and getattr(player, param) != value:
                return False
        return True
                
            
        
        
    
    def search(self, country=None, year=None):
        if country is None and year is None:
            raise ValueError()
        return self._search(country=country, year=year)
        
    def _search(self, country, year):
        for player in self.all():
            if self.keep_player(country, year, player):
                yield player
        
        raise StopIteration()


