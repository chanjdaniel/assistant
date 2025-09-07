<general_rules>
**Agent and Service Creation Patterns:**
- Before creating new agents, always search the `app/agents/` directory to check if similar functionality already exists
- Before creating new services, always search the `app/services/` directory to check if similar functionality already exists
- When creating new agents, place them in `app/agents/` and follow the existing naming convention (e.g., `planner.py`, `repo_assistant.py`)
- When creating new services, place them in `app/services/` and follow the existing naming convention (e.g., `git_service.py`, `calendar_service.py`)

**Git-Based Undo Functionality:**
- All file changes are automatically tracked via Git commits for undo support
- Use the git service (`app/services/git_service.py`) for version control operations
- Always provide dry-run previews before applying changes to files or calendar events
- Tag calendar events with metadata to enable safe deletion and rollback operations

**Goals Management:**
- Goals are stored in the `goals/` directory in dual formats:
  - `goals.md`: Human-readable markdown format with frontmatter metadata
  - `index.yaml`: Machine-readable YAML format for programmatic access
- Always maintain both formats when updating goals
- Use the goals tools (`app/agents/goals_tools.py`) for goal management operations

**Development Workflow:**
- Use Docker Compose for local development: `docker-compose up`
- Environment variables should be configured via `.env` file (use `.env.example` as template)
- All changes should be containerized and tested within the Docker environment
- Follow the modular architecture pattern with clear separation between agents, services, models, ops, and utils
</general_rules>

<repository_structure>
**Main Application Structure (`app/`):**
- `agents/`: Core agent implementations for different functionalities
  - `planner.py`: Schedule planning and task organization agent
  - `repo_assistant.py`: Repository analysis and project folder queries
  - `calendar_tools.py`: Calendar integration and event management tools
  - `goals_tools.py`: Goal creation, tracking, and milestone management tools
- `services/`: Backend service implementations
  - `git_service.py`: Git operations and version control functionality
  - `embeddings.py`: Vector embeddings and RAG (Retrieval-Augmented Generation) service
  - `calendar_service.py`: Google Calendar API integration and event management
  - `file_watcher.py`: File system monitoring and change detection
- `models/`: Data models and schema definitions (placeholder for future expansion)
- `ops/`: Operations and deployment-related utilities (placeholder for future expansion)
- `utils/`: Shared utility functions and helpers (placeholder for future expansion)

**Goals Management (`goals/`):**
- Contains goal tracking files in both human and machine-readable formats
- Supports goal prioritization, deadlines, and milestone tracking
- Integrates with calendar planning and scheduling functionality

**Configuration Files:**
- `docker-compose.yml`: Docker Compose configuration for containerized development
- `Dockerfile`: Container image definition
- `.env.example`: Environment variable template for API keys and configuration
- `requirements.txt`: Python dependency specifications
</repository_structure>

<dependencies_and_installation>
**Python Dependencies:**
- Install dependencies using: `pip install -r requirements.txt`
- Dependencies are managed through `requirements.txt` in the repository root
- Core technologies include LangGraph, FastAPI, and various AI/ML libraries

**Environment Configuration:**
- Copy `.env.example` to `.env` and configure required environment variables
- Set up API keys for Google Calendar integration and AI model access
- Configure local development settings as needed

**Docker Setup:**
- Use Docker Compose for consistent development environment: `docker-compose up`
- All services run in containers to ensure environment consistency
- Docker handles dependency installation and service orchestration automatically
- No manual dependency installation required when using Docker workflow
</dependencies_and_installation>

<testing_instructions>
**Current Testing Status:**
- No testing framework is currently configured in this repository
- No existing test files or test directories are present

**Future Testing Implementation Guidance:**
- When implementing tests, consider using pytest as the testing framework
- Focus testing efforts on:
  - Agent functionality and decision-making logic
  - Service integrations (Git, Calendar, Embeddings)
  - Goal management operations and data consistency
  - API endpoints and request/response handling
- Create test files in a `tests/` directory following pytest conventions
- Mock external dependencies (Google Calendar API, Git operations) in tests
- Ensure tests can run in the Docker environment for consistency
- Consider integration tests for end-to-end workflow validation
</testing_instructions>

<pull_request_formatting>
</pull_request_formatting>
