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
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

colors = {
    'background': '#282a36',
    'current-line': '#44475a',
    'foreground': '#ffffff',
    'comment': '#6272a4',
    'cyan': '#8be9fd',
    'green': '#50fa7b',
    'orange': '#ffb86c',
    'pink': '#ff79c6',
    'purple': '#bd93f9',
    'dark_gray': '#191a21',
    'red': '#ff5555',
    'yellow': '#f1fa8c',
    'lighter_gray': '#a9a9a9',
}

font_size = 20
widget_font_size = 12
mod = 'mod4'
terminal = guess_terminal() 


@hook.subscribe.startup_once
def start_picom():
    home = os.path.expanduser('~')
#     subprocess.Popen(['/usr/bin/picom --experimental-backends'])
    subprocess.Popen(['killall pulseaudio', '&' ,'/usr/bin/pulseaudio', '--start'])

@hook.subscribe.client_new
def window_to_group(window):
    if window.window.get_wm_class() in [
            ('qutebrowser', 'qutebrowser'),
            ('Xephyr', 'Xephyr'),
            ('google-chrome', 'Google-chrome'),
            ]:
        window.togroup('u')
    elif (window.window.get_wm_class() == ('st-256color', 'st-256color')) and (window.window.get_name() == 'weechat'): 
        window.togroup('o')
    elif (window.window.get_wm_class() == ('st-256color', 'st-256color')) and (window.window.get_name() == 'ranger'): 
        window.togroup('p')
    elif window.window.get_wm_class() in [
            ('st-256color', 'st-256color'),
            ('code', 'Code'), 
            ('subl','Subl'),
            ]:
        window.togroup('i')
    elif window.window.get_wm_class() in [
            ('skype', 'Skype'), 
            ('slack', 'Slack'),
            ]:
        window.togroup('o')
    else:
        window.togroup('p')

def spawn_icon(symbol_hex, foreground='#f8f8f2', fontsize=font_size):
    w = widget.TextBox(
        text=symbol_hex,
        fontsize=fontsize,
        padding=5,
        foreground=foreground,
        background=colors['current-line'],
    )

    return w

def launch_widgets():

    widgets = [
        widget.GroupBox(
            urgent_alert_method='block',
            highlight_method='block',
            rounded=False,
            disable_drag=True,
            this_screen_border=colors['background'],
            this_current_screen_border=colors['purple'],
            other_screen_border=colors['dark_gray'],
            other_current_screen_border=colors['dark_gray'],
            urgent_border=colors['red'],
            inactive=colors['current-line'],
            fontsize=font_size,
            padding_y=5,
            padding_x=8,
        ),
        widget.WindowName(
            foreground=colors['lighter_gray'],
        ),
        widget.Spacer(),
        widget.CurrentLayout(
            foreground=colors['lighter_gray'],
        ),
        widget.TextBox('\uf438', foreground=colors['current-line'], padding=-12, fontsize=62),
        spawn_icon('\uf2c9', fontsize=14),
        widget.ThermalSensor(
            tag_sensor='Tctl',
            background=colors['current-line'],
            update_interval=1,
        ),
        spawn_icon('\ue266'),
        widget.Memory(
            format='{MemUsed} MB',
            background=colors['current-line']
        ),
        spawn_icon('\uf85a'),
        widget.CPU(
            format='{load_percent}%', 
            background=colors['current-line']
        ),
        spawn_icon('\ufa7d'),
        widget.Volume(
            cardid=1,
            step=2,
            background=colors['current-line']
        ),
        widget.TextBox(
            '\uf438', 
            foreground=colors['background'], 
            background=colors['current-line'],  
            padding=-12, 
            fontsize=62
        ),
        widget.Clock(
            background=colors['background'], 
            format='%A,%e %b. %H:%M:%S',
            foreground=colors['foreground'])
    ]
            
    return widgets 

xephyr_command = "/home/eric/projects/qtile/scripts/xephyr -c /home/eric/projects/qtile/libqtile/resources/default_config.py"

dmenu_command = """
    dmenu_run -i -fn "mononoki nerd font mono-9" \
            -nb "#282a36" \
            -nf "#f8f8f2" \
            -sb "#ff5555" \
            -h 25 \
            -p Run 
    """

