from educhain import Educhain
from fastmcp import FastMCP

client = Educhain()
mcp = FastMCP(name="EduChain Server")

# === Internal logic (shared) ===

def _generate_mcqs(topic: str, num: int) -> str:
    result = client.qna_engine.generate_questions(
        topic=topic,
        num=num,
        question_type="Multiple Choice"
    )
    return result.model_dump_json()

def _get_lesson_plan(topic: str) -> str:
    plan = client.content_engine.generate_lesson_plan(topic=topic)
    return plan.model_dump_json()

# === MCP Tools & Resources ===

@mcp.tool
def generate_mcqs(topic: str, num: int) -> str:
    return _generate_mcqs(topic, num)

@mcp.resource("lessonplan://{topic}")
def get_lesson_plan(topic: str) -> str:
    return _get_lesson_plan(topic)

# === Local testing ===

def test_generate_mcqs():
    print("Testing MCQ Generator:")
    print(_generate_mcqs("Python loops", 3))

def test_get_lesson_plan():
    print("Testing Lesson Plan:")
    print(_get_lesson_plan("algebra"))

# === MCP STDIO Launch ===

if __name__ == "__main__":
    test_generate_mcqs()
    test_get_lesson_plan()
    print("Starting STDIO MCP server...")
    mcp.run()