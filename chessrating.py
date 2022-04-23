import requests
import json

class Rating:

    def __init__(self):
        self.search_count = 0
        self.failed_searches = 0
        self.chess_player = ""
        self.search_list = []
        self.in_search_mode = False
        self.from_function = ""

    def get_searches(self):
        self.in_search_mode = True
        print("Your previous searches are: \n")
        for x in self.search_list:
            print(x)
        print("\n")

    def api_request(self, player):
        response = requests.get('https://api.chess.com/pub/player/' + player + '/stats')

        if response.status_code == requests.codes.ok:
            return response              

    def search_ratings(self):

        while True:
            self.search_count += 1

            print("\n")
            print('Get a Chess.com rating:')
            
            self.chess_player = input('Enter a Chess.com username: ')

            if self.chess_player == "getmethefuckout":
                print('Thank you for searching Chess.com ratings!')
                break

            if self.chess_player == "!prev_searches":
                self.in_search_mode = True             
                self.get_searches()    
                self.in_search_mode = False
                self.from_function = "search"
                self.search_count -= 1
                self.failed_searches -= 1

            if(self.in_search_mode is False):
                
                self.search_list.append(self.chess_player)
                response = self.api_request(self.chess_player)
                        
                if response is None:
                    self.failed_searches += 1

                    if(self.from_function != "search"):
                        print("Sorry, there was an error with your request! \n")
                    
                    print("Search count: ", "\n Total: ", self.search_count,
                    "\n Failed: ", self.failed_searches)
                    
                else:   
                
                    data = response.json()

                    if  "chess_rapid" in data:
                        rapid_rating = data['chess_rapid']['last']['rating']
                    else:
                        rapid_rating = "Rapid rating was not found!"
                        
                    if  "chess_blitz" in data:
                        blitz_rating = data['chess_blitz']['last']['rating']
                    else:
                        blitz_rating = "Blitz rating was not found!"
                    
                    if  "chess_bullet" in data:
                        bullet_rating = data['chess_bullet']['last']['rating']
                    else:
                        bullet_rating = "Bullet rating was not found!"
                    
                    print("Your Chess.com ratings are: \n",
                    "Rapid: ", rapid_rating,
                    "\n Blitz: ", blitz_rating,
                    "\n Bullet: ", bullet_rating)

                    print("\n Search count: ", "\n Total: ", self.search_count,
                        "\n Failed: ", self.failed_searches)
        

p2 = Rating()
p2.search_ratings()

