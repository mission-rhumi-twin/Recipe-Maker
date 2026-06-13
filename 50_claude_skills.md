# 50 Claude Skills Every Engineer and Researcher Should Own

> A curated, deduplicated, and impact-ranked reading list drawn from the full landscape of community-built Claude Code skills. Every entry was selected on one criterion: **does it meaningfully reduce the cost of doing hard technical work?** Stars, hype, and novelty were irrelevant. Impact was the only vote that counted.
>
> Every source link below was verified live. No guessed URLs.

---

## How to Use This Document

Each skill entry follows this structure:

- **What it is** — plain-language description of the skill's function
- **Why it matters** — the real engineering or research problem it solves
- **Best used when** — the specific trigger that makes this skill worth activating
- **Install** — verified direct GitHub link to the SKILL.md or repo

Skills are grouped into six domains. Within each domain, ordered by breadth of impact — the ones that affect the most work, most often, come first.

---

## Domain 1 — Thinking, Planning, and Process

These skills run before any code is written. Most engineers skip planning because it feels slow. These make planning faster than skipping it.

---

### 1. `grill-me`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md

Before you commit to any plan, any architecture, any approach — this skill interviews you. It asks the questions you didn't know you needed to answer. It surfaces implicit assumptions, catches circular logic, and stress-tests your reasoning before you've spent a single hour on implementation. The skill is deliberately adversarial: it will not validate your idea, it will interrogate it. Engineers who use this before writing code ship fewer rewrites.

**Best used when:** You have a plan you feel confident about. Especially then.

---

### 2. `grill-with-docs`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md

The same adversarial interview as `grill-me`, extended to challenge your plan against your existing architecture decision records (ADRs) and CONTEXT.md. It does not just ask if your plan is internally consistent — it asks whether it's consistent with decisions already made. This catches the most expensive class of mistake: the technically correct solution that contradicts a decision made six months ago for reasons nobody told you about.

**Best used when:** Working in an existing codebase with documented architecture decisions, or onboarding to a team that has a CONTEXT.md.

---

### 3. `writing-plans`
**Install:** https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md

Converts messy, rambling thinking into a structured, milestone-driven written plan. It separates the goal from the approach, the approach from the steps, and the steps from the verification criteria. Plans produced with this skill can be handed off, reviewed, and executed without the original author in the room. Without this skill, most engineers confuse "I know what I'm doing" with "I have a plan." Those are different things.

**Best used when:** Starting any project or task that spans more than one session, involves more than one person, or will be reviewed by someone else.

---

### 4. `executing-plans`
**Install:** https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md

Executes structured plans with checkpoints and verification at each step. It prevents the failure mode where a plan is made and then immediately abandoned when implementation hits friction. The skill enforces that the current step must be demonstrably complete before moving to the next. This is the difference between a plan and a plan that gets followed.

**Best used when:** Working through a multi-step plan, especially during long implementation sessions where context drift is a risk.

**Chains naturally with:** `writing-plans`, `grill-me`

---

### 5. `brainstorming`
**Install:** https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md

Structured creative idea generation. The value is not that it generates more ideas — it is that it generates ideas you would not have reached by anchoring on the first reasonable option. It enforces divergence before convergence, the part of brainstorming most people skip. Engineers in particular tend to identify a good-enough solution and stop. This skill makes that early stopping visible and costly.

**Best used when:** You have a problem and one solution already in mind. The goal is to not let that one solution be the only one you evaluate.

---

### 6. `prototype`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md

Builds a deliberately throwaway prototype to explore the design space before committing to a real implementation. The prototype is not the product. It is the experiment that tells you whether your assumptions about the product are correct. This skill enforces the mental separation between exploration and commitment — two modes of engineering work that should never happen simultaneously.

**Best used when:** You are uncertain about an interface, API design, data model, or user interaction pattern. When uncertainty is high, build cheap and break fast.

---

### 7. `to-issues`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md

Takes any plan, spec, or PRD and breaks it into independently-grabbable GitHub issues using vertical slicing. Each issue is scoped so that a single engineer can pick it up without needing to understand the entire system. This is the skill that makes plans executable at a team level.

