# Google Calendar integration service
from __future__ import annotations
from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

READONLY = ["https://www.googleapis.com/auth/calendar.readonly"]
WRITE = ["https://www.googleapis.com/auth/calendar.events"]

TOKEN_PATH = Path("../google/token.json")
CREDS_PATH = Path("../google/client_secret.json")  # download from GCP console

def _ensure_creds(scopes):
    TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_PATH), scopes)
            creds = flow.run_local_server(port=8080, prompt="consent")
        TOKEN_PATH.write_text(creds.to_json())
    return creds

def calendar_service_readonly():
    creds = _ensure_creds(READONLY)
    return build("calendar", "v3", credentials=creds)

def calendar_service_write():
    creds = _ensure_creds(WRITE)
    return build("calendar", "v3", credentials=creds)

def ensure_sandbox_calendar(svc, name="Assistant — Sandbox"):
    # find or create
    cals = svc.calendarList().list().execute().get("items", [])
    for c in cals:
        if c.get("summary") == name:
            return c["id"]
    cal = svc.calendars().insert(body={"summary": name}).execute()
    # add to list so it shows up
    svc.calendarList().insert(body={"id": cal["id"]}).execute()
    return cal["id"]

def create_tagged_event(svc, calendar_id, title, start_iso, end_iso, plan_id, op_id):
    body = {
      "summary": title,
      "start": {"dateTime": start_iso, "timeZone": "Asia/Taipei"},
      "end":   {"dateTime": end_iso,   "timeZone": "Asia/Taipei"},
      "extendedProperties": {"private": {"assistant": "true", "plan_id": plan_id, "op_id": op_id}},
    }
    return svc.events().insert(calendarId=calendar_id, body=body).execute()
