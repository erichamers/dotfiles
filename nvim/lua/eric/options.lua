vim.opt.clipboard = "unnamedplus"
vim.opt.cmdheight = 2

vim.opt.guicursor = ""
vim.opt.completeopt = { "menu", "menuone", "noselect" }

vim.opt.hlsearch = false
vim.opt.mouse = "a"
vim.opt.showtabline = 2
vim.opt.smartcase = true
vim.opt.smartindent = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.numberwidth = 4
vim.opt.wrap = false
vim.opt.sidescrolloff = 8
vim.opt.scrolloff = 8
vim.opt.termguicolors = true

vim.g.mapleader = ";"
vim.g.indentLine_char = "▏"

vim.g.python3_host_prog = "/home/eric/.pyenv/versions/py3nvim/bin/python"

vim.opt.cursorline = true
vim.opt.cursorlineopt = "both"

vim.cmd([[
   autocmd InsertLeave * highlight CursorLine guibg=#1e2127
]])

vim.cmd([[
   autocmd InsertEnter * highlight CursorLine guibg=#1e2127
]])