**Best used when:** You have a written plan or spec and need to move it into an issue tracker for distribution and tracking.

**Chains naturally with:** `writing-plans`, `prd-to-plan`

---

### 8. `prd-to-plan`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/prd-to-plan/SKILL.md

Converts a product requirements document into a multi-phase, vertical-slice execution plan with architectural decisions locked upfront. The key distinction from `to-issues` is that this skill produces a sequenced plan with dependencies and locked decisions, not just a list of tasks. It answers what order to do things in, and why.

**Best used when:** You have a PRD and need to translate it into an engineering execution plan that a team can follow without constant clarification.

---

### 9. `domain-model`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-model/SKILL.md

Extracts the ubiquitous language from a codebase and domain experts, then maintains a living model of what terms mean in your specific context. Term drift — where "user," "account," "customer," and "profile" start meaning different things to different people — is one of the most invisible and expensive sources of bugs and miscommunication in engineering. This skill makes domain language explicit and enforced.

**Best used when:** Starting a new project, onboarding to a codebase, or when the same word means different things in different parts of your system.

---

### 10. `preserving-productive-tensions`
**Install:** https://github.com/obra/superpowers/blob/main/skills/preserving-productive-tensions/SKILL.md

Manages architectural decisions by holding competing viewpoints simultaneously rather than forcing premature resolution. Some architectural decisions do not have right answers — they have tradeoffs. This skill prevents the pressure to decide from collapsing nuanced tradeoffs into false certainty. It keeps the tension alive until the decision is genuinely informed.

**Best used when:** Facing architectural choices where smart people disagree, or where the right answer depends on future information you do not yet have.

---

## Domain 2 — Code Quality, Debugging, and Review

These skills address the work that happens after the plan and before the merge.

---

### 11. `systematic-debugging`
**Install:** https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md

A four-phase root cause methodology: reproduce → isolate → hypothesize → verify. No guessing allowed. The skill enforces that you cannot move to the next phase until the current one is complete. This sounds simple until you are three hours into a bug and you realize you have been guessing since hour one. This skill breaks that pattern by making the methodology explicit and mandatory.

**Best used when:** You have a bug you cannot immediately explain, or when you have already spent more than thirty minutes without a clear hypothesis.

---

### 12. `diagnose`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md

A disciplined root-cause debug loop specifically designed for hard bugs and performance regressions. Where `systematic-debugging` is a general methodology, `diagnose` is tuned for the specific challenges of performance work — where the bug is not a crash but a slow path, and where isolation is harder because the behavior is statistical rather than deterministic.

**Best used when:** Performance regressions, intermittent failures, or bugs that only appear under load or in specific environments.

---

### 13. `tdd`
**Install:** https://github.com/obra/superpowers/blob/main/skills/tdd/SKILL.md

Red-green-refactor test-driven development enforcement per vertical slice. The skill does not just suggest TDD — it enforces it. You write a failing test first. You write the minimum code to make it pass. Then you refactor. The discipline here is not the methodology (most engineers know it) but the enforcement (most engineers skip it when under pressure).

**Best used when:** Any new feature or bug fix. The habit is more valuable than the technique.

---

### 14. `karpathy-guidelines`
**Install:** https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md

Behavioral coding guidelines distilled from Andrej Karpathy's engineering philosophy: no overcomplication, no hidden assumptions, no magic. The skill keeps Claude honest about implementation choices — it pushes back on unnecessary abstraction, premature generalization, and code that is clever at the cost of being readable. Particularly valuable when working with AI-generated code, which tends toward verbose solutions that look complete but carry hidden complexity.

**Best used when:** Code review, refactoring, or any time you suspect the implementation is more complicated than the problem requires.

---

### 15. `verification-before-completion`
**Install:** https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md

An evidence checklist the agent must pass before it is permitted to declare any task complete. This skill exists because AI agents are optimistic: they report success before verification. The checklist forces demonstration rather than assertion. "It should work" is not acceptable. "Here is the test output showing it works" is.

**Best used when:** Any agentic workflow where Claude is executing multi-step tasks. This is the guardrail that keeps "done" honest.

---

### 16. `requesting-code-review`
**Install:** https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md

