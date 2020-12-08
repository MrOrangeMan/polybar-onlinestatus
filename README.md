# polybar-onlinestatus
polybar module that checks if you are online

To install use `pip install polybar-onlinestatus`

And use module below.

```
[module/onlinestatus]
type = custom/script
exec = polybar-onlinestatus
tail = true
```


#TO-DO:
- Add space after icon
- Add while loop with delay due to "tail = true"
