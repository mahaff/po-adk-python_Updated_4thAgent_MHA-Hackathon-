"""
healthcare_agent — A2A application entry point.

Start the server with:
    uvicorn healthcare_agent.app:a2a_app --host 0.0.0.0 --port 8001

The agent card is served publicly at:
    GET http://localhost:8001/.well-known/agent-card.json

All other endpoints require an X-API-Key header (see shared/middleware.py).
"""
import os

from a2a.types import AgentSkill
from shared.app_factory import create_a2a_app

from .agent import root_agent

a2a_app = create_a2a_app(
    agent=root_agent,
    name="healthcare_fhir_agent",
    description=(
        "A hospital readmission risk assessment agent that analyzes patient "
        "summaries and predicts 30-day readmission risk."
    ),
    url=os.getenv("HEALTHCARE_AGENT_URL", os.getenv("BASE_URL", "http://localhost:8001")),
    port=8001,
    skills=[
        AgentSkill(
            id="readmission-risk",
            name="readmission-risk",
            description="Analyze patient summaries and estimate 30-day readmission risk.",
            tags=["readmission", "risk", "text"],
        ),
    ],
)
