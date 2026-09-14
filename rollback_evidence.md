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
