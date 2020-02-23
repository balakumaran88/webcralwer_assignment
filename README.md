# webcrawler_assignment

This project fetches the now showing movies from bookmyshow.in

### Getting Started

create a virtual enviroment by executing python -m venv venv
initialize the virtual environment using .\venv\Scripts\activate.bat on windows
install scrapy library using the following command pip install scrapy

### Running the application
scrapy crawl bookmyshow

###Test
A SQLite database with the name "bookmyshows.db" is created and the dtabase contains shows_tb table which includes the scapped data.
