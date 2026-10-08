@echo off

start cmd /k "cd /d C:\CERT-AI-Platform\services\lanl-parser && uvicorn main:app --reload --port 8006"

start cmd /k "cd /d C:\CERT-AI-Platform\services\detection-engine && uvicorn main:app --reload --port 8007"

start cmd /k "cd /d C:\CERT-AI-Platform\services\incident-manager && uvicorn main:app --reload --port 8008"

start cmd /k "cd /d C:\CERT-AI-Platform\services\soar-engine && uvicorn main:app --reload --port 8009"

start cmd /k "cd /d C:\CERT-AI-Platform\services\playbook-engine && uvicorn main:app --reload --port 8010"

start cmd /k "cd /d C:\CERT-AI-Platform\services\mitre-mapper && uvicorn main:app --reload --port 8011"