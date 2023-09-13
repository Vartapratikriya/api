# Vartapratikriya-API

## Endpoints

- `/`
  - Returns the status of the application.
- `/config`
  - Returns the configuration of the application.
- `/articles/top_keywords`
  - Returns a list of articles, each with a list of its top keywords.
  - The `filter` query parameter can be used to filter the results by language or category.
- `/articles/sentiment`
  - Returns a dictionary of sentiment scores for each language or category.
  - The `filter_by` query parameter must be set to `language` or `category`.
- `/articles/headlines`
  - Returns a list of articles, each with its headline.
  - The `filter` query parameter can be used to filter the results by language or category.
  - Available filter options are `language`, `category`, & `publishedAt`
- `/articles/categories`
  - Returns a list of articles, each with its category.
  - The `filter` query parameter can be used to filter the results by language or category.
  - Available filter options are `language`, `category`, & `publishedAt`

## Queries

The following queries can be used to filter the results of the API endpoints:

- `filter`: This query parameter can be used to filter the results by language or category. The value of this parameter must be one of the following:
  - `language`: This filter will return articles in the specified language.
  - `category`: This filter will return articles in the specified category.

## Examples

The following examples show how to use the API endpoints:

- To get the status of the application, you can use the following request:

GET /

```

* To get the configuration of the application, you can use the following request:

```

GET /config

- To get a list of articles, each with a list of its top keywords, you can use the following request:

GET /articles/top_keywords

```

* To get a dictionary of sentiment scores for each language, you can use the following request:

```

GET /articles/sentiment?filter_by=\<parameter\>

```

* To get a list of top headlines, you can use the following request:

```

GET /articles/headlines

```

* To get a list of articles from a specific category, you can use the following request:

```

GET /articles/categories?category=\<category\>
