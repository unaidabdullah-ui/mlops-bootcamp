# Stage 1: Python Fundamentals

⏱️ Suggested time: 2–3 weeks · 🎓 Learned from: CodeWithHarry, CampusX

## 🎯 Goals

By the end of this stage you can:
- Write Python with variables, loops, functions and data structures
- Model data with classes (OOP)
- Use NumPy arrays and pandas DataFrames
- Build a small CLI tool with `argparse` and `logging`

## 📂 What's Inside

| Folder | Topic |
|--------|-------|
| [`python-basics`](python-basics) | `PY_01` basics → `PY_02` OOP → `PY_03` NumPy → `PY_04` pandas → `PY_05` Matplotlib |
| [`file-organizer`](file-organizer) | CLI tool that sorts a folder's files by type, with dry-run mode and logging |

## ▶️ Run It

```bash
pip install numpy pandas matplotlib
cd python-basics && python PY_01.py

cd ../file-organizer
python organizer.py --path ~/Downloads --dry-run
```

## 🏋️ Practice

1. Add a `grade()` method to the `Student` class in `PY_02.py` that returns A/B/C based on the average.
2. In `PY_04.py`, add a column `Tax` = 10% of `Salary` and print the employees earning above the mean.
3. Add an `--undo` flag to the file organizer that moves the files back.

## 📚 Free Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Kaggle Learn: Python](https://www.kaggle.com/learn/python)
- [NumPy: Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)

## ✅ Checklist

- [ ] I can write functions and classes without looking up syntax
- [ ] I can load, filter and summarize data with pandas
- [ ] I built a CLI tool that takes arguments

**Next →** [Stage 2: Linux & Shell](../02-linux-shell)
