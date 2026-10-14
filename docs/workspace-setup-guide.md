# 🌐 Workspace Distribution & Cross-Project Integration Guide

This guide defines how to establish `agent-workspace` as the single source of truth across all **Eigenscribe Inc.** and **Scriber Labs** repositories using **Option B: Centralized Submodule / Template Repository Architecture**.

---

## 🏛️ Architecture Overview

To eliminate drift across independent projects, all agents, engineers, and repositories link directly back to `agent-workspace`:

```text
agent-workspace (Canonical Single Source of Truth)
├── house-rules/
│   ├── python-rules.md
│   └── css-rules.md
├── boilerplates/
│   ├── gold-standard-boilerplate.py
│   └── tse-boilerplate.css
└── docs/
    └── workspace-setup-guide.md

       │
       ├──► [Workflow 1: Git Submodule]  ──► Existing Projects (.agent-workspace/)
       │
       └──► [Workflow 2: Template Repo]  ──► Green-field Repositories
```

---

## 🔗 Workflow 1: Git Submodule Integration (Existing Projects)

For existing codebases or multi-repo ecosystems, include `agent-workspace` as a git submodule to ensure seamless synchronization.

### 1️⃣ Step 1: Add Submodule to Target Repository
From the root of your target repository, run:

```bash
git submodule add <REPO_URL_TO_AGENT_WORKSPACE> .agent-workspace
```

### 2️⃣ Step 2: Configure Agent Entry Point
Create or update `.junie/AGENTS.md` (and optionally a root `AGENTS.md`) in your target repository with standard reference bridges:

```markdown
# 🔬 Project Agent Guidelines

This project adheres to canonical Eigenscribe Inc. / Scriber Labs development standards.

## 📁 Canonical Workspace References
Agents must consult the linked rules and templates in `.agent-workspace`:
- **Python Rules**: `.agent-workspace/house-rules/python-rules.md`
- **CSS / UI System**: `.agent-workspace/house-rules/css-rules.md`
- **Python Numeric Template**: `.agent-workspace/boilerplates/gold-standard-boilerplate.py`
- **CSS Design System Template**: `.agent-workspace/boilerplates/tse-boilerplate.css`

## 🎯 Project-Specific Context & Overrides
- Target domain and operational requirements for this repository.
```

### 3️⃣ Step 3: Clone & Synchronization Commands
- **Cloning a project with the submodule**:
  ```bash
  git clone --recurse-submodules <TARGET_REPO_URL>
  ```
- **Updating to the latest rules across all repos**:
  ```bash
  git submodule update --remote --merge
  ```

---

## 📋 Workflow 2: Template Repository (New Projects)

For greenfield projects:

### 1️⃣ Step 1: Enable Template Repository
In GitHub / GitLab repository settings for `agent-workspace`:
- Check **"Template repository"** (GitHub) / mark as template.

### 2️⃣ Step 2: Initialize from Template
1. Create a new repository using `agent-workspace` as the template base.
2. Clone locally and verify directory layout.
3. The newly generated project retains the canonical structure (`house-rules/`, `boilerplates/`, `.junie/AGENTS.md`).

---

## 🛠️ Verification & Best Practices

1. **Path Resolution**: Keep paths in consumer projects pointing cleanly to `.agent-workspace/house-rules/...`.
2. **Version Pinning**: Submodules allow pinning to specific stable commits or tags for critical releases, preventing accidental breakage from rule changes.
3. **Continuous Enforcement**: Agent sessions run against the linked rules without requiring manual copy-pasting across projects.
