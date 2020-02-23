# webcrawler_assignment

This project fetches the now showing movies from bookmyshow.in

### Getting Started

create a virtual enviroment by executing python -m venv venv
initialize the virtual environment using .\venv\Scripts\activate.bat on windows
install scrapy library using the following command pip install scrapy

### Running the application
cd bookmyshow
scrapy crawl bookmyshow

### Test
A SQLite database with the name "bookmyshows.db" is created and the dtabase contains shows_tb table which includes the scapped data.

### For the below questions please do not code this, put your answer in the README for this
1. Can this crawler be made more generic?. Please extend the code above to incorporate this.
I tried but could not find a methodology that logically generalizes the present code.
2. Are there any sites you cannot crawl?
I was not able to crawl sites with subscription popup and dynamically updating sites on scroll
3. How would you scale this crawler so it can crawl millions of website?
I learnt that we can upload the site using 1) scrapyd 2) scrapycloud we can deploy the application and get an api.
using kubernetes we can scale the docarized application container deployed.
4. How would you store all the different data?
here in this exaple I have used sqlite, in case of production data, I will go with mongodb for insertion of data, since it is schemaless, it will be much suitable to store the scraped data.
5. Explain the architecture and design of the system. Draw a simple diagram of time permits
This application works on the basis of scrapy framework architecture
req ---> scrapy core ---> scheduler ---> scrapy core ---> downloader ---> scapy core ---> pipeline
6. Explain the data model
I have stored a 4 fileds from the ruuning shows data availble on bookmyshow with the following fields 1) title 2)language 3) genre 
4)url in the table shows_tb
7. Design patterns used
The code works on the basis of scrapy framework which is an asynchronous non blocking event driven architecture.
