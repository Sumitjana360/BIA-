# Sales Order Python Project

A second analyst needs a small program they can run and understand without opening a notebook. This project keeps the familiar sales-order price rules in one module, one order's data and behavior in a class, and the CSV input in `data/`. The sample orders are fictional.

## What is in the folder?

| File | Job |
| --- | --- |
| `main.py` | Script to run; loads CSV rows and reports results. |
| `pricing.py` | Reusable total and order-band functions. |
| `order.py` | `SalesOrder` class for one order. You will finish it. |
| `data/S09_orders.csv` | Ten sample order records. Keep this input unchanged. |
| `README.md` | Run and Git instructions. |
| `.gitignore` | Keeps local caches, environments, and secrets out of normal Git staging. |

An order dictionary from `csv.DictReader` holds text, including numeric-looking text. `main.py` converts those values before creating each `SalesOrder`. A list then holds the ten separate objects. The class is useful here because each order's fields and calculations belong together; dictionaries and functions are also good choices for other tasks.

## Before you start

You need Python 3, a text editor, and a terminal. Git and a GitHub account are needed for the publishing part. No third-party Python packages are needed. Extract the ZIP into a normal folder outside any existing Git repository. Open a terminal **inside `sales-order-project`**, where `main.py` and `data/` are both visible.

Check the interpreter with `python --version`. If `python` is not the Python 3 command on your computer, use `py -3` on Windows or `python3` on macOS/Linux in the commands below.

## 1. Observe an import before completing the class

Run:

```text
python main.py --orientation
```

This already works. It calls `calculate_final_total` from `pricing.py` and displays `945.00` and `standard`. Notice `import pricing` near the top of `main.py` and the `pricing.calculate_final_total(...)` call. What would happen if the code were pasted into `main.py` and then changed in only one of the two files?

The ordinary `python main.py` run is **intentionally incomplete** until you finish the class. Its `NotImplementedError` points to a learner task. The `if __name__ == "__main__":` block chooses what runs when you execute this file as a script.

## 2. Build one order, then compare two

In `order.py`, complete the three numbered TODOs:

1. In `__init__`, store the five incoming values on the current object using `self`. Each order must retain its own values.
2. Make `final_total()` return the result of the imported `calculate_final_total` function for this object's values. Leave the formula in `pricing.py`.
3. Make `band()` use this object's final total with the imported `classify_order` function.

In `main.py`, complete TODO 4 in `show_two_orders()` by making two distinct `SalesOrder` instances from the indicated in-memory values. Predict their totals and bands, then run:

```text
python main.py --two
```

Check `ORD-1001` at `945.00` / `standard` and `ORD-1002` at `1181.25` / `large`. The script then changes the **first object in memory** from quantity 4 to 5. Predict its new band and check that the second object's quantity stays 5. The CSV file is not edited. Which values belong to `self` when a method runs on the first object?

## 3. Run the full project

Once the TODOs are complete, run from this project folder:

```text
python main.py
```

The script reads `data/S09_orders.csv`, converts `unit_price`, `discount_pct`, and `tax_pct` to `float` and `quantity` to `int`, then creates one object per row. It reports each order's ID, price, quantity, final total, and band. The final line should show **10 orders, 4 large, 6 standard**. `ORD-1001` and `ORD-1002` should match the two checks above. Displaying two decimal places does not round the calculated numeric value.

If the input file cannot be found, check that your terminal is in `sales-order-project` and that `data/S09_orders.csv` is present. If Python reports `ModuleNotFoundError`, check the spelling of `pricing.py` or `order.py` and run `main.py` from this folder. Save edited files before rerunning; each command starts a fresh Python process.

## 4. Record your work with Git, then publish

Git tracks local history. GitHub hosts a remote copy. A changed working file is not yet staged; `git add` stages the version you intend to commit; `git commit` records it **locally**; `git push` sends commits to GitHub. Saving, staging, or committing alone does not publish the project.

After the full run works, check `git --version`, then use a terminal in `sales-order-project`:

```text
git init
git status
git add main.py order.py pricing.py data/S09_orders.csv README.md .gitignore
git status
git commit -m "Build modular sales order project"
git branch -M main
git log --oneline
```

Inspect `git status` before staging. The CSV is fictional; never stage credentials, private data, `.env` files, or local caches. If Git asks for a commit identity, set your own name and email privately in your Git configuration, then retry the commit. Do not share credentials in class output.

Create a **new empty** repository on GitHub. Do not ask GitHub to add its own README, `.gitignore`, or license at creation. Copy its remote URL, then replace the quoted placeholder below with that URL:

```text
git remote add origin "PASTE-REMOTE-URL-HERE"
git remote -v
git push -u origin main
```

Use your configured safe GitHub authentication route, such as a credential manager or browser-based sign-in; do not put a password or token in a command, file, or screenshot. Reopen the GitHub repository and confirm the source files, CSV, README, and commit appear there. A successful local commit does not prove the push succeeded.

Improve one sentence in this README after the first push. Save it, then make a second local commit and publish it:

```text
git status
git add README.md
git commit -m "Clarify project run instructions"
git push
git log --oneline
```

For a controlled pull exercise, first confirm `git status` shows a clean working tree. Make one small **README-only** edit on GitHub, then in your local project run:

```text
git pull --ff-only
git log --oneline
```

Read the updated local README. This example assumes you made no competing local changes. If the working tree is not clean, or Git cannot fast-forward, stop and ask your trainer rather than forcing a reset.

`git init` starts tracking this existing local folder. `git clone` instead downloads an existing remote repository **and its history** into a new folder; a trainer may demonstrate cloning your published repo to a separate location. A branch is a separate line of work; recognizing `main` is enough here.

If GitHub access, authentication, or network service blocks a push, keep the working local project and commits. Later, sign in through your configured method, confirm the empty remote URL with `git remote -v`, rerun `git push -u origin main`, and verify the files and commits on GitHub. Do not treat publication as complete until that check succeeds.

## Explain your project to another analyst

Point to the file containing the price rule, the file containing one order's state and methods, the script to run, the input data, the usage notes, and the ignore rules. Then explain where a working edit, a staged change, a local commit, and the GitHub-hosted copy each live. Which one can a colleague see after a successful push?
