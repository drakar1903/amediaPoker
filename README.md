# amediaPoker

HOW TO USE:

Run docker-compose up --build and access http://0.0.0.0:8000/docs for endpoints

# Generate random hand

Click the appropriate endpoint in the /docs, or do a curl:

```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/randomhand/' \
  -H 'accept: application/json' \
  -d ''
```

# Upload a hand
Click the appropriate endpoint in the /docs and specify the payload, or do a curl:

```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/hand/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "card_3": "6c",
  "id": 53,
  "card_5": "2h",
  "card_1": "6d",
  "card_2": "qc",
  "card_4": "js"
}'
```

Technical limitation: ID must be given in a hand, but it will be assigned the lowest currently unassigned ID

# Fetch a hand
Click the appropriate endpoint in the /docs and specify the payload (hand ID), or do a curl:

```sh
curl -X 'GET' \
  'http://0.0.0.0:8000/hand/12' \
  -H 'accept: application/json'
```

Alternatively, you can fetch *all* hands in the database

```sh
curl -X 'GET' \
  'http://0.0.0.0:8000/hands/?skip=0&limit=100' \
  -H 'accept: application/json'
```


# Compare hands

Do a curl:

```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/compareHands' \
  -H 'accept: application/json' \
  -d '[{
		"card_1": "js",
		"card_2": "ac",
		"card_3": "2c",
		"card_5": "jd",
		"card_4": "4c",
		"id": 50
	},
	{
		"card_1": "2s",
		"card_2": "3c",
		"card_3": "4c",
		"card_5": "5d",
		"card_4": "6c",
		"id": 51
	},
	{
		"card_1": "2c",
		"card_2": "3c",
		"card_3": "4c",
		"card_5": "5c",
		"card_4": "6c",
		"id": 51
	}
]'
```

