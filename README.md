# Parsley

![Parsley logo and stylized description.](http://i.imgur.com/LFYhXal.png)

This tool accepts a list of URL's from a file, downloads each one, parses, and
converts the HTML to JSON format.

## Run it yourself

Clone this repo and install its dependencies;

Run `python main.py` with no args to test it;

It will download the content three URLs listed on the [sample-links.txt](https://github.com/cardoso-neto/Parsley/blob/master/sample-links.txt) file;

A JSON for each URL will be saved on the `./data/` folder with a sanitized version of URL as its filename.

## Example

Original HTML:

```html
<title>Buy Historical Stock Market Analytics JSON API | Stock Data API</title>
<meta name="description" content="Historical stock data JSON REST API for financial market data. Includes over
6,000 companies and more than 50 advanced technical indicators.">
```

Parsed JSON:

```json
{
  "tags": [
    {
      "attributes": null,
      "content": "Buy Historical Stock Market Analytics JSON API | Stock Data API",
      "name": "title"
    },
    {
      "attributes": {
        "content": "Historical stock data JSON REST API for financial market data. Includes over 6,000 companies
         and more than 50 advanced technical indicators.",
        "name": "description"
      },
      "content": null,
      "name": "meta"
    }
  ]
}
```

## Args

```
usage: main.py [-h] [--input INPUT] [--output_dir OUTPUT_DIR]
               [--workers WORKERS]

Gets a list of URLs and converts the HTML to JSON.

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Input file
  --output_dir OUTPUT_DIR
                        Output directory
  --workers WORKERS     Number of threads
```
