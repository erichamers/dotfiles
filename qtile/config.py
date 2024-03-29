import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup
def autostart():
    processes = [
        ["/usr/bin/dunst"],
        ["/usr/bin/picom"],
        ["/usr/bin/lxqt-policykit-agent"],
        ["/usr/bin/unclutter", "--timeout", "1"],
    ]
    for p in processes:
        subprocess.Popen(p)


@hook.subscribe.startup_once
def autostart_once():
    processes = [["nitrogen", "--restore"]]
    for p in processes:
        subprocess.Popen(p)


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Custom commands
    Key(
        [mod],
        "r",
        lazy.spawn('dmenu_run -nb "black" -fn "JetBrains Mono Nerd Font-8"'),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Print", lazy.spawn("flameshot full -p /home/eric/screenshots/")),
    Key(
        [mod, "shift"], "Print", lazy.spawn("flameshot gui -p /home/eric/screenshots/")
    ),
    Key(
        ["mod1"],
        "Tab",
        lazy.group.next_window(),
        desc="Focus next window",
    ),
    Key([mod], "period", lazy.next_screen(), desc="Focus next monitor"),
    Key([mod], "b", lazy.spawn("google-chrome-stable"), desc="Launch Google Chrome"),
    Key([mod], "e", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([mod], "q", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key(
        [mod],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout",
    ),
]

groups_dict = {
    # Key: keymap for that group | Value: Group object
    "y": Group(name="web", matches=[Match(wm_class="Google-chrome")]),
    "u": Group(
        name="dev",
        matches=[
            Match(wm_class="Alacritty"),
            Match(wm_class="Code"),
            Match(wm_class="jetbrains-idea-ce"),
        ],
    ),
    "i": Group(name="slack", matches=[Match(wm_class="Slack")]),
    "o": Group(
        name="teams",
        matches=[
            Match(title="Chat | Microsoft Teams"),
            Match(title="Microsoft Teams - Preview"),
        ],
    ),
    "p": Group(
        name="etc",
        matches=[
            Match(wm_class="zoom"),
            Match(wm_class="gpclient"),
            Match(wm_class="Postman"),
        ],
    ),
}

groups = groups_dict.values()

for k, v in groups_dict.items():
    keys.extend(
        [
            Key(
                [mod],
                k,
                lazy.group[v.name].toscreen(),
                desc="Switch to group {}".format(v.name),
            ),
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(v.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(v.name),
            ),
        ]
    )

default_layout_opts = {
    "border_width": 2,
    "margin": 20,
    "border_focus": "#e1acff",
    "border_normal": "#1d2330",
    "border_on_single": True,
}

layouts = [
    layout.Stack(**default_layout_opts, num_stacks=1),
    layout.Columns(**default_layout_opts),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="block",
                ),
                widget.Sep(padding=30),
                widget.TaskList(
                    highlight_method="block", max_title_width=300, txt_floating=""
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentScreen(active_text="⬤", inactive_text="", padding=10),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "us_intl"],
                    display_map={"us": "US", "us_intl": "BR"},
                ),
                widget.Memory(format="RAM Usage: {MemUsed:.0f} MB", padding=10),
                widget.PulseVolume(padding=10, limit_max_volume=True),
                widget.Clock(format="%b %d, %a | %I:%M:%S %p", padding=10),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="block",
                ),
                widget.Sep(padding=30),
                widget.TaskList(
                    highlight_method="block", max_title_width=300, txt_floating=""
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentScreen(active_text="⬤", inactive_text="", padding=10),
                widget.Systray(icon_size=15, padding=10),
                widget.Sep(padding=30),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "us_intl"],
                    display_map={"us": "US", "us_intl": "BR"},
                ),
                widget.Memory(format="RAM Usage: {MemUsed:.0f} MB", padding=10),
                widget.PulseVolume(padding=10, limit_max_volume=True),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", padding=10),
            ],
            24,
        ),
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="Blueman-manager"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
