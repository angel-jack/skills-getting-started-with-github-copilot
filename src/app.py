"""
High School Management System API

A super simple FastAPI application that allows students to view, sign up,
and unregister for extracurricular activities at Mergington High School.

Endpoints:
- GET /activities: List all activities and their details.
- POST /activities/{activity_name}/signup: Sign up a student for an activity.
- POST /activities/{activity_name}/unregister: Unregister a student from an activity.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Sports activities
    "Soccer Team": {
        "description": "Join the school soccer team and compete in local leagues",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly matches",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    # Intellectual activities
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Mondays, 4:00 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
    },
    "Science Club": {
        "description": "Explore science experiments and participate in science fairs",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["ethan@mergington.edu", "charlotte@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["jack@mergington.edu", "amelia@mergington.edu"]
    },
    # Arts activities
    "Art Club": {
        "description": "Explore different art techniques and create your own masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["grace@mergington.edu", "henry@mergington.edu"]
    },
    "Drama Society": {
        "description": "Participate in school plays and improve acting skills",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["ella@mergington.edu", "benjamin@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and showcase your work",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["zoe@mergington.edu", "leo@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    """Get all activities and their details."""
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """
    Sign up a student for an activity.

    Args:
        activity_name (str): The name of the activity.
        email (str): The student's email address.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If activity not found, already signed up, or full.
    """
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    # Prevent duplicate signups
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    # Prevent exceeding max participants
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.post("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """
    Unregister a student from an activity.

    Args:
        activity_name (str): The name of the activity.
        email (str): The student's email address.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If activity not found or student not registered.
    """
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    # Check if student is registered
    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Student not registered for this activity")
    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
