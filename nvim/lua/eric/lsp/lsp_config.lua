-- Python setup
local capabilities = require("cmp_nvim_lsp").default_capabilities()
local path = require("lspconfig/util").path

local border = { "┌", "─", "┐", "│", "┘", "─", "└", "│" }

local handlers = {
	["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, { border = border }),
	["textDocument/signatureHelp"] = vim.lsp.with(vim.lsp.handlers.signature_help, { border = border }),
}

local function on_attach()
	vim.keymap.set("n", "<C-g>", vim.lsp.buf.definition, {})
	vim.keymap.set("n", "K", vim.lsp.buf.hover, { buffer = 0 })
end

local function get_python_venv()
	if vim.env.VIRTUAL_ENV then
		return vim.env.VIRTUAL_ENV
	end

	local match = vim.fn.glob(path.join(vim.fn.getcwd(), "Pipfile"))
	if match ~= "" then
		return vim.fn.trim(vim.fn.system("PIPENV_PIPFILE=" .. match .. " pipenv --venv"))
	end

	match = vim.fn.glob(path.join(vim.fn.getcwd(), "poetry.lock"))
	if match ~= "" then
		return vim.fn.trim(vim.fn.system("poetry env info -p"))
	end
end

local venv = get_python_venv()

require("lspconfig").pylsp.setup({
	settings = {
		pylsp = {
			plugins = {
				pycodestyle = {
					ignore = { "E501", "E113" },
				},
			},
		},
	},
	capabilities = capabilities,
	cmd = { "/home/eric/.local/venv/bin/pylsp", "-v" },
	cmd_env = { VIRTUAL_ENV = venv, PATH = path.join(venv, "bin") .. ":" .. vim.env.PATH },
	on_attach = on_attach,
	handlers = handlers,
})

-- Autoformatter config
require("formatter").setup({
	filetype = {
		go = { require("formatter.filetypes.go").gofmt },
		python = {
			{
				exe = "/home/eric/.pyenv/shims/isort",
				args = { "-q", "-" },
				stdin = true,
			},

			{
				exe = "/home/eric/.pyenv/shims/black",
				args = { "-q", "-" },
				stdin = true,
			},
		},
		lua = { require("formatter.filetypes.lua").stylua },
	},
})

-- Lua setup
require("lspconfig").sumneko_lua.setup({
	capabilities = capabilities,
	handlers = handlers,
	on_attach = on_attach,
	settings = {
		Lua = {
			runtime = {
				-- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
				version = "LuaJIT",
			},
			diagnostics = {
				-- Get the language server to recognize the `vim` global
				globals = { "vim" },
			},
			workspace = {
				-- Make the server aware of Neovim runtime files
				library = vim.api.nvim_get_runtime_file("", true),
			},
			-- Do not send telemetry data containing a randomized but unique identifier
			telemetry = {
				enable = false,
			},
		},
	},
})

require("lspconfig").gopls.setup({
	capabilities = capabilities,
	handlers = handlers,
	on_attach = on_attach,
})

require("lspconfig").java_language_server.setup({
	capabilities = capabilities,
	handlers = handlers,
	on_attach = on_attach,
	cmd = { "/home/eric/apps/java-language-server/dist/lang_server_linux.sh" },
})