A pre-submission checklist that surfaces issues before any human reviewer sees your work. It systematically checks for the categories of problems reviewers will catch anyway — and makes you catch them yourself first. This compresses review cycles, reduces back-and-forth, and signals to reviewers that you have done the basic work of self-review.

**Best used when:** Before submitting any pull request or code for review.

**Chains naturally with:** `receiving-code-review`

---

### 17. `receiving-code-review`
**Install:** https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md

A structured protocol for processing and applying review feedback without ego. The skill separates receiving feedback (understanding what the reviewer is saying) from responding to feedback (deciding what to do about it) from applying feedback (making the changes). Most engineers conflate all three and respond defensively to the first one. This skill slows the process down in the right places and speeds it up overall.

**Best used when:** You have received code review feedback, especially feedback you disagree with or find unclear.

---

### 18. `finishing-a-development-branch`
**Install:** https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md

Runs a test gate and presents four merge options with appropriate context for each. The skill enforces that branches are not merged until they pass the defined test criteria — not because someone checked a box, but because the test gate actually ran and passed. The four merge options provide structured decision support for the merge strategy.

**Best used when:** Completing any development branch before merging to main or a shared environment.

---

### 19. `improve-codebase-architecture`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md

Identifies deepening opportunities in a codebase and uses domain language from CONTEXT.md to frame architectural improvements in the language of your actual system. It does not suggest generic best practices — it suggests specific improvements grounded in the vocabulary and constraints of your project.

**Best used when:** The codebase works but feels wrong. When you sense architectural debt but cannot articulate it clearly enough to act on it.

---

### 20. `finding-duplicate-functions`
**Install:** https://github.com/obra/superpowers-lab/blob/main/skills/finding-duplicate-functions/SKILL.md

Semantic duplication detection optimized for LLM-generated codebases. AI assistants are particularly prone to generating semantically identical functions with different names because they lack memory of what was written earlier in the session. This skill finds that duplication before it compounds into a maintenance problem.

**Best used when:** After any significant AI-assisted coding session, or when a codebase feels like it has grown faster than its coherence.

---

## Domain 3 — Research, Writing, and Academic Work

These skills exist at the intersection of engineering and scholarship. For anyone producing knowledge — papers, reports, literature reviews, technical documentation — not just code.

---

### 21. `academic-research-skills` (deep-research)
**Install:** https://github.com/Imbad0202/academic-research-skills/blob/main/deep-research/SKILL.md
**Repo:** https://github.com/Imbad0202/academic-research-skills

A thirteen-agent pipeline covering the full arc of academic research: literature review, Socratic guided mode for developing arguments, and systematic review following PRISMA methodology. It can take a research question and produce a defensible, citation-grounded literature review with the rigor expected at graduate level. The Socratic mode detects user intent — exploratory versus goal-oriented — and adjusts its behavior accordingly.

**Best used when:** Starting a new research area, preparing a related work section, or conducting a systematic review for a paper or thesis.

**Chains naturally with:** `academic-paper`, `research-claim-map`

---

### 22. `academic-paper`
**Install:** https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper/SKILL.md

A twelve-agent paper writing pipeline producing LaTeX output with visualization, revision coaching, and multi-format citation management. The agents specialize: one handles structure, one handles writing quality, one handles figures, one handles citations. The output is not a draft — it is a manuscript ready for revision. Full pipeline estimate is roughly $4–6 per 15,000-word paper.

**Best used when:** Writing a conference paper, journal article, or thesis chapter.

---

### 23. `academic-paper-reviewer`
**Install:** https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper-reviewer/SKILL.md

Multi-perspective peer review with a 0–100 rubric, simulating an Editor-in-Chief plus three specialist reviewers plus a Devil's Advocate. The Devil's Advocate does not soften under pushback — it uses rebuttal assessment with explicit deflection detection. Anti-sycophancy rules prevent persistent pushback from being treated as valid evidence. Finds things you cannot find yourself because you know what you meant to write.

**Best used when:** Before submitting any paper. Also useful during writing to stress-test arguments before they are fully committed to prose.

---

### 24. `claude-scientific-writer`
**Install:** https://github.com/K-Dense-AI/claude-scientific-writer

