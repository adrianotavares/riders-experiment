# Riders Experiment

RESTful API to search riders

**User Story:**

As a user, 
I want to search for riders (motorcyclists) by city 
so that I can easily locate friends in each city.

**Acceptance Criteria:**

* The API should accept the city name as a parameter.
* The API should return a JSON with the following fields for each rider found:
    * id
    * name
    * city
    * latitude
    * longitude
    * brand
    * model
    * status (true or false)

**Endpoint:**

```
GET /riders?city={city_name}
```

```json
[
  {
    "id": 1,
    "name": "João",
    "city": "São Paulo",
    "latitude": -23.55052,
    "longitude": -46.633309,
    "motorcycle_brand": "Honda",
    "motorcycle_model": "CG 160",
    "status": true
  },
  {
    "id": 2,
    "name": "Maria",
    "city": "Rio de Janeiro",
    "latitude": -22.906846,
    "longitude": -43.172896,
    "motorcycle_brand": "Yamaha",
    "motorcycle_model": "Fazer 250",
    "status": false
  }
]
```

To run the file riders.py, you can follow these steps:

1. Open a terminal or command prompt: Navigate to the directory where the file riders.py is saved using the cd command.
2. Create a virtual environment (optional): It is recommended to create a virtual environment to isolate the code and project dependencies. You can create a virtual environment using the command python3 -m venv venv (on Linux or macOS) or py -3 -m venv venv (on Windows).
3. Activate the virtual environment (optional): After creating the virtual environment, you need to activate it. On Linux or macOS, use the command source venv/bin/activate. On Windows, use the command venv\Scripts\activate.
4. Install dependencies: The file riders.py depends on Flask and the json module. Install these dependencies using the command pip install flask and pip install json.
5. Run the application: Run the file riders.py using the command python3 riders.py.
6. Test the API: Once the application is running, you can test the API by accessing the following URL in a web browser:

```
http://127.0.0.1:5000/riders?city=São Paulo
http://127.0.0.1:5000/riders?city=ALL
```

This will return a list of motorcyclists located in São Paulo. You can replace "São Paulo" with the name of any other city to filter motorcyclists by city.

Note: Make sure the file riders.json is in the same directory as the file riders.py.

**Running Tests**

```python
if __name__ == '__main__':
    unittest.main()
```

How to run the tests:

* Save the code above in a file called test_riders.py in the same directory as the file riders.py.
* Open a terminal or command prompt and navigate to the directory where the files are saved.
* Run the following command:

```console
python3 test_riders.py
```

The tests will run and the results will be displayed in the terminal.
