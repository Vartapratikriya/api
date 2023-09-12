# Vartapratikriya API

This API provides access to a live scraped set of articles and insights about them.

## Endpoints

The API has the following endpoints:

- `/`
  - This endpoint returns the version of the API and the status of the server.
- `/articles/top`
  - This endpoint returns the top keywords from the last scraped articles.
- `/articles/headlines`
  - This endpoint returns the latest scraped top headlines.
- `/articles/categories`
  - This endpoint returns the articles in the specified category. The category can be specified by the `category` query parameter.

## Example Requests & response

The following are examples of requests that you can make to the API:

- To get the version of the API, you can make a GET request to the `/` endpoint.

#### Request:

```
GET https://vartapratikriya-api.vercel.app/
```

#### Response:

```
{
  "status": "ok",
  "vartapratikriya": "v0.1.0"
}
```

- To get the top articles, you can make a GET request to the `/articles/top` endpoint.

#### Request:

```
GET https://vartapratikriya-api.vercel.app/articles/top
```

#### Response:

```
{
  "generated_at": "2023-09-12 04:22:14.962075",
  "insights": "v0.1.0",
  "keywords": [
    [
      "India",
      41
    ],
   ...
  ]
}

```

- To get the headlines of the articles, you can make a GET request to the `/articles/headlines` endpoint.

#### Request:

```
GET https://vartapratikriya-api.vercel.app/articles/headlines
```

#### Response:

```
{
   "news_listener": "v0.1.0",
   "generated_at": "2023-09-12 04:59:08.253620",
   "articles": [...]
}
```

#### Request:

- To get the articles in the specified category, you can make a GET request to the `/articles/categories` endpoint and specify the category in the `category` query parameter. Available categories: [
  "sports",
  "healthcare",
  "business",
  "media",
  "laws",
  "entertainment",
  "weather",
  "policy",
  ]

```
GET https://vartapratikriya-api.vercel.app/articles/categories?category=business
```

#### Response:

```
{
    "news_listener": "v0.1.0",
    "scraped_at": "2023-09-12 04:59:14.259942",
    "articles": {
        "sports": [..],
        ...
    }
}
```
