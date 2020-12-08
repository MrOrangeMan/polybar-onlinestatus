# polybar-onlinestatus
polybar module that checks if you are online

To install use `pip install polybar-onlinestatus`

And use module below:

```
[module/onlinestatus]
type = custom/script
exec = polybar-onlinestatus
tail = true
label = %{T4} %output% %{T-}
format-underline = #07BDEE
```

```font-3 = Hack Nerd Font:style=Bold:size=12```

You can use any font you want, but make sure icon is big enough. I recommend Nerd Hack but it's up to you.

For more options use ```polybar-onlinestatus --help``` in your terminal and assign options in ```exec = polybar-onlinestatus``` line.

Icon used by default is ``, if you are unable to see it - you need to install nerd font from nerdfonts.com 