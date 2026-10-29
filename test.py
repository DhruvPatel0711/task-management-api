import requests

TIMEOUT = 10

BASE_URL = "http://127.0.0.1:8000"

USERNAME = "testadmin"
PASSWORD = "Admin@123"

headers = {}


def check(response, expected):
    print(
        f"{response.request.method} "
        f"{response.request.url} "
        f"-> {response.status_code}",
        flush=True
    )

    if response.status_code != expected:
        print(response.text)

    assert response.status_code == expected


# -------------------------
# AUTH
# -------------------------

def test_login():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": USERNAME,
            "password": PASSWORD
        }, timeout=TIMEOUT
    )

    check(response, 200)

    token = response.json()["access_token"]

    headers["Authorization"] = f"Bearer {token}"

    print("Login successful")


def test_me():
    response = requests.get(
        f"{BASE_URL}/auth/me",
        headers=headers
    )

    check(response, 200)

    print("Current user:", response.json())


# -------------------------
# USER
# -------------------------

def test_create_user():
    response = requests.post(
        f"{BASE_URL}/users/",
        headers=headers,
        json={
            "username": "testuser2",
            "password": "User1234"
        }
    )

    check(response, 200)

    user = response.json()

    print("Created user:", user)

    return user["id"]


def test_delete_user(user_id):
    response = requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers=headers
    )

    check(response, 200)

    print(response.json())


def test_restore_user(user_id):
    response = requests.patch(
        f"{BASE_URL}/users/{user_id}/restore",
        headers=headers
    )

    check(response, 200)

    print("Restored user:", response.json())


# -------------------------
# TASK
# -------------------------

def test_create_task():
    response = requests.post(
        f"{BASE_URL}/tasks/",
        headers=headers,
        json={
            "title": "Test Task",
            "desc": "Created by test.py",
            "category": "Testing",
            "priority": "routine",
            "deadline": "2026-12-31T23:59:59"
        }
    )

    check(response, 200)

    task = response.json()

    print("Created task:", task)

    return task["id"]


def test_get_tasks():
    response = requests.get(
        f"{BASE_URL}/tasks/",
        headers=headers
    )

    check(response, 200)

    print("Tasks:", response.json())


def test_get_task(task_id):
    response = requests.get(
        f"{BASE_URL}/tasks/{task_id}",
        headers=headers
    )

    check(response, 200)

    print("Task:", response.json())


def test_update_task(task_id):
    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        headers=headers,
        json={
            "title": "Updated Test Task",
            "desc": "Updated by test.py",
            "category": "Testing",
            "priority": "elevated",
            "deadline": "2027-01-31T23:59:59"
        }
    )

    check(response, 200)

    print("Updated task:", response.json())


def test_delete_task(task_id):
    response = requests.delete(
        f"{BASE_URL}/tasks/{task_id}",
        headers=headers
    )

    check(response, 200)

    print(response.json())


def test_restore_task(task_id):
    response = requests.patch(
        f"{BASE_URL}/tasks/{task_id}/restore",
        headers=headers
    )

    check(response, 200)

    print("Restored task:", response.json())


# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":

    test_login()

    test_me()

    user_id = test_create_user()

    task_id = test_create_task()

    test_get_tasks()
    test_get_task(task_id)
    test_update_task(task_id)
    test_delete_task(task_id)
    test_restore_task(task_id)

    test_delete_user(user_id)
    test_restore_user(user_id)

    print("\n======================")
    print("ALL TESTS PASSED")
    print("======================")