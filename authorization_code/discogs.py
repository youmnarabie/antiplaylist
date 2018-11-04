
import sys


key = "rMSSoUTCGrIYupZvSiEe"
secret = "EVxsbFqVAIFpqIuQWswsUBCzKeKncxWo"
d = discogs_client.Client('ExampleApplication/0.1', user_token = 'PGtPrKkPRHNwSSkSEnDAUrothkMjdsoPczOyeeYu')
# d.set_consumer_key(key, secret)
# url = d.get_authorize_url()
# request_token = url[0]
# request_secret = url[1]
# authorize_url = url[2]
# print(authorize_url)
# verifier = input("Insert verification after visiting link \n")
# type(verifier)
# stuff = d.get_access_token(verifier)
# access_token = stuff[0]
# access_secret = stuff[1]

results = d.search("Rooting for my baby")
artist = results[0].data.get("genre")
print(artist)