" SteveGremory's Vim Config file, which he wrote himself this time!
syntax on
filetype plugin indent on

"
" Plugin Management
"
call plug#begin()
Plug 'junegunn/vim-easy-align'
Plug 'itchyny/lightline.vim'
Plug 'lervag/vimtex'
Plug 'preservim/nerdtree'
Plug 'morhetz/gruvbox'
Plug 'nvim-tree/nvim-web-devicons'
call plug#end()

"
" Setting Vim variables
"
set number		        " Enable line numbers
set tabstop=8           " Tab = 4 spaces
set expandtab		    " Choose tabs or spaces automatically
set autoindent		    " Automatically add tabs/spaces
set smartindent 	    " Vim said to do this don't ask me
set softtabstop=8	    " Remove 4 spaces when removing a tab

colorscheme gruvbox 
hi Normal guibg=NONE ctermbg=NONE

"
" Extension configuration
"

"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
if (empty($TMUX))
  if (has("nvim"))
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  if (has("termguicolors"))
    set termguicolors
  endif
endif

