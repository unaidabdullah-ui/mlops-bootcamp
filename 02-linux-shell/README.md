# Stage 2: Linux & Shell Scripting

⏱️ Suggested time: 1–2 weeks · 🎓 Learned from: TrainWithShubham

## 🎯 Goals

By the end of this stage you can:
- Move around Linux and use core commands (`find`, `grep`, pipes)
- Write Bash scripts with variables, conditions and exit codes
- Automate model training and Docker deployment with scripts

## 📂 What's Inside

| Folder | Topic |
|--------|-------|
| [`00_basics`](00_basics) | First scripts, variables |
| [`01_linux_commands`](01_linux_commands) | `scan_datasets.sh`: list every file in a data folder |
| [`02_variables_and_conditions`](02_variables_and_conditions) | `check_env.sh`: verify Python and Docker are installed |
| [`03_ml_training_automation`](03_ml_training_automation) | `train_model.sh`: run training and fail loudly on errors |
| [`04_docker_and_deployment_scripts`](04_docker_and_deployment_scripts) | `deploy.sh`: build and run a Docker image |

## ▶️ Run It

Use Linux, macOS, WSL or Git Bash:

```bash
bash 00_basics/01_hello.sh
bash 01_linux_commands/scan_datasets.sh ../03-data-handling
bash 02_variables_and_conditions/check_env.sh
```

All scripts are checked with [ShellCheck](https://www.shellcheck.net/) in CI.

## 🏋️ Practice

1. Make `scan_datasets.sh` also print each file's size (`du -h`).
2. Make `check_env.sh` also check for `git` and `kubectl`.
3. Add a `set -euo pipefail` line to every script and explain what each flag does.

## 📚 Free Resources

- [Linux Journey](https://linuxjourney.com/)
- [Bash Guide for Beginners (TLDP)](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [ShellCheck](https://www.shellcheck.net/): paste a script, get its bugs

## ✅ Checklist

- [ ] I can find files and search inside them from the terminal
- [ ] I can write a script that exits non-zero on failure
- [ ] I automated a build or deploy step with Bash

**← Previous** [Stage 1: Python](../01-python) · **Next →** [Stage 3: Data Handling](../03-data-handling)
