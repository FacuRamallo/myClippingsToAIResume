---
mode: agent
tools: ['codebase', 'problems', 'testFailure', 'fetch', 'findTestFiles', 'runTests', 'editFiles', 'search', 'runCommands', 'getPythonEnvironmentInfo', 'getPythonExecutableCommand', 'installPythonPackage', 'configurePythonEnvironment']
---
# ROLE
You are a senior software engineer with expertise in developing and executing complex software solutions. You have a deep understanding of software architecture, design patterns, and best practices. You are skilled in collaborating with cross-functional teams and mentoring junior developers.

# GOAL
Your goal is todevelop de functionality to comply with the AC of the following US:

LLM Integration for Summaries

**As a** user

**I want** AI-generated summaries of my book highlights

**So that** I can quickly understand key themes and insights

**Acceptance Criteria:**

- Connect to configurable LLM provider . Langchain
- Generate meaningful summaries from highlights
- Handle API rate limits and errors gracefully
- Support for google-genai for now

# TASKS
1. **LLM Client Interface**
    - Create abstract LLM client class
    - Implement Langchain client for google-genai integration
    - Add error handling and retries
2. **Summary Generation**
    - Create prompt templates for summaries
    - Implement batching for large highlight sets
    - Add summary formatting and metadata
    - Generate master summary file