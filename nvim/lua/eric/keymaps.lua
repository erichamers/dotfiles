vim.keymap.set("n", "<leader>t", "<cmd>Ex<CR>", {})
vim.keymap.set("n", "<C-s>", "<cmd>w<CR>", {})

-- Telescope keymappings
local builtin = require "telescope.builtin"
vim.keymap.set("n", "<leader>p", builtin.find_files, {})
vim.keymap.set("n", "<leader>fg", builtin.live_grep, {})
vim.keymap.set("n", "<leader>fb", builtin.buffers, {})

-- Buffer navigation
vim.keymap.set("n", "<C-w>", "<cmd>bd<CR>", {})
vim.keymap.set("n", "<C-j>", "<cmd>bprevious<CR>", {})
vim.keymap.set("n", "<C-k>", "<cmd>bnext<CR>", {})
