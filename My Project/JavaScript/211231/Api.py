import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "0dc3d3ce56mshe91af5994dca501p12ddffjsn7c63d5cd810a"
    }

conn.request("GET", "/weather?q=Seoul%2Ckr&lat=0&lon=0&callback=test&id=2172797&lang=null&units=imperial&mode=xml", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))