Publication-ready scientific document creation with real-time research lookup, citation management, and an eight-dimension ScholarEval review. The eight dimensions include originality, methodological rigor, clarity, significance, and reproducibility — the criteria that determine whether a paper gets published.

**Best used when:** Producing research reports, technical white papers, or manuscript drafts where publication quality is the target.

---

### 25. `research-claim-map`
**Install:** https://github.com/lyndonkl/claude/blob/main/skills/research-claim-map/SKILL.md
**Repo:** https://github.com/lyndonkl/claude

Triangulated claim verification with source grading and confidence calibration per claim. Every factual assertion in your work gets mapped to its sources, graded for quality, and tagged with a confidence level. This is the skill that separates rigorous technical writing from writing that merely looks rigorous.

**Best used when:** Any technical writing where factual claims need to be traceable and defensible. Critical for papers, reports, and any work that will be reviewed or cited.

---

### 26. `inspectional-reading`
**Install:** https://github.com/lyndonkl/claude/blob/main/skills/inspectional-reading/SKILL.md

Adler Level 1 systematic reading: skim, classify document type, and decide whether deeper reading is worth the time. Most technical professionals read everything at the same depth, which means they read too much of the wrong things and too little of the right things. This skill makes the decision about depth explicit and fast.

**Best used when:** Evaluating a paper or document before deciding whether to read it in full. Especially useful during literature reviews when volume is high.

**Chains naturally with:** `structural-analysis` (Adler Level 2), `component-extraction` (Adler Level 3)

---

### 27. `structural-analysis`
**Install:** https://github.com/lyndonkl/claude/blob/main/skills/structural-analysis/SKILL.md

Adler Level 2 reading: classify content type, state the unity of the work in one sentence, enumerate its parts, and define the problem it is solving. This is the level of reading where you understand what a paper is doing before you evaluate whether it is doing it well. Most peer reviewers skip this level and go directly to line editing, which is why reviews often miss structural problems.

**Best used when:** Reading a paper you need to evaluate, cite, or build on. Before writing a related work section.

---

### 28. `component-extraction`
**Install:** https://github.com/lyndonkl/claude/blob/main/skills/component-extraction/SKILL.md

Adler Level 3 deep thematic extraction with value chains, sub-trends, and watch indicators. This is the level of reading where you extract actionable intelligence from a document — not just what it says, but what it implies, what it does not say, and what you should watch for as a result. For researchers, this is the difference between consuming the literature and using it.

**Best used when:** Reading seminal papers in a new field, synthesizing a body of literature, or preparing a comprehensive literature review.

---

### 29. `avoid-ai-writing`
**Install:** https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md
**Repo:** https://github.com/conorbronsdon/avoid-ai-writing

Audits and rewrites text to remove AI writing patterns using a 109-entry tiered word replacement table and 49 pattern categories. Three detection tiers: Tier 1 words always flag, Tier 2 flag when they cluster, Tier 3 flag only at high density. Includes a detect mode that flags without rewriting — useful when patterns might be intentional. Works in Claude Code, Cursor, Hermes, and OpenClaw.

**Best used when:** Before submitting any written work — papers, reports, cover letters, documentation, anything a person will read and judge.

---

### 30. `autoresearch`
**Install:** https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill
**Repo:** https://github.com/Orchestra-Research/AI-Research-SKILLs

Autonomous research orchestration using a two-loop architecture: inner loop handles rapid experiments with measurable outcomes; outer loop handles synthesis, reflection, and paper writing. Two fully autonomous papers have been produced end-to-end using this skill. Also installable via `npm install @orchestra-research/ai-research-skills` for one-command setup across all coding agents.

**Best used when:** You have a research question and need to move from hypothesis to documented result with minimal manual orchestration.

---

## Domain 4 — Aerospace and Scientific Computing

For engineers and researchers working in simulation-heavy, numerically intensive, or domain-specific technical fields.

---

### 31. `orbital-mechanics`
**Install:** https://github.com/Soljourner/claude-engineering-skills/blob/master/skills/thinking/orbital-mechanics/SKILL.md
**Repo:** https://github.com/Soljourner/claude-engineering-skills

