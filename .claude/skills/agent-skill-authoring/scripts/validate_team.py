#!/usr/bin/env python3
"""Validate the project's subagents and skills. Standard library only.

Usage: python3 .claude/skills/agent-skill-authoring/scripts/validate_team.py [project_root]
Exit code 1 if any ERROR is found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[4]
AGENTS = ROOT / ".claude" / "agents"
SKILLS = ROOT / ".claude" / "skills"
ROUTING = SKILLS / "expert-team-orchestration" / "SKILL.md"
COLORS = {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
NON_EXPERTS = {"expert-orchestrator", "team-builder"}
errors, warns = [], []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: frontmatter must start on line 1 with ---")
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{path}: unterminated frontmatter")
        return {}, text
    fm, body = text[4:end], text[end + 4:]
    data, key = {}, None
    for line in fm.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            data[key] = val if val else []
        elif line.lstrip().startswith("- ") and key is not None:
            if not isinstance(data[key], list):
                data[key] = []
            data[key].append(line.strip()[2:].strip())
        else:
            errors.append(f"{path}: cannot parse frontmatter line: {line!r}")
    return data, body


skills = {}
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d}: missing SKILL.md")
        continue
    fm, body = frontmatter(f)
    name = fm.get("name", d.name)
    if name != d.name:
        errors.append(f"{f}: name '{name}' != directory '{d.name}'")
    desc = fm.get("description", "")
    if not desc:
        errors.append(f"{f}: missing description")
    if len(str(desc)) + len(str(fm.get("when_to_use", ""))) > 1536:
        warns.append(f"{f}: description + when_to_use > 1536 chars (will be truncated)")
    if len(body.splitlines()) > 500:
        warns.append(f"{f}: body > 500 lines")
    if fm.get("context") == "fork" and fm.get("agent") and not (AGENTS / f"{fm['agent']}.md").exists():
        errors.append(f"{f}: agent '{fm['agent']}' not found")
    skills[d.name] = fm

agents, used, personas = {}, {}, {}
for f in sorted(AGENTS.glob("*.md")):
    fm, body = frontmatter(f)
    name = fm.get("name")
    if not name:
        errors.append(f"{f}: missing name")
        continue
    if ":" in name or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append(f"{f}: name '{name}' must be lowercase-hyphenated without ':'")
    if f.stem != name:
        errors.append(f"{f}: file name should match name '{name}'")
    if name in agents:
        errors.append(f"{f}: duplicate agent name '{name}'")
    if not fm.get("description"):
        errors.append(f"{f}: missing description")
    if fm.get("color") and fm["color"] not in COLORS:
        errors.append(f"{f}: invalid color '{fm['color']}'")
    sk = fm.get("skills", [])
    if isinstance(sk, str):
        sk = [s.strip() for s in sk.split(",") if s.strip()]
    if len(sk) > 32:
        errors.append(f"{f}: more than 32 preloaded skills")
    for s in sk:
        if s not in skills:
            errors.append(f"{f}: preloads unknown skill '{s}'")
        elif str(skills[s].get("disable-model-invocation", "")).lower() in {"true", "yes", "on", "1"}:
            errors.append(f"{f}: skill '{s}' has disable-model-invocation and cannot be preloaded")
        used.setdefault(s, []).append(name)
    if name not in NON_EXPERTS:
        if sk[:1] != ["research-pack-citation"]:
            warns.append(f"{f}: expert should preload research-pack-citation first")
        if "Agent" not in str(fm.get("disallowedTools", "")):
            warns.append(f"{f}: expert should have disallowedTools: Agent")
    if len(body.strip()) < 200:
        warns.append(f"{f}: system prompt looks very short")
    model = str(fm.get("model", ""))
    if not (model in {"opus", "sonnet", "haiku", "fable", "inherit"} or model.startswith("claude-")):
        errors.append(f"{f}: model '{model}' missing or invalid")
    if not (ROOT / "knowledge" / name / "README.md").exists():
        errors.append(f"{f}: missing knowledge/{name}/README.md")
    if f"knowledge/{name}/" not in body:
        warns.append(f"{f}: system prompt does not tell the agent to read knowledge/{name}/")
    m = re.search(r"Your name is \*\*([^*]+)\*\*", body)
    if not m:
        warns.append(f"{f}: no Persona name")
    else:
        personas.setdefault(m.group(1), []).append(name)
    agents[name] = fm

n = len(agents)
for p, owners in personas.items():
    if len(owners) > 1:
        errors.append(f"persona name '{p}' used by {owners}")
if not 10 <= n <= 50:
    errors.append(f"team has {n} agents; expected 10-50")
for s, fm in skills.items():
    if s not in used and fm.get("context") != "fork":
        warns.append(f"skill '{s}' is not preloaded by any agent")
if ROUTING.exists():
    routing = ROUTING.read_text(encoding="utf-8")
    for a in agents:
        if a not in NON_EXPERTS and f"`{a}`" not in routing:
            errors.append(f"agent '{a}' missing from orchestrator routing table")
desc_chars = sum(len(str(fm.get("description", ""))) for fm in agents.values())
if desc_chars > 40000:
    warns.append(f"combined agent descriptions ~{desc_chars // 4} tokens; budget is 15k")

print(f"Agents: {n} | Skills: {len(skills)} | Agent description chars: {desc_chars}")
for s in sorted(used):
    print(f"  {s}: {len(used[s])} agent(s)")
for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print("OK" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
