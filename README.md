## MCP Client & Server Sample

## Setup (Linux)

```sh
python3 -m venv venv
source venv/bin/activate

# -----------------------------
# Start the MCP Server fisrt
# -----------------------------
python3 mcp_server.py

# -----------------------------
# Test the MCP client
# -----------------------------
python3 mcp_client.py

# -----------------------------
# Test the agent
# The OPEN_API_KEY environment variable must be set either via .env file or export
# -----------------------------

export OPENAI_API_KEY=sk-proj-IA_xxxxxxxXXXXXXxxxxxXXXXXxxxxXXXXX

python3 agent.py
```