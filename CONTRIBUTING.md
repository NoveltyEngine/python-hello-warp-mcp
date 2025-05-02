# Contributing to Hello World MCP Server

Thank you for your interest in contributing to the Hello World MCP Server project! This simple project aims to provide a reference implementation for MCP (Machine Conversational Protocol) servers that can be used with Warp Terminal.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/hello_world_mcp.git`
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev]"  # Or: pip install -e ".[dev]"
   ```

## Making Changes

1. Create a new branch for your feature or bugfix: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests if applicable
4. Commit your changes: `git commit -m "Add your descriptive commit message"`
5. Push to your branch: `git push origin feature/your-feature-name`
6. Open a Pull Request against the main repository

## Code Style

This project uses:
- Black for code formatting
- isort for import sorting

You can run these tools before submitting your PR:
```bash
black hello_world_mcp/
isort hello_world_mcp/
```

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
