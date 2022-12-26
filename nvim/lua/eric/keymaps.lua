vim.keymap.set({ "n", "v", "i" }, "<C-s>", "<cmd>w<CR>", {})

-- Telescope keymappings
local builtin = require("telescope.builtin")
vim.keymap.set("n", "<leader>p", builtin.find_files, {})
vim.keymap.set("n", "<leader>fg", builtin.live_grep, {})
vim.keymap.set("n", "<leader>fb", builtin.buffers, {})
vim.keymap.set("n", "<leader>fr", builtin.lsp_references, {})

-- Horizontal split navigation
vim.keymap.set("n", "<C-h>", "<C-w>h", {})
vim.keymap.set("n", "<C-l>", "<C-w>l", {})

-- Buffer navigation
vim.keymap.set("n", "<C-w>", "<cmd>bd<CR>", {})
vim.keymap.set("n", "<C-j>", "<cmd>bprevious<CR>", {})
vim.keymap.set("n", "<C-k>", "<cmd>bnext<CR>", {})

-- Remaking navigation
vim.keymap.set("n", "G", "Gzz", {})
vim.keymap.set("n", "<C-u>", "<C-u>zz", {})
vim.keymap.set("n", "<C-d>", "<C-d>zz", {})

-- Nerdtree mappings
vim.keymap.set("n", "<leader>t", "<cmd>NvimTreeToggle<CR>", {})

-- Terminal
vim.keymap.set("n", "<C-Bslash>", ":FloatermToggle<CR>", {})
