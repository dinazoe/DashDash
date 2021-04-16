# DashDash
Dashboard of movies scrapped from rottentomatoes, metacritic, imdb. Uses flask as web engine. Uses requests and BeautifulSoup to scrape the data.

# Installation instructions.
- Run command below to install the virtual environment package:
    '''
    pip3 install virtualenv
    '''

- Run the command to initiate a virtual environment
    '''
    virtualenv DashboardTest
    '''
- Run the command below as an admin to let the activate powershell script Run
    set-executionpolicy remotesigned

- Run the command to activate the virtual environment
    '''
    .\DashboardTest\Scripts\activate
    '''
- Run command below to install flask and sql alchemy:
    pip3 install flask flask-sqlalchemy

- To use the scraper
    '''
    pip3 install requests beautifulsoup4
    '''