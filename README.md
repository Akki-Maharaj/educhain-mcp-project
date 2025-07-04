🚀 EduChain Claude Integration
✍️ AI Internship Assignment — Final Submission
This repository contains the full implementation for the AI Internship Assignment. It showcases how to generate educational content using EduChain, and how to prepare the system for future integration with Claude Desktop via MCP protocol.

🧠 TASK BREAKDOWN
✅ Task 1: EduChain Setup
📦 Installed EduChain SDK from satvik314/educhain

🧪 Used:

client.qna_engine.generate_questions(...) → 📘 Generate MCQs

client.content_engine.generate_lesson_plan(...) → 🗂️ Generate Lesson Plans

✅ Verified functionality by displaying and saving output.

🛠️ Task 2: Build MCP Server
🧰 Built an MCP server using fastmcp

🔧 Implemented two features:

Tool: generate_mcqs(topic: str, num: int)

Resource: lessonplan://{topic}

💾 Output is:

Printed in terminal

Saved in Sample_Response.txt

🛑 MCP server is initialized but not run (for Claude, see Task 3)

💬 Task 3: Claude Integration (Future-Ready)
🧱 MCP server initialized with FastMCP(name="EduChain Server")

🧠 You can register tools like this:

@mcp.tool, @mcp.resource, then call mcp.run()

🖥️ When ready, use this Claude config:

json
Copy
Edit
{
  "mcpServers": {
    "educhain": {
      "command": "python",
      "args": ["Task2_Build_MCP_Server.py"]
    }
  }
}
📁 FILE STRUCTURE
📄 File	📌 Description
Task2_Build_MCP_Server.py	✅ Main MCP-compatible EduChain script
Sample_Response.txt	📝 Output of generated MCQs and lesson plans
README.md	📚 This documentation
claude_desktop_config.json	⚙️ Not included — should be manually created for Claude

▶️ HOW TO RUN (Task 2)
💻 Install dependencies:
pip install educhain fastmcp

🚀 Run the script:
python Task2_Build_MCP_Server.py

📊 You’ll see:

MCQs printed to the terminal

Lesson plan printed below

Both results saved to Sample_Response.txt

📚 REFERENCES & CREDITS
🧠 EduChain SDK: https://github.com/satvik314/educhain

⚙️ FastMCP Docs: https://gofastmcp.com

🖥️ Claude Docs: https://docs.anthropic.com

📬 SUBMISSION INSTRUCTIONS
✔️ Make sure to include:

Task_Build_MCP_Server.py

Sample_Response.txt

README.md