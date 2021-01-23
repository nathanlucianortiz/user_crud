import requests
from pprint import pprint


def test_scan():
    resp = requests.get("http://127.0.0.1:5000/users")
    pprint(resp.json())


def test_read():
    resp = requests.get("http://127.0.0.1:5000/users/1")
    pprint(resp.json())


def test_create():
    sample = {"first_name": "Nathan", "last_name": "Ortiz", "job_title": "Crew member"}
    resp = requests.post("http://127.0.0.1:5000/users", json=sample)
    pprint(resp.json())


def test_update():
    sample = {"first_name": "Mary", "last_name": "Anne", "job_title": "Crew member"}
    resp = requests.put("http://127.0.0.1:5000/users/2", json=sample)

if __name__ == "__main__":
    test_scan()
    test_read()
    test_create()
    test_update()