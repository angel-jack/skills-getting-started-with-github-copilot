# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey angel-jack!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/angel-jack/skills-getting-started-with-github-copilot/issues/1)

---

# Mergington High School Activities API

A FastAPI application for managing extracurricular activities at Mergington High School.

## Features

- View all available activities and their details
- Sign up for an activity (with participant limits)
- Unregister from an activity

## API Endpoints

- `GET /activities`  
  Returns all activities and their details.

- `POST /activities/{activity_name}/signup?email=student@mergington.edu`  
  Sign up a student for an activity.

- `POST /activities/{activity_name}/unregister?email=student@mergington.edu`  
  Unregister a student from an activity.

## Running Locally

```bash
pip install fastapi uvicorn
uvicorn src.app:app --reload
```

## Running Tests

```bash
pip install pytest httpx
pytest
```

## Frontend

Open `src/static/index.html` in your browser for a simple UI.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

