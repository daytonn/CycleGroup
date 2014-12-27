import sublime
import sublime_plugin


class ToggleGroupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        group = self.view.window().active_group()
        side = "Left" if group == 1 else "Right"

        if group == 1:
            self.view.window().focus_group(0)
        else:
            self.view.window().focus_group(1)

        sublime.status_message("%{side} Pane Activated" % locals())