Orbit propagation, trajectory analysis, and maneuver planning covering Hohmann transfers, bi-elliptic transfers, and interplanetary trajectories. The skill encodes the mathematical and physical constraints of astrodynamics so Claude can reason about orbital problems with the precision the domain requires — not as a generalist approximating the field, but as a tool that understands the governing equations.

**Best used when:** Trajectory design, mission planning, orbit determination, or any work involving propagation of state vectors under gravitational and perturbative forces.

---

### 32. `fluid-dynamics` + `pump-design`
**Install:** https://github.com/Soljourner/claude-engineering-skills/blob/master/skills/thinking/fluid-dynamics/SKILL.md

Centrifugal and axial pump analysis, CFD setup, OpenFOAM workflow integration, and cavitation checks. Covers the complete workflow from problem setup through solver configuration through results interpretation. The pairing of pump design with fluid dynamics is deliberate — design problems and analysis problems in this domain are inseparable.

**Best used when:** Propulsion system design, flow analysis for spacecraft thermal systems, or any engineering problem involving fluid behavior.

---

### 33. `structural-analysis + FEA`
**Install:** https://github.com/Soljourner/claude-engineering-skills/blob/master/skills/thinking/structural-analysis/SKILL.md

ANSYS integration, stress and fatigue and buckling workflows, and boundary condition setup for finite element analysis. The skill handles the translation between physical problem and computational model — the part of FEA that is most error-prone because it requires both domain knowledge and software knowledge simultaneously.

**Best used when:** Structural analysis of spacecraft components, load cases for launch environments, or any problem requiring stress, fatigue, or buckling evaluation.

---

### 34. `thermodynamics`
**Install:** https://github.com/Soljourner/claude-engineering-skills/blob/master/skills/thinking/thermodynamics/SKILL.md

Heat transfer analysis, thermal system design, and fluid property lookups. Covers conduction, convection, and radiation with the level of rigor required for spacecraft thermal analysis. The fluid property lookup capability connects the analytical work to real material data.

**Best used when:** Thermal control system design, heat exchanger sizing, or any analysis requiring accurate thermophysical properties.

---

### 35. `materials-simulation-skills`
**Install:** https://github.com/HeshamFS/materials-simulation-skills
**Repo:** https://github.com/HeshamFS/materials-simulation-skills

Numerical stability, time-stepping strategies, linear solver selection, and simulation validation for computational materials science. The skill addresses challenges specific to materials simulation: stiffness, convergence, and the gap between simulation results and physical reality. Validation methodology is built in — not as a check at the end, but as a discipline throughout. Install individual skills via `cp -r skills/core-numerical/numerical-stability ~/.claude/skills/numerical-stability`.

**Best used when:** Any simulation work where numerical stability is a concern, or where you need to validate that your simulation is modeling the physics you intend.

---

## Domain 5 — Productivity, Session Management, and Workflow Chaining

Claude has no memory between sessions. These skills are the infrastructure for making it behave as though it does.

---

### 36. `handoff`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md

Compacts any session into a handoff document for cross-session and cross-agent continuity. The handoff document captures decisions made, context established, and next steps identified — in a format that can be fed into a new session to restore context without re-explaining everything. This is the single most important session management skill because it is the one that makes all other long-running work possible.

**Best used when:** Ending any session that will be continued. Before any context-critical work that might span multiple sessions.

---

### 37. `caveman`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/productivity/caveman/SKILL.md

Reduces token usage by approximately seventy-five percent while preserving full technical accuracy. Strips filler, redundancy, and conversational overhead from prompts and responses, keeping only the technically essential content. In long sessions with large codebases or documents, token limits are a real constraint. This skill extends how far you can go in a single context window.

**Best used when:** Working with large codebases, long documents, or any session where you are approaching context limits.

---

### 38. `session-search`
**Install:** https://github.com/glebis/claude-skills
**Repo:** https://github.com/glebis/claude-skills

Semantic search across all Claude Code session transcripts. When you need to find a decision, a solution, or a piece of context from a previous session, this skill makes your entire history searchable by meaning rather than by keyword. It converts your session history from an archive into a retrievable knowledge base.

**Best used when:** You know you solved a problem before but cannot remember how. Or when you need to reconstruct the reasoning behind a past decision.

