# salesken_assignement
It compares each string and trying to find out the similarity with each string

### Steps to follow to run the application

##### Step 1 : Install the requirement.txt file

##### Step 2 : Run app.py

##### Now application is running on http://localhost:5000

##### Step 3 : Open the Postman and use the "POST" API

http://localhost:5000/calculate_vector

in Body pass paramter strings

key  :   strings 

value      "we are sorry for the inconvenience",
              "we are sorry for the delay",
              "we regret for your inconvenience",
              "we don't deliver to baner region in pune",
              "we will get you the best possible rate"

##### Response for above example

[['1.0000002', '0.8742637', '0.80048907', '0.23807865', '0.4646978'], ['0.8742637', '1.', '0.605015', '0.25081366', '0.4493389'], ['0.80048907', '0.605015', '1.', '0.17848739', '0.41954646'], ['0.23807865', '0.25081366', '0.17848739', '1.', '0.249558'], ['0.4646978', '0.4493389', '0.41954646', '0.249558', '1.']]

