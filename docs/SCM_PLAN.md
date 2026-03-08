# Software Configuration Management (SCM) Plan
## Book Catalog Service

## 1. Introduction

This document outlines the Software Configuration Management (SCM) plan for the Book Catalog Service project.  
The purpose of this plan is to ensure proper control, tracking, and management of all project artifacts including source code, documentation, and configuration files throughout the development lifecycle.

SCM practices help maintain system integrity, enable team collaboration, and support controlled evolution of the software.

---

# 2. SCM Objectives

The main objectives of Software Configuration Management in this project are:

## 2.1 Traceability

Traceability ensures that all changes made to the system are tracked and documented.

Using Git allows the team to:
- Track who made each change
- Identify when the change occurred
- Understand the purpose of each modification through commit messages

This improves transparency and helps in debugging and auditing project history.

---

## 2.2 Quality

SCM supports maintaining high software quality by controlling how code changes are introduced into the main codebase.

Quality is ensured by:
- Using feature branches for development
- Reviewing code before merging
- Applying Continuous Integration (CI) checks such as linting and unit testing

These practices prevent unstable or incorrect code from entering the main branch.

---

## 2.3 Reliability

Reliability is achieved by maintaining a stable and well-managed codebase.

Git enables:
- Version history for all changes
- The ability to revert to previous stable versions
- Controlled integration of new features

This ensures the system remains stable even when new updates are introduced.

---

# 3. Version Control System

The project uses **Git** as the version control system.

Git provides:
- Distributed version control
- Efficient branching and merging
- Collaboration support for multiple developers

The repository is initialized locally and can later be hosted on platforms such as GitHub or GitLab.

---

# 4. Branching Strategy

The project adopts a **Git Flow-inspired branching strategy** to manage development activities.

## Main Branch

The `master` branch contains the stable and production-ready version of the project.  
All finalized features and stable updates are merged into this branch.

---

## Feature Branches

New features are developed in separate branches created from the `master` branch.

Feature branch naming convention:
