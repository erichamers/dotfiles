local nnoremap = require("eric.mapper").nnoremap

-- nnoremap("<leader>q", "<cmd>Ex<CR>")

-- Close current buffer
nnoremap("<C-w>", "<cmd>bd<CR>")

-- Switch between buffers
nnoremap("<C-k>", "<cmd>bnext<CR>")
nnoremap("<C-j>", "<cmd>bprev<CR>")

local builtin = require("telescope.builtin")

nnoremap("<C-p>", builtin.find_files)
nnoremap("<leader>fg", builtin.live_grep)
nnoremap("<leader>fb", builtin.buffers)
nnoremap("<leader>fh", builtin.help_tags)

-- Move between splits
nnoremap("<C-h>", "<C-W>h")
nnoremap("<C-l>", "<C-W>l")

-- Nvim-Tree keymaps
nnoremap("<C-t>", "<cmd>NvimTreeToggle<CR>")

-- PGDOWN PGUP remaster
nnoremap("<C-u>", "<C-u>zz")
nnoremap("<C-d>", "<C-d>zz")
nnoremap("G", "Gzz")
nnoremap("n", "nzz")
nnoremap("N", "Nzz")
