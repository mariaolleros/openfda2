import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?search=salycilic", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos1 = json.loads(repos_raw)

repo=repo['results']

for element in repo:
    print("This aspirin is produced by these manufactures :",repo[0]['patient']['drug'][1]['openfda']['manufacturer_name'])




