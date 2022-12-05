vim.cmd([[packadd packer.nvim]])

return require("packer").startup(function(use)
	use("wbthomason/packer.nvim")
	use("morhetz/gruvbox")
	use("olimorris/onedarkpro.nvim")
	use({
		"nvim-telescope/telescope.nvim",
		tag = "0.1.0",
		requires = { { "nvim-lua/plenary.nvim" } },
	})
	use("ap/vim-buftabline")
	use({
		"nvim-treesitter/nvim-treesitter",
		run = ":TSUpdate",
	})
	use("neovim/nvim-lspconfig")
	use("hrsh7th/nvim-cmp")
	use("hrsh7th/cmp-nvim-lsp")
	use("hrsh7th/cmp-buffer")
	use("hrsh7th/cmp-path")
	use("L3MON4D3/LuaSnip")
	use("jiangmiao/auto-pairs")
	use("vim-airline/vim-airline")
	use("vim-airline/vim-airline-themes")
	use("nvim-tree/nvim-tree.lua")
	use("nvim-tree/nvim-web-devicons")
	use("Yggdroot/indentLine")
	use("averms/black-nvim")
	use("jose-elias-alvarez/null-ls.nvim")
	use("tpope/vim-fugitive")
	use("folke/tokyonight.nvim")
	use("ThePrimeagen/vim-be-good")
end)
