set number

syntax on 
set autoindent
set expandtab
set ts=4 sw=4

set background=dark
set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=$HOME/.local/lib/python2.7/site-packages/powerline/bindings/vim/
set showtabline=2

" Always show statusline
set laststatus=2

" Use 256 colours (Use this setting only if your terminal supports 256 colours)
set t_Co=256

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different 
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" Split config
set splitbelow

" Netrw config
let g:netrw_banner = 0

"############# Custom Mappings ############# 

" JSON Formatting
com! FormatJSON %!python -m json.tool
nmap <C-j> :FormatJSON<CR>

" File Explorer
map <C-e> :Sex<CR>

" Window commands
nmap <C-q> :q<CR>

" Splits
map <C-v> :vs<CR>
map <C-h> :sp<CR>
nmap <silent> <A-Up> :wincmd k<CR>
nmap <silent> <A-Down> :wincmd j<CR>
nmap <silent> <A-Left> :wincmd h<CR>
nmap <silent> <A-Right> :wincmd l<CR>






