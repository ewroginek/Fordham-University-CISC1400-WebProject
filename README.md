<img src="/utils/Logo_Fordham_University_Tagline.png" alt="Fordham University" width="700">

# 🌐 CISC 1400 Personal Website Quality Checker

This tool is designed to help **Fordham University CISC 1400 students** check the quality of their personal website projects.

You can run it on your own website to find out:
- If all the key HTML tags covered in class have been included
- If your hyperlinks and image source paths are working
- If your page has enough content and styling to meet the project requirements
- And what your total project grade would be!

---

## ✅ What You Need

Before using this tool, make sure you have:

1. **Python installed** on your computer  
   - Most Macs already have it (I recommend **NOT** using an iPad!)
   - On Windows, you can download it here: https://www.python.org/downloads/

2. **Download this folder**  
   - Click the green **"Code"** button, then choose **"Download ZIP"**  
   - After downloading, **unzip the folder**

---

## One-Time Setup

Open your terminal (or command prompt), navigate to your newly downloaded "Fordham-University-CISC1400-WebProject" folder using the "cd" command, and run these commands:

```bash
python -m venv venv
```

```bash
# On Mac or Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

Then install the required tools:

```bash
pip install -r requirements.txt
```

---

## How to Use

Once setup is done, just run this command with your website URL (replacing "your-username" with your username):

```bash
python grade_single.py https://storm.cis.fordham.edu/~your-username/
```

You’ll get:

- A checklist of what’s included and what’s missing
- Your total grade (out of 100)
- An example output below for your website!

```
🎓 Grading results for: https://storm.cis.fordham.edu/~your-username/
--------------------------------------------------
✅ Website Hosted on the Storm Server: 60 pts
✅ Line Count: 136 lines
         ✅ Line Count >= 50: 10 pts
         ✅ Line Count > 100: 10 pts
✅ CSS Used: 10 pts
✅ Tag Points: 10 pts
         ✔️  Used Title Tag
         ✔️  Used Header Tag
         ✔️  Used Paragraph Tag
         ✔️  Used Section Tag
         ✔️  Used Footer Tag
         ✔️  Used Hyperlink Tag
         ✔️  Used Image Tag
         ✔️  Used Unordered list Tag
         ✔️  Used Ordered list Tag
         ✔️  Used Working-urls Tag
```

---

## What's in this Folder?

| File | What it does |
|------|--------------|
| `grade_single.py` | Run this to check your website |
| `grading_utils.py` | The brains behind the checker |
| `requirements.txt` | List of tools this project needs |
| `README.md` | This help file |

---

## ❓ Help

This tool is meant to help you understand how your project is evaluated and to make sure you didn’t miss anything covered in class to create a personal and creative website!

Happy coding!
