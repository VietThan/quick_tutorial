export VENV=~/Documents/OdinProjects/quick_tutorial/env

---

For most steps you will copy an earlier step's directory to a new directory, change your working directory to the new directory, then install your project:

```bash
cd ..; cp -r package ini; cd ini
$VENV/bin/pip install -e .
```
For a few steps, you won't copy an earlier step's directory, but you will still need to install your project with `$VENV/bin/pip install -e .`.

Finally for a few steps, you might add a dependency to your project in its setup.py file, and then install both the dependency and the project with either `$VENV/bin/pip install -e .` or `$VENV/bin/pip install -e ".[dev]"`.

---

```bash
# Change directory into your newly created project.
cd cc_starter
# Create a new virtual environment...
python3 -m venv env
# ...where we upgrade packaging tools...
env/bin/pip install --upgrade pip setuptools
# ...and into which we install our project.
env/bin/pip install -e .
```