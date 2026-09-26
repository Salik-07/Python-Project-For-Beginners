---
name: repair-codex-windows-git-access
description: Troubleshoot Codex on Windows when Git cannot create .git/index.lock or the elevated sandbox fails opening .sandbox-bin. Use for these permission errors in chats or scheduled tasks, not for ordinary merge or authentication failures.
---

# Repair Codex Windows Git access

This file is self-contained so it can be uploaded to another assistant. Diagnose the machine in front of you; do not assume that a past user's ACL entries or configuration apply. Explain proposed permission changes before making them.

## Identify the failing boundary

| Error or observation | What to investigate |
| --- | --- |
| `git add` reports `.git/index.lock: Permission denied` | Git cannot write repository metadata. Check for an active/stale lock, Windows ACLs, and Codex filesystem permissions. |
| Codex reports `helper_sandbox_lock_failed` while opening `.codex\.sandbox-bin` | The elevated Windows sandbox failed to initialize. This is separate from a repository's `.git` ACL. |
| Staging works but `git push` fails | Check remote URL, authentication, command rules, and network policy. Do not change ACLs for a network failure. |

Ask for the exact failing command and full error. If the assistant has no local shell, ask the user to run the commands and paste the results. A successful Git write in ordinary PowerShell does not prove the Codex sandbox identity can write.

## Inspect the Git write failure

Run these read-only commands in PowerShell, replacing the repository path:

```powershell
$repo = 'C:\path\to\repository'
$gitDir = (git -C $repo rev-parse --absolute-git-dir).Trim()
git -C $repo status --short --branch
Test-Path -LiteralPath (Join-Path $gitDir 'index.lock')
Get-Process git -ErrorAction SilentlyContinue
whoami /user
whoami /groups
icacls $repo
icacls $gitDir
$acl = Get-Acl -LiteralPath $gitDir
$acl.Access | Where-Object { $_.AccessControlType -eq 'Deny' -and -not $_.IsInherited } |
    Format-Table IdentityReference, FileSystemRights, InheritanceFlags, PropagationFlags
```

If `index.lock` exists, establish whether a running Git process owns it. Remove a stale lock only after confirming no process is using it. If no lock exists, compare the repository root and `.git` ACLs. Explicit Deny access control entries can override inherited Modify grants for the Codex sandbox identity. Also inspect the active Codex permission profile and command rules in `config.toml`: the workspace and `.git` need appropriate write access, but that configuration cannot override a Windows ACL denial. Scheduled tasks may have different effective settings from an interactive chat.

A narrow temporary write test inside `.git` from both ordinary PowerShell and Codex can separate an ACL or sandbox issue from a general filesystem issue. Remove the test file afterward. Do not create a Git commit merely to test write access.

## Repair only confirmed ACL entries

If inspection proves specific explicit Deny entries are the blocker:

1. Save the existing ACL outside the repository: `$backupPath = Join-Path $env:TEMP ("git-acl-{0}.txt" -f (Get-Date -Format "yyyyMMdd-HHmmss")); icacls $gitDir /save $backupPath`. Keep the backup until the repair is verified.
2. Record the exact affected identities, rights, inheritance flags, and number of rules. Select only those explicit Deny rules with `Get-Acl`; show the selected rules and check their count before changing anything. Do not copy SIDs from another person's machine.
3. In regular PowerShell if Codex cannot edit the ACL, call `RemoveAccessRuleSpecific` only on the reviewed rules, then `Set-Acl -LiteralPath $gitDir -AclObject $acl`. Do not reset the entire ACL or apply broad recursive grants.
4. Run `icacls $gitDir` again and verify the intended Deny entries are gone and other entries remain. Then retry the exact Git staging command with explicitly selected files. Inspect `git diff --cached --name-only`.

Here is the core of a targeted repair **after** the identities and expected count have been determined from that machine:

```powershell
$acl = Get-Acl -LiteralPath $gitDir
$targetIdentities = @('REPLACE_WITH_VERIFIED_IDENTITY')
$expectedCount = 0 # REPLACE with the verified positive number
if ($targetIdentities -contains 'REPLACE_WITH_VERIFIED_IDENTITY' -or $expectedCount -le 0) {
    throw 'Set and verify target identities and expected count first.'
}
$rules = @($acl.Access | Where-Object {
    $_.AccessControlType -eq 'Deny' -and
    -not $_.IsInherited -and
    $targetIdentities -contains $_.IdentityReference.Value
})
$rules | Format-List IdentityReference, FileSystemRights, InheritanceFlags, PropagationFlags
if ($rules.Count -ne $expectedCount) { throw "Expected $expectedCount deny entries; found $($rules.Count)" }
# Stop here and review every listed rule before running the following lines.
foreach ($rule in $rules) { $acl.RemoveAccessRuleSpecific($rule) }
Set-Acl -LiteralPath $gitDir -AclObject $acl -ErrorAction Stop
```

## Handle an elevated sandbox startup failure separately

Inspect the error in `$HOME\.codex\.sandbox\setup_error.json` and the ACL on `$HOME\.codex\.sandbox-bin`. Consult current [OpenAI Windows sandbox guidance](https://learn.chatgpt.com/docs/windows/windows-sandbox). `[windows] sandbox = "unelevated"` is a documented fallback when elevated setup fails, with weaker isolation. Save `config.toml`, fully quit Codex, and reopen it before retesting. This fallback does not repair an unrelated `.git` Deny ACE.

Check network settings before changing backends. With `network.enabled = true` and `features.network_proxy = false`, commands have direct unrestricted network access; configured domain allow rules are inactive. Do not disable the proxy silently to make a push work. Explain that security change and get the user's decision. Prefer restoring the elevated backend and active proxy when feasible. See [OpenAI Permissions](https://learn.chatgpt.com/docs/permissions).

## Finish

Report the confirmed cause, exact ACL or configuration changes, whether staging and pushing were actually tested, and remaining security tradeoffs. Avoid committing or pushing unless the user's task authorizes it. A successful interactive command does not by itself prove a scheduled task will work; check a later run when relevant.

