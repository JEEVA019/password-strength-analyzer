#!/usr/bin/env python3
"""
Password Strength Analyzer
Author: Jeeva R
Description: Analyzes password strength based on security best practices.
             Demonstrates security awareness, string analysis, and Python logic.
"""

import re
import string
import argparse
from datetime import datetime

# Common weak passwords list
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567890", "111111",
    "iloveyou", "welcome", "login", "passw0rd", "master",
    "hello", "dragon", "sunshine", "princess", "football"
]

def check_length(password):
    """Check password length score."""
    length = len(password)
    if length >= 16:
        return 3, "Excellent length (16+ chars)"
    elif length >= 12:
        return 2, "Good length (12-15 chars)"
    elif length >= 8:
        return 1, "Minimum length (8-11 chars)"
    else:
        return 0, "Too short (under 8 chars) — FAIL"

def check_complexity(password):
    """Check character variety."""
    score = 0
    feedback = []

    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Has uppercase letters")
    else:
        feedback.append("Missing uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Has lowercase letters")
    else:
        feedback.append("Missing lowercase letters")

    if re.search(r'\d', password):
        score += 1
        feedback.append("Has numbers")
    else:
        feedback.append("Missing numbers")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Has special characters")
    else:
        feedback.append("Missing special characters")

    return score, feedback

def check_patterns(password):
    """Detect weak patterns."""
    issues = []

    if re.search(r'(.)\1{2,}', password):
        issues.append("Contains repeated characters (e.g. aaa, 111)")

    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        issues.append("Contains sequential numbers")

    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
        issues.append("Contains sequential letters")

    if password.lower() in COMMON_PASSWORDS:
        issues.append("This is a commonly used password — extremely weak!")

    if re.search(r'(password|admin|login|user|welcome)', password.lower()):
        issues.append("Contains common weak keywords")

    return issues

def estimate_crack_time(score):
    """Rough estimate of crack time based on score."""
    estimates = {
        0: "Instantly",
        1: "Less than 1 minute",
        2: "A few hours",
        3: "Several days",
        4: "Weeks to months",
        5: "Years",
        6: "Decades",
        7: "Centuries+"
    }
    return estimates.get(min(score, 7), "Unknown")

def analyze_password(password):
    """Run full password analysis."""
    print(f"\n{'='*55}")
    print(f"  Password Strength Analyzer — by Jeeva R")
    print(f"{'='*55}")
    print(f"  Analyzed : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Password : {'*' * len(password)} ({len(password)} chars)")
    print(f"{'='*55}\n")

    total_score = 0

    # Length check
    length_score, length_msg = check_length(password)
    total_score += length_score
    print(f"  [LENGTH]")
    print(f"    {length_msg}")

    # Complexity check
    complexity_score, complexity_feedback = check_complexity(password)
    total_score += complexity_score
    print(f"\n  [COMPLEXITY]")
    for item in complexity_feedback:
        symbol = "+" if "Has" in item else "-"
        print(f"    [{symbol}] {item}")

    # Pattern check
    pattern_issues = check_patterns(password)
    print(f"\n  [PATTERN ANALYSIS]")
    if pattern_issues:
        for issue in pattern_issues:
            print(f"    [-] {issue}")
            total_score -= 1
    else:
        print(f"    [+] No weak patterns detected")
        total_score += 1

    # Final score
    total_score = max(0, total_score)
    crack_time = estimate_crack_time(total_score)

    if total_score >= 7:
        strength = "VERY STRONG"
        bar = "##########"
    elif total_score >= 5:
        strength = "STRONG"
        bar = "########  "
    elif total_score >= 4:
        strength = "MODERATE"
        bar = "######    "
    elif total_score >= 2:
        strength = "WEAK"
        bar = "###       "
    else:
        strength = "VERY WEAK"
        bar = "#         "

    print(f"\n{'='*55}")
    print(f"  RESULT    : {strength}")
    print(f"  SCORE     : {total_score}/8")
    print(f"  STRENGTH  : [{bar}]")
    print(f"  EST. CRACK: {crack_time}")
    print(f"{'='*55}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Analyzer — Educational Tool by Jeeva R"
    )
    parser.add_argument(
        "-p", "--password",
        help="Password to analyze (wrap in quotes)",
        type=str
    )
    args = parser.parse_args()

    if args.password:
        analyze_password(args.password)
    else:
        print("\n  Password Strength Analyzer — by Jeeva R")
        print("  ----------------------------------------")
        while True:
            password = input("\n  Enter password to analyze (or 'quit' to exit): ")
            if password.lower() == 'quit':
                print("\n  Exiting. Stay secure!\n")
                break
            if not password:
                print("  Please enter a password.")
                continue
            analyze_password(password)

if __name__ == "__main__":
    main()
