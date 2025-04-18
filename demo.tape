Output demo.gif

Require "token-cli"

Set Shell "fish"
Set FontSize 22
Set Width 1200
Set Height 600

Type `echo "Ceci n'est pas une pipe." | token-cli` Sleep 500ms  Enter

Sleep 2s

Type `fzf --preview "token-cli --force-terminal {}"` Sleep 500ms Enter

Sleep 2s

Up@2s 3

Sleep 2s