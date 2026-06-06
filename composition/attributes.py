from pymonad.tools import curry

@curry(3)
def tag(tag: str, attr: dict[str, str], content: str):
    attributes = " ".join(f'{k}="{v}"' for k, v in attr.items())
    attrs = f" {attributes}" if attributes else ""
    return f"<{tag}{attrs}>{content}</{tag}>"

attributes = { 'class': 'list-group', 'id': 'list-item' }
li_tag = tag('li', attributes, 'item 23')
print(li_tag)

bold = tag("b", {"class": "bold"} )
italic = tag("i", {})
bold_tag = bold("bold content")
italic_tag = italic("italic content")
print(bold_tag)
print(italic_tag)