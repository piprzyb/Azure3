import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://9d9f9b7d-c829-49e6-9cc9-1cfac99ab9df.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'e6om6dbipiGVhkDnCMAg0eMFE97tIfhN'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "sepal_length": 6.1,
            "sepal_width": 2.8,
            "petal_length": 4.0,
            "petal_width": 1.3,
          }
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


