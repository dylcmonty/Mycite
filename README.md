readme.txt

/ProjectFolder
  ├── main.py		# Entry point script - only if needed
  ├── boot.py		# Logic modules: classes, functions, utilities, ect.
  ├── __init__.py	# Makes program a package.
  ├── readme.txt	# This file
  ├── OperatingSystem/	# Specialized directory
  ├── Hardware/		# Specialized directory
  └── assets/		# Optional specialized module directory with __init__.py to group modules in packages.
	  ├── bloom/	# [Add caption here]
	  ├── hyphae/	# [Add caption here]
	  └── KatBots/	# [Add caption here]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
General Python Notes:

This is an outline for a medium sized project.
Small project may only be one file.
Large projects break functionailty into packages of modules, and so they contain
	the files and a __init__.py file inside a folder to create these. Large
	projects may have compentes like api, core, models, or tests.
You will always need a "start here" point if you are running a CLI or lauching
	an aplication. You want to keep imports cleaer by having a clean start
	up sequence.
If an app starts at the start point by loading the GUI, assets, and connecting 
	to services; then I'm starting with whats like the assets load functions.
CLI tools: parse command-line arguments, dsibatch, commands (e.g. git status)
Desktop apps: initialize window, load first page/screen
Web server:start listening for HTTP requests (e.g. launch flask or Django server)
Data pipelines: begin ETL process (extract, transform, load)
