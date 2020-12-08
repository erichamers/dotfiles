import dracula.draw 

config.load_autoconfig()

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
config.set('statusbar.show', 'in-mode')
config.set('fonts.default_family', 'mononoki nerd font mono')
config.set('fonts.default_size', '12px')

# Keybindings
config.bind('<Ctrl+r>', 'restart')
config.bind('<Ctrl+j>', 'tab-move -')
config.bind('<Ctrl+k>', 'tab-move +')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 3,
        'horizontal': 4 
    }
})
