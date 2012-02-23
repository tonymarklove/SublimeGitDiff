import sublime, sublime_plugin, tempfile, os, string, re
from subprocess import Popen

MERGEPROG = '"%s\SourceGear\DiffMerge\DiffMerge.exe"' % os.environ['ProgramFiles']

class HighlightUnifiedDiffCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()

		if len(sel) > 1:
			return

		searchFrom = 0 if len(sel) < 1 else sel[0].b

		start = self.view.find("^<<<<<<<", searchFrom)

		if start == None:
			start = self.view.find("^<<<<<<<", 0)

		if start == None:
			return

		end = self.view.find("^>>>>>>>", start.b)

		if end == None:
			return

		region = sublime.Region(start.a, end.b)
		region = self.view.full_line(region)

		sel.clear()
		sel.add(region)
		self.view.show(region)


class RegionMergeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()

		if len(sel) > 1:
			return

		start = self.view.full_line(sel[0].a).b
		end = self.view.full_line(sel[0].b-1).a - 1
		region = sublime.Region(start, end)
			
		unified = self.view.substr(region)
		unified = unified.split("=======\n")

		theirs = unified[1]

		unified = re.split('\|\|\|\|\|\|\|.*\n', unified[0])
		#print unified[0]

		ours = unified[0]
		common = unified[1]

		ourFile = os.path.join(tempfile.gettempdir(), 'sublime-ours')
		commonFile = os.path.join(tempfile.gettempdir(), 'sublime-common')
		theirFile = os.path.join(tempfile.gettempdir(), 'sublime-theirs')
		
		with open(ourFile, mode='w') as f:
			f.write(ours.encode("utf-8"))

		with open(commonFile, mode='w') as f:
			f.write(common.encode("utf-8"))

		with open(theirFile, mode='w') as f:
			f.write(theirs.encode("utf-8"))

		Popen('%s "%s" "%s" "%s"' % (MERGEPROG, ourFile, commonFile, theirFile))


class RegionMergeResultCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()

		if len(sel) > 1:
			return

		commonFile = os.path.join(tempfile.gettempdir(), 'sublime-common')

		with open(commonFile, mode='r') as f:
			self.view.replace(edit, sel[0], f.read())