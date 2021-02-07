import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://7d249654-31f3-4bb0-a5f8-46d465e17dce.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'yQY9fvJPRrc8Cw1IveCOkEatklg2Uqme'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "sepal_length": 1,
            "sepal_width": 1,
            "petal_length": 2,
            "petal_width": 2,
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


