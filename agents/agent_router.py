from tools.tool_registry import TOOLS
from agents.base_agent import BaseAgent

class AgentRouter:
    def __init__(self, memory):
        self.agent = BaseAgent(memory)

    def route(self, user_input):
        user_input_lower = user_input.lower()

        # Calculator Tool
        if "calculate" in user_input_lower:
            expression = user_input_lower.replace("calculate", "").strip()
            return TOOLS["calculator"](expression)

        # Save Output Tool
        elif "save this" in user_input_lower:
            content = user_input.replace("save this", "").strip()
            return TOOLS["save_output"](content)

        # Default AI Agent
        else:
            return self.agent.think(user_input)
