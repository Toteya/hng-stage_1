# HNG Stage 1 - Number Classification API

This public API returns interesting mathematical properties about it any given number, including a fun fact.

## Table of Content
* [Setup](#setup)
* [API](#api)
* [Links](#links)

## Setup

#### Install dependencies:
`pip install -r requirements.txt`

#### Run the web application:
`python3 -m api.v1.app`

#### Access endpoint locally:
`localhost:5000/api/classify-number?number=<number>`


## API

#### Endpoint URL:
`https://hng-stage-1-kslo.onrender.com/api/classify-number?number=<number>`

#### Request / Response Format
- Resquest:

`GET** https://hng-stage-1-kslo.onrender.com/api/classify-number?number=4`

- Response (JSON):

```
{
  "digit_sum": SUM OF DIGITS,
  "fun_fact": AN INTERESTING FACT
  "is_perfect": true/false,
  "is_prime": true/false,
  "number": THE NUMBER,
  "properties": []
}
```

#### Example Usage:
- Resquest:

`curl -s https://hng-stage-1-kslo.onrender.com/api/classify-number?number=4`

- Response:

```
{
   "digit_sum" : 5,
   "fun_fact" : "5 is the number of kyu (pupil) grades in judo.",
   "is_perfect" : false,
   "is_prime" : true,
   "number" : 5,
   "properties" : [
      "odd",
      "armstrong"
   ]
}
```

## Links
* [HNG Python Developers](https://hng.tech/hire/python-developers)
* [Numbes API](http://numbersapi.com)
