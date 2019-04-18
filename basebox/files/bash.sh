#!/bin/bash

# append this to ~/.bashrc

## EXPORTS
##########################################
export GIT_PS1_SHOWUNTRACKEDFILES=1 GIT_PS1_SHOWSTASHSTATE=1 GIT_PS1_SHOWDIRTYSTATE=1 GIT_PS1_SHOWCOLORHINTS=1 GIT_PS1_DESCRIBE_STYLE="branch" GIT_PS1_SHOWUPSTREAM="auto git"

## DIRCOLORS + COLORIZED LS/GREP
##########################################
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dir_colors && eval "$(dircolors -b ~/.dir_colors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

## BASH COMPLETION
##########################################

if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi


## BASH OPTIONS
##########################################

# Update window size after every command
shopt -s checkwinsize

# Automatically trim long paths in the prompt
PROMPT_DIRTRIM=4

# Enable history expansion with space
# E.g. typing !!<space> will replace the !! with your last command
bind Space:magic-space

# Case-insensitive globbing (used in pathname expansion)
shopt -s nocaseglob;

# Perform file completion in a case insensitive fashion
bind "set completion-ignore-case on"

# Treat hyphens and underscores as equivalent
bind "set completion-map-case on"

# Display matches for ambiguous patterns at first tab press
bind "set show-all-if-ambiguous on"

# Immediately add a trailing slash when autocompleting symlinks to directories
bind "set mark-symlinked-directories on"

# Append to the Bash history file, rather than overwriting it
shopt -s histappend;

# Save multi-line commands as one command
shopt -s cmdhist

# Record each line as it gets issued
PROMPT_COMMAND='history -a'

# Huge history. Doesn't appear to slow things down, so why not?
HISTSIZE=500000
HISTFILESIZE=100000

# Avoid duplicate entries
HISTCONTROL="ignoreboth"

# Don't record some commands
export HISTIGNORE="&:[ ]*:exit:ls:bg:fg:history:clear"

# Use standard ISO 8601 timestamp
# %F equivalent to %Y-%m-%d
# %T equivalent to %H:%M:%S (24-hours format)
HISTTIMEFORMAT='%F %T '

# Autocorrect typos in path names when using `cd`
shopt -s cdspell;

# Add the directories you want to have fast access to, separated by colon
# Ex: CDPATH=".:~:~/projects" will look for targets in the current working directory, in home and in the ~/projects folder
CDPATH="."

# Correct spelling errors during tab-completion
shopt -s dirspell 2> /dev/null

# Enable some Bash 4 features when possible:
# * `autocd`, e.g. `**/qux` will enter `./foo/bar/baz/qux`
# * Recursive globbing, e.g. `echo **/*.txt`
for option in autocd globstar; do
    shopt -s "$option" 2> /dev/null;
done;


## BASH PROMPT - PC
##########################################

if [[ "${USER}" == "root" ]]; then
    export PS1='\[\033[00;31m\]\u\[\033[00;37m\] \[\033[00;34m\]\h \[\033[01;36m\]\w\[\033[00;33m\]$(__git_ps1 " (%s)")\[\033[00m\] '
else
    export PS1='\[\033[00;31m\]\u\[\033[00;37m\] \[\033[00;37m\]\h \[\033[01;36m\]\w\[\033[00;33m\]$(__git_ps1 " (%s)")\[\033[00m\] '
fi;

export PS2="\[\033[00;33m\]> \[\033[00m\]";


## ALIASES
##########################################

alias ll='ls -ahlF'
alias la='ls -ACF'
alias l='ls -ahlF'
alias df='df -h'

alias cd..='cd ../'                         # Go back 1 directory level (for fast typers)
alias ..='cd ../'                           # Go back 1 directory level
alias ...='cd ../../'                       # Go back 2 directory levels
alias .3='cd ../../../'                     # Go back 3 directory levels
alias .4='cd ../../../../'                  # Go back 4 directory levels
alias .5='cd ../../../../../'               # Go back 5 directory levels
alias .6='cd ../../../../../../'            # Go back 6 directory levels

alias ip='ip --color'
alias ipb='ip --color --brief'

alias ap="ansible-playbook"
alias va="source venv/bin/activate"

alias gl="git log --pretty=format:\"%C(yellow)%h%Cred%d %Creset%s%Cblue [%cn %ai]\" --decorate --graph"
alias gll="git log --pretty=format:\"%C(yellow)%h%Cred%d %Creset%s%Cblue [%cn %ai]\" --decorate --graph --numstat"

alias gs="git status -s"
alias gss="git status"

alias gb='git branch '
alias go='git checkout '
alias grv='git remote -v'

alias gc="git commit"
alias ga="git add "
alias gd="git diff"
alias gpl="git pull origin master --tags"
alias gps="git push origin master --tags"

# I **think** this shouldn't break anything... python2 is going away 
# so we need to start defaulting to python3.
# DO NOT CHANGE FOR ROOT OR AT THE SYSTEM LEVEL!
alias python="python3"
alias pip="pip3"
