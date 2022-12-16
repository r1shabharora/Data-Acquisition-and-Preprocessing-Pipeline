# Data-Acquisition-and-Preprocessing-Pipeline - Created by RISHABH ARORA
In this code, Rishabh has created a datapipeline to fetch Stock quotes and other financial data from Yahoo Finance.
Gathering data from one source, formatting/cleansing (as required) and then loading it into a database.

STAGE-ONE (GETTING DATA)
Below is the example of the URL that has been used in this project:
https://finance.yahoo.com/most-active?offset=0&count=100
Now, the number in the end of the URL can always be changed based on user's requirements. But, for this project data for 100 top most active stocks will be fetched.

Usually 'Yahoo Finance!' website is quite stable but in case the website response is not ok(200) then this program will auto-quit/exit due to a build in if/else condition that will only allow further processing if response code is 200.
try and except method is also implemented to deal with unexpected errors and making the whole data pipeline program stable and reliable.

At the start of the program, system time is captued so that in the end total elapsed time can be calculated.

For the input, the URL has to be provided and then using beautiful soup stock data will be fetched in a dataframe.
Stock data can be utilized for analysis and stoage purpose to track changes from time to time.
Data is stored in a database and MongoDB is used as the database provider.

Raw data cannot be loaded directly into the database so cleansing is required. The stock price came as string which was converted to integer. Values in 'Average volume' was also converted using a custom function. This custom function transformed the values that were denoted as 3M to 3000000. This was done so that further analysis can be performed in future on this data.

Also, a 'CAPTURED DATE' column was created in the dataframe because each time this program runs, it appends data into the database and by collecting data in time-series, this whole database will become more and more valuable. Example: time-series analysis can be performed, stock prediction can be performed using machine learning algorithms, etc.


STAGE TWO (LOADING DATA INTO DATABASE)
In MongoDB, records are also known as documents.
Data is stored in a dataframe. This data is converted into a dictionary and then using pymongo library, entire dataframe has been loaded into database.

STAGE THREE (FINAL)
Once the data is loaded into the database, the user is notified as three beep sounds are played followed by the print command that will display time taken for this program to run.

Thank you for reading this.
