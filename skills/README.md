# Agent skill

[`grabblist-research`](grabblist-research/SKILL.md) is a portable Markdown playbook for agents using the hosted Grabblist MCP.

It contains no credentials and does not install or run the MCP service. Connect the remote endpoint separately, then make the skill directory available through your agent host's normal skill-loading mechanism.

The format uses a `SKILL.md` file with YAML frontmatter plus references and reusable output templates. Hosts that do not support skill discovery can still use the files as ordinary instructions.
