# Agentic AI Project

An Agentic AI system built with Python that combines **autonomous agents**, **memory**, and **tool usage** to solve complex tasks.

## Features

- Multi-agent architecture
- Task planning and execution
- Memory management (short-term + long-term)
- Tool integration
- Output logging and result storage
- Modular and extensible design

## Project Structure

```bash
agentic-ai-project/
│
├── agents/           # Agent definitions and orchestration logic
├── memory/           # Memory modules and retrieval logic
├── saved_outputs/    # Logs, responses, and generated outputs
├── tools/            # External tools the agents can use
├── utils/            # Helper utilities, prompts, configs
│
├── app.py            # Main entry point
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── .env              # Environment variables (not committed)
└── .env.example      # Example environment configuration
