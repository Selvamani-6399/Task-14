
import requests


def get_breweries(state):
   
    breweries = []
    
    page = 1
    
    more_pages = True
    
    while more_pages:
       
        url = f"https://api.openbrewerydb.org/breweries?by_state={state}&page={page}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
           
            data = response.json()
            
            if data:
                
                breweries.extend(data)
               
                page += 1
            else:
              
                more_pages = False
        else:
          
            raise Exception(f"Request failed with status code {response.status_code}")

    return breweries


states = ["alaska", "maine", "new york"]


for state in states:

    breweries = get_breweries(state)
  
    print(f"State: {state.title()}")
    print(f"Number of breweries: {len(breweries)}")
    
    types = {}
    
    websites = []
    
    for brewery in breweries:
        
        print(f"Brewery: {brewery['name']}")
        
        brewery_type = brewery['brewery_type']
        
        if brewery_type in types:

            types[brewery_type] += 1
        else:
    
            types[brewery_type] = 1
        
        brewery_website = brewery['https://api.openbrewerydb.org/v1/breweries']
    
        if brewery_website:
            
            websites.append(brewery['name'])
   
    print(f"Types of breweries and their counts:")
    for brewery_type, count in types.items():
        print(f"{brewery_type}: {count}")
  
    print(f"Number of breweries that have websites: {len(websites)}")
    print(f"Names of breweries that have websites: {', '.join(websites)}")
   
    print()
