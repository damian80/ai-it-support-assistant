# AI IT Support Assistant

An AI-powered IT support chatbot built with Python and Claude API (Anthropic). Designed for school IT environments using macOS, JAMF Pro, and Google Workspace.

## Features

- Interactive chat interface with Claude AI
- Conversation memory — Claude remembers context within a session
- Conversation logging with timestamps
- Custom system prompt tailored for school IT support
- Handles common IT issues: projectors, networking, device management, Google Workspace

## Tech Stack

- Python 3
- Anthropic Claude API
- python-dotenv (environment variable management)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/damian80/ai-it-support-assistant.git
cd ai-it-support-assistant
```

2. Install dependencies:
```bash
pip3 install anthropic python-dotenv
```

3. Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

4. Run the assistant:
```bash
python3 "First API call.py"
```

## Usage

```
Welcome to AI IT Support Assistant
Type 'quit' to exit

You: my projector has no display in room 118
IT Support: Let's troubleshoot the projector. First, check these common issues:
1. Ensure the projector is powered on
2. Check HDMI cable connections
3. Press Input/Source on the remote to cycle inputs
...

You: quit
Conversation Saved!
```

## Future Improvements

- Web interface
- Ticket creation system
- Integration with JAMF Pro API
- Multi-user support

## Author

Built by Damian Ciasnocha as part of an AI Engineering career development portfolio.
