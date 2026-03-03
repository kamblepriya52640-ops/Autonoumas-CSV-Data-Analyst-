# Autonomous CSV Data Analyst

This project uses LangChain's Pandas DataFrame Agent to perform natural language analysis on CSV data, integrated into a Django web application.

## Project Implementation Roadmap

This project follows a structured 4-week development cycle focused on building, securing, and refining the Pandas Agent.

## Week 1: The Pandas Agent (Foundation)

Goal: Establish the core data processing engine.

Tasks: Set up the LangChain Pandas Dataframe Agent and load sample CSV data.

Validation: Verify that basic data queries (e.g., calculating means, counting rows) match manual Pandas execution.

## Week 2: Graphing Capability (Visualization)

Goal: Enable visual data representation.

Tasks: Integrate matplotlib via prompt engineering. Implement logic to capture, store (.png), and return URLs for generated charts.

Validation: Test complex visualization requests, such as 3-month rolling averages of sales data.

## Week 3: Safety & Sandboxing (Security)

Goal: Secure the execution environment.

Tasks: Implement sandboxing mechanisms to restrict library access and isolate the file system.

Validation: Conduct security audits and attempt Prompt Injection attacks (e.g., unauthorized file deletion) to ensure system integrity.

## Week 4: UI & Persistence (Finalization)

Goal: Improve user experience and reliability.

Tasks: Implement real-time streaming of the agent’s "Thought Process" (intermediate steps) to the UI.

Validation: Perform comprehensive end-to-end testing and final polishing of the system.
