"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nocompatible
set number relativenumber
set clipboard=unnamedplus
set backspace=indent,eol,start

set updatetime=300
set encoding=utf-8
scriptencoding utf-8

set hlsearch
set wildmenu
set wildignore=*.jpg,*.png,*.gif,*.pdf,*.pyc,*.flv,*.img
set wildmode=list:longest
set showcmd
set signcolumn=no
set path+=../inc,../include,../tests,./src,./srcs

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Remap Keys
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader><space> :nohlsearch<CR>
inoremap  <Esc>
nnoremap <space> :

inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>
inoremap " ""<Left>

" Remap Page Up to Left Arrow
nnoremap <PageUp> <Left>
inoremap <PageUp> <Left>
vnoremap <PageUp> <Left>

" Remap Page Down to Right Arrow
nnoremap <PageDown> <Right>
inoremap <PageDown> <Right>
vnoremap <PageDown> <Right>

let g:mappings_enabled = 1

function! ToggleMappings()
    if g:mappings_enabled
        imap 1 !
        imap 2 @
        imap 3 #
        imap 4 $
        imap 5 %
        imap 6 ^
        imap 7 &
        imap 8 *
        imap 9 (
        imap 0 )
        imap - _
        imap = +
        let g:mappings_enabled = 0
    else
        iunmap 1
        iunmap 2
        iunmap 3
        iunmap 4
        iunmap 5
        iunmap 6
        iunmap 7
        iunmap 8
        iunmap 0
        iunmap -
        iunmap =
        let g:mappings_enabled = 1
    endif
endfunction

inoremap <F9> <C-O>:call ToggleMappings()<CR>

" toggle on non-printable-chars
set listchars=tab:→\ ,space:·,nbsp:␣,trail:•,eol:¬
map <F2> :set invlist<CR>

" terminal
nnoremap <silent> <F4> :bel term<CR>
set autochdir

" run python script
nnoremap <f5> :w <CR>:!clear <CR>:!python3 % <CR>

" insert date
nnoremap <f6> :r!date "+\%Y-\%m-\%d \%H:\%M:\%S" <Esc>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Folding
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set foldmethod=syntax
set foldlevel=2
nnoremap ' zR
nnoremap " zM
nnoremap zz zA
nnoremap <leader><leader> za

" Define a function to set the custom highlight
function! SetCustomHighlight()
    highlight Folded ctermbg=black ctermfg=cyan guibg=#000000 guifg=#ffffff
endfunction

" Call the function when the ColorScheme event is triggered
augroup SetCustomHighlightGroup
    autocmd!
    autocmd ColorScheme * call SetCustomHighlight()
augroup END

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab, indentation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

syntax enable
filetype plugin indent on
set smartindent
set autoindent
set tabstop=4
set shiftwidth=4
set noexpandtab
set cindent

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Splits and Tabbed Files
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

noremap <c-up> <c-w>+
noremap <c-down> <c-w>-
noremap <c-left> <c-w>>
noremap <c-right> <c-w><

" tags
set tags=./tags,tags;/

" Define a shortcut to generate tags for the project
command! -nargs=0 GenerateTags !ctags -R --exclude=.git --exclude=build
map <C-\> :tab split<CR>:exec("tag ".expand("<cword>"))<CR>
map <Esc>/ :vsp <CR>:exec("tag ".expand("<cword>"))<CR>

" Alt-right/left to navigate forward/backward in the tags stack
map <M-Left> <C-T>
map <M-Right> <C-]>
