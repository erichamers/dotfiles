local lsputil = require("lspconfig/util")

function get_python_venv()
	if vim.env.VIRTUAL_ENV then
		return vim.env.VIRTUAL_ENV
	end

	local match = vim.fn.glob(lsputil.path.join(vim.fn.getcwd(), "Pipfile"))
	if match ~= "" then
		return vim.fn.trim(vim.fn.system("PIPENV_PIPFILE=" .. match .. " pipenv --venv"))
	end

	match = vim.fn.glob(lsputil.path.join(vim.fn.getcwd(), "poetry.lock"))
	if match ~= "" then
		return vim.fn.trim(vim.fn.system("poetry env info -p"))
	end
end

-- Lsp Config
require("lspconfig")["pylsp"].setup({
	cmd = { "/home/eric/.local/venv/bin/pylsp", "-v" },
	cmd_env = { VIRTUAL_ENV = get_python_venv(), PATH = lsputil.path.join(venv, "bin") .. ":" .. vim.env.PATH },
	on_attach = function(client, bufnr)
		vim.keymap.set("n", "<C-g>", vim.lsp.buf.definition, {})
		vim.keymap.set("n", "K", vim.lsp.buf.hover, { buffer = 0 })
	end,
})

-- Autoformatter config
local python = require("formatter.filetypes.python")

require("formatter").setup({
	filetype = {
		python = { python.black, python.isort },
		lua = { require("formatter.filetypes.lua").stylua },
	},
})
