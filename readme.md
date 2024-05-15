# Football Match Data API

This is a Flask API that provides information about football matches. The API reads data from a `match_data.json` file and dynamically updates when the file changes.

## Features
- For more information on how to obtain this data check this repo [url]
- Retrieve all live matches.
- Retrieve all upcoming matches.
- Retrieve all finished matches and their results.
- Retrieve live match details for a specific team.

## Prerequisites

- Python 3.11.4 (tested)
- requirements.txt

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MrSopia/livescore-scraper
    cd livescore-scraper
    ```

2. **Create a virtual environment (optional)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have a `match_data.json` file in the same directory as `app.py`**. Here’s an example `match_data.json`:

    ```json
    [
      {
        "home_team": "Lamia",
        "away_team": "Aris",
        "status": "Live",
        "time": "60'",
        "score": "Lamia 2 - 1 Aris"
      },
      {
        "home_team": "Olympiacos",
        "away_team": "AEK Athens",
        "status": "Upcoming 15 MAY 19:00",
        "start_time": "15 MAY"
      },
      {
        "home_team": "PAOK FC",
        "away_team": "Panathinaikos",
        "status": "Upcoming 15 MAY 19:00",
        "start_time": "15 MAY"
      },
      {
        "home_team": "PAOK FC",
        "away_team": "Olympiacos",
        "status": "Finished",
        "result": "PAOK FC 2 - 0 Olympiacos"
      },
      {
        "home_team": "Brighton",
        "away_team": "Chelsea",
        "status": "Upcoming 15 MAY 20:45",
        "start_time": "15 MAY"
      },
      {
        "home_team": "Manchester United",
        "away_team": "Newcastle United",
        "status": "Upcoming 15 MAY 21:00",
        "start_time": "15 MAY"
      },
      {
        "home_team": "Tottenham Hotspur",
        "away_team": "Manchester City",
        "status": "Finished",
        "result": "Tottenham Hotspur 0 - 2 Manchester City"
      }
    ]
    ```

## Running the API

To run the API, use the following command:

```bash
python flask_api.py
```

The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Get All Live Matches

- **URL**: `/api/live`
- **Method**: `GET`
- **Description**: Returns all live matches.

**Example Request**:

``` bash
curl http://127.0.0.1:5000/api/live
```

### Get All Upcoming Matches

- **URL**: `/api/upcoming`
- **Method**: `GET`
- **Description**: Returns all upcoming matches.

**Example Request**:

``` bash
curl http://127.0.0.1:5000/api/upcoming
```

### Get All Finished Matches

- **URL**: `/api/finished`
- **Method**: `GET`
- **Description**: Returns all finished matches with results.

**Example Request**:

``` bash
curl http://127.0.0.1:5000/api/finished
```

### Get Live Match by Team Name

- **URL**: `/api/match`
- **Method**: `GET`
- **Description**: Returns live match details for a given team name.
- **Query Parameter**:
  - `team`: The name of the team (home or away).

**Example Request**:

``` bash
curl http://127.0.0.1:5000/api/match?team=Lamia
```

## Dynamic Data Reloading

The API uses the `watchdog` library to monitor changes in the `match_data.json` file. Whenever the file is modified, the data is reloaded automatically, ensuring the API serves the most recent information.

## License

This project is licensed under the MIT License.
