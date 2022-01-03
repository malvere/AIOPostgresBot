# AIOP Bot
- **A**ll
- **I**n
- **O**ne
- **P**ostgreSQL
- **Bot**  

Telegram Bot that parses any desired instagram user Id's using Requests and inserts them to PostgreSQL DataBase.
## Background
According to CNBC there are more than 2 Billion active Instagram users worldwide. Thats a lot. Because of that, things get tricky when it comes to creating a new account with a neat, short name for your brand new instagram account. There are **1679616** possible combinations of usernames, which consist of letters and numbers. When compared to 2 Billions, it’s just 0.08%. Even every possible combination of 5 symbols (60466176 if letters and numbers are used)is just 3.02%. But there are still might be some 4 and 5 symbol usernames left. In order to help with parsing of 60466176 potential usernames, AIOPostgresBot was made.
## Features
- Controls and notifications in Telegram via AIOGram
- Lightweight due to use of Requests library
- PostgreSQL to handle big amount of usernames
- Built in dictionary generation function with the ability to handle user input
- Cloud-Ready
## Notes 
User input currently only works via CLI.  
In order to retrieve appropriate JSON from Instagram API private IP or proxy should be used. Cloud Platforms such as Heroku provide Enterprise IP by default, which is blocked by Instagram (Redirect to login page). Implementing Instagram Private API could also be a solution.
