# Rollback Evidence

## Project

A/B Test Analysis

## Purpose

This document demonstrates Git version control and rollback capability for the project.

## Stable Version

The working project was tagged as:

`v1.0`

The v1.0 tag points to the stable A/B Test Analysis application.

## Version 1.1

A harmless temporary file was added to demonstrate a version change.

Commit:

`Add temporary rollback test file`

The version was tagged:

`v1.1`

## Rollback

The latest commit was reverted using:

```bash
git revert HEAD
This generated a new rollback commit:

Revert "Add temporary rollback test file"

The rollback was pushed to the GitHub main branch using:

git push origin main
Verification

After the rollback:

The temporary test file was removed.
Git history remained intact.
The Streamlit A/B Test dashboard remained functional.
The rollback commit was visible in GitHub commit history.
Git History

The final history follows this pattern:

v1.0 — Stable working version
   ↓
v1.1 — Temporary change
   ↓
Revert — Previous change undone
Commands Used
git tag v1.0
git push origin v1.0

git add rollback_test.txt
git commit -m "Add temporary rollback test file"
git push origin main

git tag v1.1
git push origin v1.1

git revert HEAD
git push origin main
Conclusion

The project successfully demonstrates a safe and traceable rollback process using Git. Previous commits were preserved while the latest change was undone through a dedicated revert commit.
