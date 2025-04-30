import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "utils")))
import requests
from utils.grading_utils import grade_website, TAG_COLUMN_NAMES

def print_checklist(tag_scores):
    for tag, label in TAG_COLUMN_NAMES.items():
        check = "✔️ " if tag_scores[label] else "❌"
        print(f"\t {check} {label}")

def grade_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        html = response.text
        scores, tag_results = grade_website(html, url if url.endswith('/') else url + '/')

        # Compute project grade
        base_score = scores['Reachable'] + scores['Line Count >= 50'] + scores['Line Count > 100'] + scores['CSS Used']
        tag_score = min(sum(scores[col] for col in TAG_COLUMN_NAMES.values()), 10)
        total_grade = base_score + tag_score

        print(f"\n🎓 Grading results for: {url}")
        print(f"{'-'*50}")
        reachable = "✅" if scores['Reachable'] == 60 else "❌"
        linecount = "✅" if scores['Line Count'] >= 50 else "❌"
        line_50 = "✅" if 50 <= scores['Line Count'] else "❌"
        line_100 = "✅" if 100 < scores['Line Count'] else "❌"
        css = "✅" if scores['CSS Used'] == 10 else "❌"
        tags = "✅" if tag_score >= 10 else "❌"

        print(f"{reachable} Website Hosted on the Storm Server: {scores['Reachable']} pts")
        print(f"{linecount} Line Count: {scores['Line Count']} lines")
        print(f"\t {line_50} Line Count >= 50: {scores['Line Count >= 50']} pts")
        print(f"\t {line_100} Line Count > 100: {scores['Line Count > 100']} pts")
        print(f"{css} CSS Used: {scores['CSS Used']} pts")
        print(f"{tags} Tag Points: {tag_score} pts")

        print_checklist(scores)

        print(f"\n📊 Final Project Grade: {total_grade}/100")

        if total_grade == 100:
            print("🌟 Perfect score! Great job!\n")
        elif total_grade >= 80:
            print("👍 Solid work! Just a few things missing.\n")
        else:
            print("🛠️ Needs improvement. Check the missing items above.\n")

    except Exception as e:
        print(f"❌ Failed to grade URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python grade_single.py <URL>")
        sys.exit(1)
    grade_url(sys.argv[1])
