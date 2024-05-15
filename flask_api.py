import time
import json
from flask import Flask, request, jsonify
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)

match_data = []

class FileWatcher(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_data()
        
    def on_modified(self, event):
        if event.src_path.endswith(self.file_path):
            self.load_data()

    def load_data(self):
        global match_data
        try:
            with open(self.file_path, 'r') as f:
                match_data = json.load(f)
            print(f"Data reloaded from {self.file_path}")
        except Exception as e:
            print(f"Failed to load data from {self.file_path}: {e}")

def start_file_watcher(file_path):
    event_handler = FileWatcher(file_path)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    return observer

@app.route('/api/live', methods=['GET'])
def get_live_matches():
    live_matches = [match for match in match_data if match.get('status') == 'Live']
    return jsonify(live_matches), 200

@app.route('/api/upcoming', methods=['GET'])
def get_upcoming_matches():
    upcoming_matches = [match for match in match_data if 'Upcoming' in match.get('status', '')]
    return jsonify(upcoming_matches), 200

@app.route('/api/finished', methods=['GET'])
def get_finished_matches():
    finished_matches = [match for match in match_data if match.get('status') == 'Finished']
    return jsonify(finished_matches), 200

@app.route('/api/match', methods=['GET'])
def get_match_by_team():
    team_name = request.args.get('team')
    if not team_name:
        return jsonify({"error": "No team name provided"}), 400

    matches = [match for match in match_data if match.get('home_team') == team_name or match.get('away_team') == team_name]
    live_matches = [match for match in matches if match.get('status') == 'Live']

    if not live_matches:
        return jsonify({"message": "No live matches found for the given team"}), 404

    return jsonify(live_matches), 200

if __name__ == '__main__':
    json_file_path = 'match_data.json'
    observer = start_file_watcher(json_file_path)
    try:
        app.run(debug=True, use_reloader=False)
    finally:
        observer.stop()
        observer.join()
