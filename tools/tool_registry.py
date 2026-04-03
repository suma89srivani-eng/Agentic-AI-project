import os

def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"


def save_output_tool(text, filename="output.txt"):
    os.makedirs("saved_outputs", exist_ok=True)
    file_path = os.path.join("saved_outputs", filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

    return f"Output saved successfully to {file_path}"


TOOLS = {
    "calculator": calculator_tool,
    "save_output": save_output_tool
}
