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


colors = {
    'background': '#282a36',
    'purple_highlight': '#bd93f9',
    'dark_gray': '#191a21',
    'urgent': '#ff5555',
    'inactive': '#44475a',
    'lighter_gray': '#a9a9a9',
    'comment': '#6272a4',
    'foreground': '#ffffff',
    'orange': '#ffb86c',
}

font_size = 20
widget_font_size = 12

@hook.subscribe.client_new
def window_to_group(window):
    if window.name == 'qutebrowser':
        window.togroup('1')
    elif window.name == 'Alacritty':
        window.togroup('2')
    elif window.name == 'Slack':
        window.togroup('3')
    elif window.name == 'Skype':
        window.togroup('3')
    else:
        window.togroup('4')

def spawn_icon(symbol_hex, foreground='#f8f8f2'):
    w = widget.TextBox(
        text=symbol_hex,
        fontsize=font_size,
        padding=0,
        foreground=foreground
    )

    return w

def set_screen():
    screen =  Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    urgent_alert_method='block',
                    highlight_method='block',
                    rounded=False,
                    disable_drag=True,
                    this_screen_border=colors['background'],
                    this_current_screen_border=colors['purple_highlight'],
                    other_screen_border=colors['dark_gray'],
                    other_current_screen_border=colors['dark_gray'],
                    urgent_border=colors['urgent'],
                    inactive=colors['inactive'],
                    fontsize=font_size,
                ),
                widget.WindowName(
                    foreground=colors['lighter_gray'],
                ),
                widget.Spacer(),
                spawn_icon('\ue266', '#8be9fd'),
                widget.Memory(
                    format='{MemUsed} MB'
                ),
                spawn_icon('\uf85a', '#f1fa8c'),
                widget.CPU(
                    format='{load_percent}%' 
                ),
                spawn_icon('\ufa7d', colors['orange']),
                widget.Volume(
                    cardid=1,
                    step=2,
                #     emoji=True,
                ),
                widget.Clock(format='%A,%e %b. %H:%M:%S'),
            ],
            25,
            opacity=.95,
            background=colors['background'],
        )
    )
    return screen

mod = "mod4"
terminal = 'alacritty'

keys = [
    # Move around windows
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
    Key([mod], 'e', lazy.spawn('pcmanfm')),

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
    Key([mod], 'r', lazy.spawn('rofi -show run')),
]

default_groups_config = {
    'persist': True
} 

groups = [
    Group(
        name='1', 
        label='\ue743',
        exclusive=True,
        **default_groups_config
    ),
    Group(
        name='2', 
        label='\ue795',
        exclusive=True,
        **default_groups_config
    ),
    Group(
        name='3', 
        label='\uf9b0',
        exclusive=True,
        **default_groups_config
    ),
    Group(
        name='4', 
        label='\ufc6e',
        **default_groups_config
        ) 
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name, switch_group=True), lazy.layout.to_screen(i.name),
            desc='Switch to & move focused window to group {}'.format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

monadtall_config = {
    'margin': 10,
    'border_width': 1,
    'border_focus': colors['foreground'], 
    'border_normal': colors['comment'],
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
    layout.MonadTall(**monadtall_config),
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

screens = [
    set_screen(),
    set_screen()
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
