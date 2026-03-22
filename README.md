# password-strength-analyzer

A Python tool that analyzes password strength based on cybersecurity best practices — length, complexity, pattern detection, and common password checking.

## What it does
- Scores password length, complexity and patterns
- Detects weak patterns — sequential chars, repeated chars, common keywords
- Checks against a list of the most commonly used passwords
- Estimates crack time based on overall score
- Runs interactively or via command line argument

## Skills demonstrated
- Security awareness (OWASP password guidelines)
- String analysis and regex pattern matching
- CLI tool design with argparse
- Python logic and control flow

## Usage
```bash
# Interactive mode
python3 analyzer.py

# Single password via argument
python3 analyzer.py -p "MyP@ssw0rd123"
```

## Example output
```
=======================================================
  Password Strength Analyzer — by Jeeva R
=======================================================
  Analyzed : 2025-04-17 11:00:01
  Password : ************* (13 chars)
=======================================================

  [LENGTH]
    Good length (12-15 chars)

  [COMPLEXITY]
    [+] Has uppercase letters
    [+] Has lowercase letters
    [+] Has numbers
    [+] Has special characters

  [PATTERN ANALYSIS]
    [+] No weak patterns detected

=======================================================
  RESULT    : STRONG
  SCORE     : 6/8
  STRENGTH  : [########  ]
  EST. CRACK: Decades
=======================================================
```

## Tools & concepts
`Python` `Regex` `Security Awareness` `OWASP` `Password Policy` `Penetration Testing`

## Author
**Jeeva R** — Aspiring Penetration Tester | [LinkedIn](https://www.linkedin.com/in/jeeva-r-171783232/) | [TryHackMe](https://tryhackme.com)
