CycleGroup
==================

Have you ever just wanted a hotkey to cycle the focus from one group to the next? How about simply moving a file to the opposite group? Well, now you can with CycleGroup.

Installation
------------

Install with Package Control or clone the repository:

```sh
git clone git@github.com:daytonn/CycleGroup.git ~/Library/Application\ Support/Sublime\ Text\ 3/Installed\ Packages/CycleGroup
```

Keybindings
-----------

`super+\` (`⌘+\`) will cycle the focused group (a group is a division of tabs in Sublime). For exampe if you have two groups, one on the left, and one on the right, and the cursor is in a file in the first group. Pressing `super+\` will focus the open file in the second group.

`shift+super+\` (`⇧+⌘+\`) will move the currently focused file, to the next group. For example if you have two groups, one on the left, and one on the right, and the cursor is in a file in the first group. Pressing `shift+super+\` will move the file to then second group.

![](https://raw.githubusercontent.com/daytonn/CycleGroup/master/cycle-group.gif)