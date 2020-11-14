# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

@hook.subscribe.startup
def autostart():
    subprocess.Popen(['picom'])

mod = "mod4"
terminal = guess_terminal()

colors = [["#292d3e", "#292d3e"],
          ["#434758", "#434758"],
          ["#ffffff", "#ffffff"],
          ["#ff5555", "#ff5555"],
          ["#8d62a9", "#8d62a9"],
          ["#667bd7", "#668bd7"],
          ["#e1acff", "#e1acff"]]

rofi_cmd = 'rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show drun'

def generate_widgets():
    w = [
        insert_separator(),
        widget.Image(
            filename='/home/eric/.config/qtile/img/arch_logo.png',
            margin=2,
            mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(rofi_cmd)}
        ),
        insert_separator(),
        widget.GroupBox(
            font='ubuntu bold',
            fontsize=9,
            highlight_method='line',
            highlight_color='161616',
            inactive='a9a9a9',
            margin_y=5,
            borderwidth=2,
            rounded=False,
        ),
        widget.Notify(
            background=colors[3]
        ),
        widget.WindowName(),
        insert_separator(),
        widget.Prompt(),
        widget.TextBox(
            text='\ue0b2',
            fontsize=20,
            foreground=colors[5],
            background=colors[0],
            padding=0
        ),
        insert_separator(bg=5),
        widget.TextBox(
            text='\uf2db',
            background=colors[5],
            fontsize=20,
        ),
        widget.Memory(
            format='{MemUsed}M/{MemTotal}M',
            background=colors[5],
        ),
        insert_separator(bg=5),
        generate_connector(bg=4, fg=5),
        insert_separator(bg=4),
        widget.TextBox(
            text='\uf85a',
            background=colors[4],
            fontsize=22,
        ),
        widget.CPU(
            format='{freq_current}GHz {load_percent}%',
            background=colors[4]
        ),
        insert_separator(bg=4),
        generate_connector(bg=5, fg=4),
        widget.TextBox(
            text=' \uf6ff',
            background=colors[5],
            fontsize=22,
        ),
        widget.Net(
            interface="enp4s0",
            padding=5,
            format='{down} \u2193 \u2191 {up}',
            background=colors[5],
        ),
        insert_separator(bg=5),
        generate_connector(bg=4, fg=5),
        widget.TextBox(
            text=' \uf64f',
            background=colors[4],
            fontsize=22,
        ),
        widget.Clock(
            background=colors[4],
            format='%b.%e  %I:%M:%S %p'
        ),
        insert_separator(bg=4),
    ]
    return w

def insert_separator(width=10, bg=0):
    w = widget.Sep(
        linewidth=0,
        padding=width,
        background=colors[bg]
    )
    return w

def generate_connector(bg, fg):
    w = widget.TextBox(
        text='\ue0c6',
        fontsize=20,
        foreground=colors[fg],
        background=colors[bg],
        padding=0
    )
    return w

keys = [
    Key([mod], 'b', lazy.spawn('qutebrowser'), desc='Qutebrowser'),

    # Settings relative to XMonadLayout

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "Up", lazy.layout.grow()),
    Key([mod], "Down", lazy.layout.shrink()),
    Key([mod], "m", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),

    # Switch screens
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),

    # Rofi
    Key([mod], "space", lazy.spawn(rofi_cmd),
        desc="Run dmenu"),

    # Spawn apps
    Key([mod], "m", lazy.spawn('konsole -e tail -c 2000 -f .local/share/qtile/qtile.log')),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Window Manipulation
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Qtile Mappings
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

letter_map = {1: 'a', 2:'s', 3:'d'}

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], letter_map[i], lazy.group[name].toscreen()))        
    keys.append(Key([mod, "shift"], letter_map[i], lazy.window.togroup(name)))

layout_theme = {
    'margin': 60,
    'border_focus': 'ffffff',
    'border_width': 1,
    'change_ratio': 0.01,
    'single_border_width': 0,
}

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='source code pro for powerline',
    fontsize=12,
    padding=5,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/Pictures/artur-sadlos-to-sh250-ooh-01-01-wip002i.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            generate_widgets(),
            24,
        ),
    ),
    Screen(
        wallpaper='~/Pictures/artur-sadlos-to-sh250-ooh-01-01-wip002i.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            generate_widgets(), 
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
