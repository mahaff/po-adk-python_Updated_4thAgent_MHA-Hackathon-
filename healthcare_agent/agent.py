"""
healthcare_agent — Text-only readmission risk agent.

This agent intentionally does not depend on FHIR metadata or external tools.
It classifies risk from the patient text supplied in the incoming message.

To customise:
  • Change model, description, and instruction below.
  • Keep tools=[] unless you explicitly add a new text-safe capability.
"""
import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# ── Model selection ────────────────────────────────────────────────────────────
# Set HEALTHCARE_AGENT_MODEL in your .env to switch models.
#
# All models are handled via LiteLLM. Use the appropriate prefix:
#   HEALTHCARE_AGENT_MODEL=gemini/gemini-2.5-flash   (Google AI Studio, default)
#   HEALTHCARE_AGENT_MODEL=openai/gpt-4o
#   HEALTHCARE_AGENT_MODEL=anthropic/claude-sonnet-4-6
#   HEALTHCARE_AGENT_MODEL=vertex_ai/gemini-2.5-flash
# ──────────────────────────────────────────────────────────────────────────────
_model_name = os.getenv("HEALTHCARE_AGENT_MODEL", "gemini/gemini-2.5-flash")
_model = LiteLlm(model=_model_name, max_retries=3, retry_delay=2.0)

root_agent = Agent(
    name="healthcare_fhir_agent",
    model=_model,
    description=(
        "A hospital readmission risk assessment agent that analyzes patient "
        "summaries and predicts 30-day readmission risk."
    ),
    instruction=(
        "You are a hospital readmission risk AI. "
        "You analyze ONLY the patient text provided in the message. "
        "Do NOT require FHIR, metadata, or external context. "
        "Return HIGH, MEDIUM, or LOW risk with a short explanation. "
        "Do not invent missing clinical details."
    ),
    tools=[],
)
