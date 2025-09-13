## MCP Python SDK demo

### Prerequisites

- Python 3.13+
- Virtualenv activated: `source /workspace/.venv/bin/activate`

### Install

```bash
pip install -r /workspace/requirements.txt
```

### Run the demo

```bash
python /workspace/mcp_demo/client.py
```

What it does:
- Spawns a stdio MCP server (`server.py`)
- Initializes the client session
- Lists tools and calls the `echo` tool

