# Git workflow log

Commands run for Experiment 4, Part A (Steps 7–12), with their actual output.

```text
$ git init
Initialized empty Git repository in D:/7KLH/S2-Even/DLAC/Exp/E4/Experiment-4-PyTorch-CUDA/.git/

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore
	README.md
	inference.py
	models/
	notebooks/
	requirements.txt
	train.py

nothing added to commit but untracked files present (use "git add" to track)

$ git add .
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'inference.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'train.py', LF will be replaced by CRLF the next time Git touches it

$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .gitignore
	new file:   README.md
	new file:   inference.py
	new file:   models/.gitkeep
	new file:   notebooks/E4_PyTorch_CUDA_Setup.ipynb
	new file:   requirements.txt
	new file:   train.py


$ git commit -m Initial project repository
[master (root-commit) 280843c] Initial project repository
 7 files changed, 574 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 inference.py
 create mode 100644 models/.gitkeep
 create mode 100644 notebooks/E4_PyTorch_CUDA_Setup.ipynb
 create mode 100644 requirements.txt
 create mode 100644 train.py

$ git branch -M main

$ git log --oneline
280843c Initial project repository

$ git branch
* main

```
