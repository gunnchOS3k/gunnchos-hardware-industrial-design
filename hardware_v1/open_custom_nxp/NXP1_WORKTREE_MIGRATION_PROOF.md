# NXP-1 worktree migration proof

**Generated:** 2026-09-18T19:13:27Z  
**Campaign:** `NXP1_CPB0_OPEN_DIGITAL_EDA_CLOSURE`  
**Claim boundary:** migration evidence only — not fab / not physical / not NDA.

## Strategy

1. Created dedicated worktree/branch `hardware/nxp-open-cpb0-eda` from `origin/main` @ `4a8aefb5fd6203842267f5adbd72b8ed324e1fac`.
2. Transferred only NXP-0 delta (72 paths) from the original dirty working tree.
3. Compared: **missing=0**, present=72, zero_loss=True.
4. Left unrelated original working-tree changes untouched (no reset/clean).

## Baseline

| Field | Value |
|---|---|
| Original branch | `cursor/supervisor-ready-portfolio-release-001` |
| Original HEAD | `5a93e261fdd8187341b94100c0df20eba6bc18b1` |
| Worktree branch | `hardware/nxp-open-cpb0-eda` |
| Worktree base | `origin/main` = `4a8aefb5fd6203842267f5adbd72b8ed324e1fac` |
| PR #80 expected | `4a8aefb5fd6203842267f5adbd72b8ed324e1fac` |
| Base matches PR #80 | `True` |

## Honesty

- Original tree not destructively cleaned.
- Only NXP-0 + Makefile NXP targets entered this worktree before NXP-1 edits.
