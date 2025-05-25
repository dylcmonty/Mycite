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
IP-Notes:
The Apache License 2.0:
    Allows anyone to use, modify, distribute, and commercialize your software.
    Requires:
        Attribution (they must keep your copyright notice)
        NOTICE file if you include one
    Includes an explicit patent license (if you hold patents on the tech, you’re giving users permission to use them under the license)
    Protects you from liability (no warranty)
This makes it a permissive but protective license — very popular with big companies and public agencies.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
General Notes:
This is an outline for a medium sized project.
Small project may only be one file.
Determine where to break functionality into packages of modules
	Possibly with API, core, models, or tests.
Eventually have program start by selecting set up in terminal then loading the GUI, assets, and connecting.
	to services; then I'm starting with whats like the assets load functions.
CLI tools to parse command-line arguments
Web server tools to start listening for HTTP requests (e.g. launch flask or Django server)
Data pipelines tools to begin ETL process (extract, transform, load)
