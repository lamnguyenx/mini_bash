<!--
Sync Impact Report:
- Version change: 0.1.0 → 1.0.0 (MAJOR: Initial constitution adoption)
- Modified principles: All principles created from scratch
- Added sections: Core Principles, Development Standards, Governance
- Removed sections: None (template fully populated)
- Templates requiring updates:
  ✅ plan-template.md - Constitution Check section aligns with new principles
  ✅ spec-template.md - No conflicts with new principles
  ✅ tasks-template.md - No conflicts with new principles
  ⚠ agent-file-template.md - Pending review
  ⚠ checklist-template.md - Pending review
- Follow-up TODOs: None - all placeholders resolved
-->

# mini_bash Constitution

## Core Principles

### I. Minimalism & Focus
Every feature must serve the core purpose of safe bash command execution; Avoid feature creep and unnecessary complexity; The package should remain small, focused, and dependency-free beyond Python standard library.

**Rationale**: mini_bash exists to solve one problem well - running bash commands safely from Python. Additional features would dilute this purpose and increase maintenance burden.

### II. Safety First (NON-NEGOTIABLE)
All bash commands MUST run with `set -Eeuo pipefail` by default; Commands MUST fail fast on errors; RuntimeError MUST be raised with clear error messages including the failed command and stderr output.

**Rationale**: The primary value proposition is preventing silent failures in bash commands. Users rely on mini_bash to catch and report errors that would otherwise be missed.

### III. Pythonic Interface
API must follow Python conventions and idioms; Function signatures must be clear and intuitive; Return types must be predictable (stdout, stderr tuple); Documentation must be accessible and practical.

**Rationale**: As a Python library, mini_bash should feel natural to Python developers and integrate seamlessly with existing Python codebases.

### IV. Zero External Dependencies
The package MUST NOT require any external dependencies beyond Python standard library; All functionality must be self-contained; Avoid introducing new dependencies unless absolutely necessary.

**Rationale**: One of mini_bash's key advantages is its simplicity and lack of dependency management complexity. This makes it easy to install and use in any Python environment.

### V. Backward Compatibility
Breaking changes require MAJOR version increments; Deprecation periods must be clearly communicated; Changes to default behavior must be justified and documented.

**Rationale**: As a utility library, stability is crucial for users who integrate mini_bash into their workflows and production systems.

## Development Standards

### Package Management
- Use Poetry for dependency management and packaging
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Maintain clear separation between development and runtime dependencies
- Keep pyproject.toml configuration minimal and focused

### Code Quality
- Single responsibility principle: one module, one purpose
- Type hints required for all public interfaces
- Comprehensive docstrings following Python conventions
- Error handling must be explicit and informative

### Testing Approach
- Manual testing required for all changes
- Test coverage should include common bash command patterns
- Edge cases: empty commands, commands with special characters, permission errors
- Integration testing with real bash commands

## Governance

This constitution supersedes all other development practices and conventions. Amendments require:
1. Documentation of the proposed change and rationale
2. Review of impact on existing principles
3. Version increment according to semantic versioning rules
4. Update to dependent templates and documentation

All pull requests and code reviews must verify compliance with these principles. Complexity must be justified with clear user benefits. Use CLAUDE.md for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-10-23 | **Last Amended**: 2025-10-23