import sublime_plugin


class CycleGroupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        num_groups = self.view.window().num_groups() - 1
        active_group = self.view.window().active_group()
        next_group = active_group + 1
        if (next_group > num_groups):
            next_group = 0

        self.view.window().focus_group(next_group)