---

### 39. `everything-learning`
**Install:** https://github.com/glebis/claude-skills

Auto-extracts patterns from coding sessions and converts them into reusable skills. The agent learns from your work: the solutions you reach, the debugging approaches that worked, the architectural decisions you made and why. Over time, this creates a personalized skill library derived from your own engineering history rather than from generic best practices.

**Best used when:** Any session where you solve a non-trivial problem. Most powerful when used consistently over time.

---

### 40. `retrospective`
**Install:** https://github.com/glebis/claude-skills

End-of-session learning capture using Continual Learning patterns. At the end of a session, the skill extracts what was learned — not what was done, but what was understood that was not understood before. Over time, the accumulation of these retrospectives becomes a personal knowledge base of engineering lessons specific to your work rather than generic to the field.

**Best used when:** End of every significant working session. The value compounds over time; the individual investment is small.

---

## Domain 6 — Multi-Agent, Advanced Automation, and Meta-Skills

These skills are the difference between using Claude as a tool and using Claude as a system.

---

### 41. `dispatching-parallel-agents`
**Install:** https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md

Fans out concurrent subagent workflows, merges results, and handles BLOCKED and DONE_WITH_CONCERNS statuses. This skill makes parallel agent execution practical rather than theoretical — the status handling is what makes it reliable. Without explicit handling of blocked and uncertain states, parallel agent workflows fail silently in ways that are hard to detect.

**Best used when:** Any task that can be decomposed into independent parallel subtasks. Research synthesis, large-scale code analysis, multi-file documentation.

---

### 42. `subagent-driven-development`
**Install:** https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md

Multi-agent execution with two-stage review per task: first stage executes, second stage reviews the execution before the result is accepted. This architecture catches the class of errors that single-agent execution misses because the agent that made the error cannot see it from inside the context that produced it.

**Best used when:** Complex implementation tasks where errors in one step compound into larger problems in subsequent steps.

---

### 43. `context-engineering-kit`
**Install:** https://github.com/NeoLabHQ/context-engineering-kit
**Plugin install:** `/plugin install sdd@NeoLabHQ/context-engineering-kit`

Multi-agent orchestration with context isolation of independent agents, quality gates based on LLM-as-Judge scoring, continuous learning that builds skills the agent needs to implement specific tasks, and spec-driven development based on the arc42 standard. Works best in complex or large codebases. Three commands: `/implement-task`, `/sdd:add-task`, `/plan-task`.

**Best used when:** Building serious agentic workflows, or when you need Claude to maintain coherence across complex multi-step tasks with existing architecture.

---

### 44. `compound-engineering-plugin`
**Install:** https://github.com/EveryInc/compound-engineering-plugin
**Plugin install:** `/plugin marketplace add EveryInc/compound-engineering-plugin && /plugin install compound-engineering`

Ideation through planning through execution through multi-agent review through knowledge compounding — a complete engineering workflow in a single plugin. Ships 37 skills and 51 agents. The knowledge compounding component is what distinguishes this from a simple workflow orchestrator: each session deposits learnings that improve subsequent sessions via the `/ce-compound` command.

**Best used when:** You want a single plugin that covers the full engineering workflow rather than assembling individual skills per phase.

---

### 45. `AI-Research-SKILLs` (full suite)
**Install:** https://github.com/Orchestra-Research/AI-Research-SKILLs
**npm:** `npm install @orchestra-research/ai-research-skills`

Comprehensive library of AI research and engineering skills covering model architecture, fine-tuning, mechanistic interpretability, data processing, post-training, safety, distributed training, optimization, evaluation, inference, agents, RAG, multimodal, MLOps, prompt engineering, and autonomous research orchestration. Each skill provides 200–500 lines of focused, actionable guidance with progressive disclosure. Twenty-plus skills total.

**Best used when:** You are working on or researching ML systems and need domain-specific guidance rather than general advice.

---

### 46. `write-a-skill`
**Install:** https://github.com/mattpocock/skills/blob/main/skills/productivity/write-a-skill/SKILL.md

