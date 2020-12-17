syntax on 

set autoindent
set background=dark
set expandtab
set laststatus=2
set number
set relativenumber
set rtp+=$HOME/.local/lib/python2.7/site-packages/powerline/bindings/vim/
set ruler

set showcmd
set showtabline=2
set sw=4
set sts=4
set splitbelow
set ts=4
set textwidth=120
set ts=4 sw=4
set t_Co=256

set clipboard=unnamedplus

" ############# Plugins Config ############# 
set nocompatible              
filetype off                 

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'dracula/dracula-theme'
Plugin 'jiangmiao/auto-pairs'

call vundle#end()           
filetype plugin indent on  

let g:netrw_banner = 0

" ############# Custom Mappings ############# 

" JSON Formatting
com! FormatJSON %!python -m json.tool
nmap <C-j> :FormatJSON<CR>

" File Explorer
map <S-e> :Explore<CR>

" Window commands
nmap <C-q> :q<CR>

" Buffers Mapping
map <silent> <C-S-b> :bd<CR>
map <silent> <C-Tab> :bnext<CR>
map <silent> <C-S-Tab> :bprevious<CR>
