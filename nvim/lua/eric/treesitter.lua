require("nvim-treesitter.configs").setup({
	ensure_installed = { "python", "lua", "go", "java" },
	sync_install = false,
	auto_install = true,
	ignore_install = {},
	highlight = {
		enable = true,
		disable = {},
		additional_vim_regex_highlighting = false,
	},
})