Creates new Claude skills with proper structure and progressive disclosure. This is the meta-skill: the one that lets you extend every other skill on this list, build skills that do not exist yet, and encode your own engineering knowledge into reusable, deployable form. Once you can build your own skills, this document becomes a starting point rather than a ceiling.

**Best used when:** You have a workflow, methodology, or domain-specific approach that you use repeatedly and want to encode once and reuse indefinitely.

---

### 47. `prompt-architect`
**Install:** https://github.com/ckelsoe/prompt-architect
**Repo:** https://github.com/ckelsoe/prompt-architect

Transforms vague or incomplete prompts into expert-level structured prompts using CO-STAR, RISEN, RISE, TIDD-EC, RTF, Chain-of-Thought, and Chain-of-Draft frameworks. Evaluates prompts across five quality dimensions: clarity, specificity, context, completeness, and structure — then guides you through targeted clarifying questions before applying the selected framework. Raises the quality floor of every other skill on this list because every skill is activated by a prompt.

**Best used when:** Before any high-stakes or complex interaction. When you know what you want but cannot articulate it in a way that produces the output you need.

---

### 48. `mxyhi/ok-skills` (karpathy-guidelines variant + planning)
**Install:** https://github.com/mxyhi/ok-skills
**Repo:** https://github.com/mxyhi/ok-skills

Curated AI coding agent skills and AGENTS.md playbooks for Claude Code, Codex, Cursor, and other SKILL.md-compatible tools. Packages karpathy-guidelines, caveman, and planning-with-files defaults into a CLAUDE_AGENTS.md that encodes a complete workflow with strict TypeScript expectations, multi-agent preference, and context-mode routing rules. More opinionated than individual skill installs — useful as a ready-made engineering culture baseline.

**Best used when:** You want a single coherent workflow package rather than assembling individual skills, and are working primarily in TypeScript.

---

### 49. `academic-pipeline` (full pipeline orchestrator)
**Install:** https://github.com/Imbad0202/academic-research-skills/blob/main/academic-pipeline/SKILL.md

The master orchestrator for the complete research workflow: deep-research → academic-paper → academic-paper-reviewer → revision loop. Runs as a single end-to-end pipeline from research question to publication-ready manuscript. Suite version currently at v3.11.0. For Codex, use the sibling distribution at `Imbad0202/academic-research-skills-codex`.

**Best used when:** You want to run the full research-to-paper pipeline without managing each skill individually. High setup cost, maximum throughput.

**Chains:** All four Imbad0202 skills in sequence.

---

### 50. `claude-deep-research-skill`
**Install:** https://github.com/199-biotechnologies (search for claude-deep-research-skill)
**Note:** Maintained by 199 Biotechnologies. Search the repo directly for the most current install path.

An eight-phase research pipeline: Scope → Retrieve (parallel five to ten searches with sub-agents) → Triangulate → Synthesize → Critique → Package. DOI and URL hallucination detection is built in. The pipeline auto-continues for reports exceeding eighteen thousand words. This is the most comprehensive single-skill research capability on this list — it covers the full arc from question to documented, cited, critiqued output with the structural integrity of a methodology rather than a conversation.

**Best used when:** Deep technical literature reviews, comprehensive technical reports, or any research task where rigor and completeness are non-negotiable.

**Chains naturally with:** `academic-paper`, `research-claim-map`, `avoid-ai-writing`

---

## Quick Reference Index

