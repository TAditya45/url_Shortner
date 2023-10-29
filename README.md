# URL Shortener 

This is a simple URL shortener service built with Python and Flask.


## Features

- Create short URLs for long links.
- Search for URLs based on a keyword in their titles.
- Retrieve metadata for a short URL.
- Redirect short URLs to their original long URLs.

## Prerequisites

- Python 3
- Flask

## Installation

1. Clone this repository to your local machine.
2. Install Flask (https://flask.palletsprojects.com/en/3.0.x/installation/)

## Usage

1. Start the Flask application using below Command 
   
   python url_shortener.py

2.The service will be accessible at http://localhost:5000

3.Endpoints

  	Create Short URL: POST /shorten
  
  	Search for URLs: GET /search?term=<search_term>
  
  	Retrieve Metadata: GET /metadata/<short_url>
  
  	Redirect to Long URL: GET /<short_url>
