# Unnderstand

### GUI and CLI
---

#### CLU more powerful tool

show current path : `pwd`

show the file, folder, etc : `ls`

make folder : `mkdir` 

example:
```
mkdir folder_name
```
move specific path : `cd`

example:
```
cd folder_name
```

move to previous one step back : `cd ..`


make file : `touch`

example:
```
touch test.py
```
Remove file : `rm test.py`

```
rm test.py
```

Remove folder force way :  `rm -rf folder_name`






# **Codespace এর ভিতরে Flask\_3 নামে folder create করে ওর ভিতরে code করা** একদম easy — **pure legit workflow**।

চলো step by step dekhi **VS Code Codespace থেকে Flask\_3 project create করা আর code করা কিভাবে কাজ করে** ⬇️



## ✅ Step-by-Step Guide (inside Codespace):

### 🪄 Step 1: Folder Create Koro

VS Code terminal (bash/pwsh/zsh) open করে লেখো:

```bash
mkdir Flask_3
cd Flask_3
```

🟢 এখন তুমি Flask\_3 ফোল্ডারের ভিতরে চলে আসছো।

---

### 🪄 Step 2: Virtual Environment বানাও (optional but good)

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/mac (used in Codespaces)
```

✅ Terminal prompt: `(.venv) @Faysal3010 ➜ /workspaces/Python_Project/Flask/Flask_3`

---

### 🪄 Step 3: Flask install করো

```bash
pip install flask
```

(চাইলে `requirements.txt` বানিয়ে রাখো future install এর জন্য)

---

### 🪄 Step 4: Flask project শুরু করো

```bash
touch app.py  # বা VS Code e right-click > New File > app.py
```

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask_3!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 🪄 Step 5: Run Flask Server

```bash
python app.py
```

📦 VS Code Codespace এ port open করতে চাইলে নিচে popup এ "Open in Browser" দিবে। না আসলে manually port 5000 open করো।

---

### ✅ Bonus: Flask\_3 কে GitHub এ push করতে চাও?

1. Repo এর root e গিয়ে `git add Flask/Flask_3/`
2. Commit:

```bash
git add .
git commit -m "Added Flask_3 project"
git push origin main
```

---

## 🧠 Bottom Line:

| ✅ করণীয়                | ✨ Status                 |
| ---------------------- | ------------------------ |
| Flask\_3 folder create | ✅ mkdir Flask\_3         |
| Code inside it         | ✅ Yes, full support      |
| GitHub e push করা      | ✅ Easily possible        |
| VS Code integration    | ✅ 100% smooth experience |

---


rm -rf folder_name
```


#### To be more understand search to `commend line sheetsheet`