| # | Skill | Domain | Source Repo |
|---|-------|--------|-------------|
| 1 | `grill-me` | Planning | mattpocock/skills |
| 2 | `grill-with-docs` | Planning | mattpocock/skills |
| 3 | `writing-plans` | Planning | obra/superpowers |
| 4 | `executing-plans` | Planning | obra/superpowers |
| 5 | `brainstorming` | Planning | obra/superpowers |
| 6 | `prototype` | Planning | mattpocock/skills |
| 7 | `to-issues` | Planning | mattpocock/skills |
| 8 | `prd-to-plan` | Planning | mattpocock/skills |
| 9 | `domain-model` | Planning | mattpocock/skills |
| 10 | `preserving-productive-tensions` | Planning | obra/superpowers |
| 11 | `systematic-debugging` | Code Quality | obra/superpowers |
| 12 | `diagnose` | Code Quality | mattpocock/skills |
| 13 | `tdd` | Code Quality | obra/superpowers |
| 14 | `karpathy-guidelines` | Code Quality | multica-ai/andrej-karpathy-skills |
| 15 | `verification-before-completion` | Code Quality | obra/superpowers |
| 16 | `requesting-code-review` | Code Quality | obra/superpowers |
| 17 | `receiving-code-review` | Code Quality | obra/superpowers |
| 18 | `finishing-a-development-branch` | Code Quality | obra/superpowers |
| 19 | `improve-codebase-architecture` | Code Quality | mattpocock/skills |
| 20 | `finding-duplicate-functions` | Code Quality | obra/superpowers-lab |
| 21 | `academic-research-skills` | Research | Imbad0202/academic-research-skills |
| 22 | `academic-paper` | Research | Imbad0202/academic-research-skills |
| 23 | `academic-paper-reviewer` | Research | Imbad0202/academic-research-skills |
| 24 | `claude-scientific-writer` | Research | K-Dense-AI/claude-scientific-writer |
| 25 | `research-claim-map` | Research | lyndonkl/claude |
| 26 | `inspectional-reading` | Research | lyndonkl/claude |
| 27 | `structural-analysis` | Research | lyndonkl/claude |
| 28 | `component-extraction` | Research | lyndonkl/claude |
| 29 | `avoid-ai-writing` | Research | conorbronsdon/avoid-ai-writing |
| 30 | `autoresearch` | Research | Orchestra-Research/AI-Research-SKILLs |
| 31 | `orbital-mechanics` | Aerospace | Soljourner/claude-engineering-skills |
| 32 | `fluid-dynamics + pump-design` | Aerospace | Soljourner/claude-engineering-skills |
| 33 | `structural-analysis + FEA` | Aerospace | Soljourner/claude-engineering-skills |
| 34 | `thermodynamics` | Aerospace | Soljourner/claude-engineering-skills |
| 35 | `materials-simulation-skills` | Aerospace | HeshamFS/materials-simulation-skills |
| 36 | `handoff` | Productivity | mattpocock/skills |
| 37 | `caveman` | Productivity | mattpocock/skills |
| 38 | `session-search` | Productivity | glebis/claude-skills |
| 39 | `everything-learning` | Productivity | glebis/claude-skills |
| 40 | `retrospective` | Productivity | glebis/claude-skills |
| 41 | `dispatching-parallel-agents` | Multi-Agent | obra/superpowers |
| 42 | `subagent-driven-development` | Multi-Agent | obra/superpowers |
| 43 | `context-engineering-kit` | Multi-Agent | NeoLabHQ/context-engineering-kit |
| 44 | `compound-engineering-plugin` | Multi-Agent | EveryInc/compound-engineering-plugin |
| 45 | `AI-Research-SKILLs` | Multi-Agent | Orchestra-Research/AI-Research-SKILLs |
| 46 | `write-a-skill` | Meta | mattpocock/skills |
| 47 | `prompt-architect` | Meta | ckelsoe/prompt-architect |
| 48 | `ok-skills` | Meta | mxyhi/ok-skills |
| 49 | `academic-pipeline` | Meta | Imbad0202/academic-research-skills |
| 50 | `claude-deep-research-skill` | Meta | 199-biotechnologies |

---

## How to Install Any Skill

```bash
# Method 1 — Global install (available across all projects)
mkdir -p ~/.claude/skills/<skill-name>
curl -o ~/.claude/skills/<skill-name>/SKILL.md <raw-github-url>

# Method 2 — Plugin marketplace (Claude Code)
/plugin marketplace add <github-user>/<repo>
/plugin install <skill-name>@<marketplace-name>

# Method 3 — Clone and symlink
git clone https://github.com/<user>/<repo>.git ~/skills/<repo>
ln -s ~/skills/<repo>/<skill-folder> ~/.claude/skills/<skill-name>
```

Each skill must sit at `.claude/skills/<skill-name>/SKILL.md` for Claude Code to discover it.

---

*Compiled June 2026. Every source link verified live. Impact-ranked, no audience filter applied. No skill was included because it was popular — every skill was included because it solves a real problem engineers and researchers face repeatedly.*
