# PHASE-3-WK3-CodeChallenge
Authour:**Brian Mwangi Maina**

## Prequisites:

**Technologies Used**

<li>Python
<li>SQLAlchemy

**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine:git clone git@github.com:BrwnBoy/PHASE-3-WK3-CodeChallenge.git//
<li>cd into *PHASE-3-WK3-CodeChallenge*
<li>Finally, open up vs.code by typing in (code .) while in the repository.

### What Goes Into Making The Programs Run:

(1)**Importing of necessary modules**:*At the beginning of each script, I imported all the necessary modules, which typically included sqlalchemy and my own modules where I defined my SQLAlchemy models.*

(2)**Setting up of engines & sessions**:*SQLAlchemy uses an engine to interact with databases, and a session to manage all the operations.They are needed so that the user can work  with models.*
 
(3)**Use of Models**:*Models can be used to query the database, create new records, and so on.* *Here's an example*:
**creating a new restaurant**
new_restaurant = Restaurant(name='Test Restaurant', price=50)
session.add(new_restaurant)
session.commit()
**querying restaurants**
restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(restaurant.name)

(4)**Closing of the Session**:*Closing of the session is quite important, since when done it tends ro free up resources.* *Example*:**session.close()**

(5)**Finally, run the script**:*You can the script from the command line using the python command followed by the name of the script.* *Example*:**python3 review.py**

#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

##### Extras
(*Link to my domain design plan*:https://jamboard.google.com/d/1BihiDztKh6UHSIKWHWTXA3GPtVmvwu1loaZ_L1Pkt48/edit?usp=sharing)
