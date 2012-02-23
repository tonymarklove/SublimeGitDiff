SublimeGitDiff
----

SublimeGitDiff is a plugin for Sublime Text 2 which allows you to easily resolve
Git merge conflicts using your favourite external merge tool.


Requirements
---

1. Sublime Text 2 [http://www.sublimetext.com]
2. Git [http://git-scm.org]
3. Your favourite merge tool*

* Tested with SourceGear DiffMerge [http://www.sourcegear.com/diffmerge]


Getting Started
---

1. Clone the repository or simply grab the latest copy of git_diff.py.

2. Copy git_diff.py into your Sublime Text packages directory. If you are not
   sure where this is, open up Sublime and go to the Preferences menu, then
   Browse Packages.

3. Configure your merge tool using the instructions below.

4. Add the following key bindings to Sublime. (You are obviously free to
   change the specific key combinations.)

	{ "keys": ["ctrl+shift+r"], "command": "highlight_unified_diff" },
	{ "keys": ["ctrl+shift+g", "ctrl+m"], "command": "region_merge" },
	{ "keys": ["ctrl+shift+g", "ctrl+r"], "command": "region_merge_result" }


When You Have a Conflict
---

1. Open the conflicted file in Sublime.

2. Hit ctrl+shift+r to select the first conflicted region.

3. Hit ctrl+shift+g then ctrl+m to run the merge tool.

4. Save the resolved file in your merge tool.

5. Back in Sublime, press ctrl+shift+g then ctrl+r to paste the result.

6. Repeat for further conflicts.


Merge Tool Configuration
---

To change the path to your merge tool set the MERGEPROG variable.

If you are using something other than SourceGear DiffMerge you may also need to
tweak the command line for the merge tool:

Search for the line containing "Popen". This should be the last line of the
RegionMergeCommand function. This line simply runs the executable defined by
MERGEPROG with three files as arguments. These files contain: our changes, the
common ancestor, and their changes.