keys = [
    # Move around windows
    Key([mod], 'x', lazy.spawn('xterm -e {}'.format(xephyr_command))),
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'k', lazy.layout.down()),
    Key([mod], 'j', lazy.layout.up()),
    Key([mod], 'l', lazy.layout.right()),

    # Next screen
    Key([mod], 'period', lazy.next_screen()),
    
    # Toggle fullscreen
    Key([mod], 'f', lazy.window.toggle_fullscreen()),

    # Toggle floating 
    Key([mod], 'space', lazy.window.toggle_floating()),

    # Launch qutebrowser
    Key([mod], 'b', lazy.spawn('qutebrowser')),

    # Launch ranger
    Key([mod], 'm', lazy.spawn('st -e weechat')),
    Key([mod], 'e', lazy.spawn('st -e ranger')),

    # Switch between windows in current stack pane
    Key([mod], 'k', lazy.layout.down(),
        desc='Move focus down in stack pane'),
    Key([mod], 'j', lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Resize windows
    Key([mod, 'shift'], 'k', lazy.layout.shrink()),
    Key([mod, 'shift'], 'j', lazy.layout.grow()),
    Key([mod, 'shift'], 'h', lazy.layout.normalize()),

    # Move windows up or down in current stack
    Key([mod, 'control'], 'k', lazy.layout.shuffle_up(),
        desc='Move window down in current stack '),
    Key([mod, 'control'], 'j', lazy.layout.shuffle_down(),
        desc='Move window up in current stack '),
    Key([mod, 'control'], 'h', lazy.layout.swap_left(),
        desc='Move window up in current stack '),
    Key([mod, 'control'], 'l', lazy.layout.swap_right(),
        desc='Move window up in current stack '),

    # Swap panes of split stack
    Key([mod, 'shift'], 'space', lazy.layout.rotate(),
        desc='Swap panes of split stack'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with # multiple stack panes

    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    Key([mod, 'control'], 'r', lazy.restart(), desc='Restart qtile'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown qtile'),
    Key([mod], 'n', lazy.spawn(dmenu_command)),
    Key([mod], 'r', lazy.spawn('rofi -show drun -show-icons')),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set 'Master' 1%+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer set 'Master' 1%-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer set 'Master' toggle")
    ),
    Key([mod], 'Tab', lazy.group.next_window(), lazy.window.bring_to_front()),
]

default_groups_config = {
    'persist': True
} 

default_layout_config = {
    'border_width': 1,
    'border_focus': colors['foreground'], 
    'border_normal': colors['comment'],
}

groups = [
    Group(
        name='u', 
        label='\ue743',
        exclusive=True,
        **default_groups_config
    ),
    Group(
        name='i', 
        label='\ue795',
        exclusive=True,
        **default_groups_config
    ),
    Group(
        name='o', 
        label='\uf9b0',
        layouts=[
            layout.Floating(
            ),
        ],
        **default_groups_config
    ),
    Group(
        name='p', 
        label='\ufc6e',
        layouts= [
            layout.Floating(
            ),    
        ],
        **default_groups_config
        ) 
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
            desc='Switch to & move focused window to group {}'.format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

monadtall_config = {
    'margin': 10,
    'single_margin': 0,
    'single_border_width': 0,
}

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(
        **default_layout_config,
        **monadtall_config,
        name='MonadTall',
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='mononoki nerd font mono',
    fontcolor=colors['foreground'],
    fontsize=widget_font_size,
    padding=10,
)

extension_defaults = widget_defaults.copy()

default_bar_config = {
    'size': 25,
    'background': colors['background'],
    'opacity': .95
}

screens = [
    Screen(
        top = bar.Bar(
                widgets=launch_widgets(),
                **default_bar_config
            ),
    ),
    Screen(
        top=bar.Bar(
            widgets=launch_widgets(),
            margin=[0, 0, 90, 0],
            **default_bar_config,
            ), 
        left=bar.Gap(100),
        right=bar.Gap(100),
        bottom=bar.Gap(90),
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
    Match(wm_type='utility'),
    Match(wm_type='notification'),
    Match(wm_type='toolbar'),
    Match(wm_type='splash'),
    Match(wm_type='dialog'),
    Match(wm_class='file_progress'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Xephyr'),
    Match(title='Skype'),
    Match(title='weechat'),
    Match(title='Slack'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "qtile"
