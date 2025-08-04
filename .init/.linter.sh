#!/bin/bash
cd /home/kavia/workspace/code-generation/event-engagement-management-service-20172/event_engagement_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

