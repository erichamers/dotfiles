import dracula.draw 

config.load_autoconfig()

colors = {
    'background': '#282a36',
    'current-line': '#44475a',
    'foreground': '#f8f8f2',
    'comment': '#6272a4',
    'cyan': '#50fa7b',
    'green': '#50fa7b',
    'orange': '#ffb86c',
    'pink': '#ff79c6',
    'purple': '#bd93f9',
    'red': '#ff5555',
    'yellow': '#f1fa8c',
    'dark_gray': '#191a21',
    'light_gray': '#a9a9a9',
}

hints_padding = {
    'bottom': 2,
    'left': 5,
    'top': 2,
    'right': 5
}

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 3,
        'horizontal': 4 
    }
})

# default config
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# custom configuration
config.set('downloads.position', 'bottom')
config.set('url.default_page', '/home/eric/.config/qutebrowser/home/homepage.html')
config.set('url.start_pages', '/home/eric/.config/qutebrowser/home/homepage.html')
config.set('url.searchengines', {'DEFAULT': 'http://www.google.com/search?q={}'})
config.set('tabs.show', 'multiple')
config.set('statusbar.show', 'always')
config.set('fonts.default_family', 'mononoki nerd font mono')
config.set('fonts.default_size', '12px')
config.set('colors.hints.bg', colors['yellow'])
config.set('colors.hints.fg', colors['current-line'])
config.set('colors.messages.info.fg', colors['foreground'])
config.set('hints.border', '0')
config.set('hints.padding', hints_padding)
config.set('colors.statusbar.command.fg', colors['foreground'])
config.set('colors.statusbar.insert.fg', colors['foreground'])
config.set('colors.statusbar.caret.fg', colors['foreground'])
config.set('colors.statusbar.normal.fg', colors['foreground'])
config.set('colors.statusbar.command.bg', colors['dark_gray'])
config.set('colors.statusbar.insert.bg', colors['dark_gray'])
config.set('colors.statusbar.caret.bg', colors['dark_gray'])
config.set('colors.statusbar.normal.bg', colors['dark_gray'])
config.set('colors.completion.fg', colors['light_gray'])
config.set('colors.completion.odd.bg', colors['dark_gray'])
config.set('colors.completion.even.bg', colors['dark_gray'])
config.set('colors.completion.category.bg', colors['background'])
config.set('colors.completion.category.fg', colors['foreground'])
config.set('colors.completion.category.border.top', colors['background'])
config.set('colors.completion.category.border.bottom', colors['background'])
config.set('colors.completion.item.selected.bg', colors['comment'])

# Keybindings
config.bind('<Ctrl+r>', 'restart')
config.bind('<Ctrl+j>', 'tab-move -')
config.bind('<Ctrl+k>', 'tab-move +')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
