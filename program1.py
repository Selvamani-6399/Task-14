
import requests


class CountryData:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
    
    def server_status(self):
        return self.response.status_code

    def fetch_data(self):
        try:
            if self.server_status() == 200:
                return self.response.json()
            else:
                print(self.server_status())
        except:
            print("Error")
    # Define a method that will display the name of the countries, currencies and currency symbols
    def show_countries(self):
 
        for item in self.fetch_data():
        
            print(f"Country: {item['name']}")
          
            print()

    # Define a method that will display all those countries which have DOLLAR as its currency
    def show_dollarcountries(self):
       
        dollar_countries = []
   
        for item in self.fetch_data():
       
            if 'Dollar' in item['currencies'][0]['name']:
                
                dollar_countries.append(item['name'])
       
        print(f"Countries that have DOLLAR as their currency are: {', '.join(dollar_countries)}")

    # Define a method that will display all those countries which have EURO as its currency
    def show_eurocountries(self):
       
        euro_countries = []
        
        for item in self.fetch_data():
           
            if item['currencies'][0]['code'] == "EUR":
               
                euro_countries.append(item['name'])

        print(f"Countries that have EURO as their currency are: {', '.join(euro_countries)}")


url= "https://restcountries.com/v3.1/all"
obj = CountryData(url)
print(obj.show_countries())
print(obj.show_dollarcountries())
print(obj.show_eurocountries())
