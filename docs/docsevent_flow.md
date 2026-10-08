\# Event Flow



1\. Sysmon generates event



2\. Fluent Bit collects event



3\. Event sent to Kafka



Topic:

raw-sysmon



4\. OCSF Normalizer converts event



Topic:

normalized-events



5\. Enrichment Engine adds:



\- Asset information

\- User information

\- Threat intelligence



Topic:

enriched-events



6\. Detection Engine evaluates:



\- Sigma Rules

\- Custom Rules

\- ML Models



Topic:

detections



7\. Correlation Engine groups alerts



Topic:

incidents



8\. Incident Manager stores incident



9\. AI Triage analyzes incident



10\. AI Investigator builds timeline



11\. AI Reporter creates report



12\. SOAR executes playbook



13\. Analyst approves action

