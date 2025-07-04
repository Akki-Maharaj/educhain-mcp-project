from educhain import Educhain
from fastmcp import FastMCP

# Initialize EduChain client
client = Educhain()

# Initialize MCP server for future integration with Claude (not used in Task 2)
mcp = FastMCP(name="EduChain Server")

# Function to generate MCQs using EduChain
def generate_mcqs(topic: str, num: int) -> str:
    result = client.qna_engine.generate_questions(
        topic=topic,
        num=num,
        question_type="Multiple Choice"
    )
    output = result.model_dump_json()

    print(f"\nMCQs on {topic}:\n")
    print(output.encode('utf-8', errors='ignore').decode())

    with open("Sample_Response.txt", "w", encoding="utf-8") as f:
        f.write(f"MCQs on {topic}:\n\n{output}\n")

    return output


# Function to generate lesson plans using EduChain
def get_lesson_plan(topic: str) -> str:
    plan = client.content_engine.generate_lesson_plan(topic=topic)
    output = plan.model_dump_json()

    print(f"\nLesson Plan for {topic}:\n")
    print(output.encode('utf-8', errors='ignore').decode())

    with open("Sample_Response.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nLesson Plan for {topic}:\n\n{output}\n")

    return output


if __name__ == "__main__":
    # Run sample tool calls for Task 2 demonstration (no Claude required)
    generate_mcqs("Python loops", 3)
    get_lesson_plan("algebra")

    # Note: The MCP server is initialized above
    # If you want to expose this to Claude in Task 3, you can register tools and call:
    # mcp.run()
