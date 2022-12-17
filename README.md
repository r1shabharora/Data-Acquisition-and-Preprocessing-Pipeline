# Data-Acquisition-and-Preprocessing-Pipeline - Created by RISHABH ARORA
In this code, Rishabh has created a datapipeline to fetch Stock quotes and other financial data from Yahoo Finance.
Gathering data from one source, formatting/cleansing (as required) and then loading it into a database.

STAGE-ONE (GETTING DATA)
Below is the example of the URL that has been used in this project:
https://finance.yahoo.com/most-active?offset=0&count=100
Now, the number at the end of the URL can always be changed based on user's requirements. But, for this project data for 100 top most active stocks will be fetched.

Usually 'Yahoo Finance!' website is quite stable but in case the website response is not ok(i.e. not 200) then this program will auto-quit/exit due to a build in if/else condition that will only allow further processing if response code is 200.

try and except method is also implemented to deal with unexpected errors and making the whole data pipeline program stable and reliable.

At the start of the program, system time is captued so that in the end total elapsed time can be calculated.

For the input, the URL has to be provided and then using beautiful soup stock data will be fetched in a dataframe.
A loop executes the number of times it finds a particular element i.e the rows in which stock data is visible on website. This row has multiple elements depending on what information is being displayed for example: Ticker symbol, Stock price, company name, etc. and appropriate element is called using select command and then using get_text() the text value or the stock information is fetched.
All information is fetched in a dictionary and appropriate keys are predefined in it, each iteration of loop will append dictionary data to the dataframe that was created in the beginning of the program.

Stock data can be utilized for analysis and stoage purpose to track changes from time to time.
Data is stored in a database and MongoDB is used as the database provider.

Raw data cannot be loaded directly into the database so cleansing is required. The stock price came as string which was converted to integer. Values in 'Average volume' was also converted using a custom function. This custom function transformed the values that were earlier denoted as '3M' and were convertedninto actual figures as '3000000'. This was done so that further analysis can be performed in future on this data.

An additional feature 'CAPTURED DATE' was built in the dictionary because each time this program runs, it appends data into the database and by collecting data in time-series, this whole database will become more and more valuable. Example: time-series analysis can be performed, stock prediction can be performed using machine learning algorithms, etc.

Some commands like .describe(),.head() and .info() are used to know our dataframe post cleaning. Maximum and minimum stock price with company name is also fetched to see current load's lowest and top stock price companies.

STAGE TWO (LOADING DATA INTO DATABASE)
In MongoDB, records are also known as documents.
Data is stored in a dataframe. This data is converted into a dictionary and then using pymongo library, entire dataframe has been loaded into database.
While connecting to database, urllib package is used and by parsing credential values using quote_plus, proper URL encoding and secure transmission is ensured.
Post successful connection, some sample database names are printed to further ensure that our connection is 100% stable.
Stock data is stored in 'stock_db' database and stored in 'stock_collection' collection of the database.
There is also a 5 second delay added after load database command, this was done to provide proper time for the command to execute and load data into the database.

STAGE THREE (FINAL)
Once the data is loaded into the database, a print command informs the user about number of records that were loaded into the database and the current number of records/documents that are part of the database.
In the end, user is also notified as three beep sounds are played followed by the print command that will display time taken for this program to run.

Thank you for reading this.
