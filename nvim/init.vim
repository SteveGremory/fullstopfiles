" SteveGremory's Vim Config file, which he wrote himself this time!
syntax on

"
" Plugin Management
"
call plug#begin()

" Alignment Plugin
Plug 'junegunn/vim-easy-align'
Plug 'nikolvs/vim-sunbather'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'itchyny/lightline.vim'
call plug#end()

"
" Setting Vim variables
"
set number		        " Enable line numbers
set tabstop=4           " Tab = 4 spaces
set expandtab		    " Choose tabs or spaces automatically
set autoindent		    " Automatically add tabs/spaces
set smartindent 	    " Vim said to do this don't ask me
set softtabstop=4	    " Remove 4 spaces when removing a tab

colorscheme sunbather 
