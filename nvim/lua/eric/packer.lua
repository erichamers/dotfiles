vim.cmd([[packadd packer.nvim]])

return require("packer").startup(function(use)
	use("wbthomason/packer.nvim")
	use("folke/tokyonight.nvim")
	use({
		"nvim-telescope/telescope.nvim",
		tag = "0.1.0",
		requires = { { "nvim-lua/plenary.nvim" } },
	})
	use("akinsho/bufferline.nvim")
	use("nvim-treesitter/nvim-treesitter")
	use("neovim/nvim-lspconfig")
	use("mhartington/formatter.nvim")
	use("hrsh7th/nvim-cmp")
	use("hrsh7th/cmp-buffer")
	use("hrsh7th/cmp-path")
	use("hrsh7th/cmp-nvim-lsp")
	use("L3MON4D3/LuaSnip")
	use("saadparwaiz1/cmp_luasnip")
	use("rafamadriz/friendly-snippets")
	use("nvim-tree/nvim-tree.lua")
	use("windwp/nvim-autopairs")
	use("voldikss/vim-floaterm")
	use("tpope/vim-fugitive")
	use("vim-airline/vim-airline")
	use("vim-airline/vim-airline-themes")
end)
