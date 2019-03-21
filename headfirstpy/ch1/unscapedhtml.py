##Converting to and from HTML encoded text.
import html
print(html.escape("This HTML fragment contains a <script>script</script> tag."))

print(html.unescape("I &hearts; Python's &lt;standard library&gt;. <b>This is Amit</b>"))
