# MCP POC - Complete Setup Guide

This is a proof-of-concept (POC) for a custom MCP (Model Context Protocol) server integrated with GitHub.

## 🚀 Quick Start

### 1. Local Testing

Test the MCP server locally:

```bash
cd mcp-server
pip install -r requirements.txt
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 server.py
```

Expected output:
```json
{"jsonrpc": "2.0", "id": 1, "result": {"tools": [{"name": "reverse_text", "description": "Reverses a string", "input_schema": {...}}]}}
```

### 2. Test the reverse_text Tool

```bash
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"reverse_text","arguments":{"text":"hello"}}}' | python3 server.py
```

Expected output:
```json
{"jsonrpc": "2.0", "id": 2, "result": {"text": "olleh"}}
```

### 3. Setup GitHub Pages Registry

- Create a new branch `gh-pages`
- Push the `registry/registry.json` to that branch
- Enable GitHub Pages in repository settings
- Access registry at: `https://<your-org>.github.io/mcp-poc/registry/registry.json`

### 4. Register in GitHub Organization

1. Go to GitHub Organization Settings
2. Navigate to **Code & Automation → MCP Registry URL**
3. Add: `https://<your-org>.github.io/mcp-poc/registry/registry.json`

### 5. Run GitHub Actions Workflow

Trigger the workflow manually:

```bash
gh workflow run mcp-test.yml
```

## 📋 Project Structure

```
mcp-poc/
 ├── registry/
 │    └── registry.json          # MCP registry configuration
 ├── mcp-server/
 │    ├── server.py              # Python MCP server implementation
 │    └── requirements.txt        # Python dependencies
 ├── workflows/
 │    └── mcp-test.yml           # GitHub Actions workflow
 └── README.md                   # This file
```

## ✅ Success Criteria

The POC is successful if:

1. ✅ GitHub recognizes your MCP server in the registry
2. ✅ `tools/list` returns the tool metadata
3. ✅ Running MCP inside GitHub Actions works
4. ✅ The registry is reachable via HTTPS
5. ✅ Copilot can call your tool (Beta feature)

## 📚 References

- [MCP Specification](https://modelcontextprotocol.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Setup](https://docs.github.com/en/pages)
