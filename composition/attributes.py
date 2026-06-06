from pymonad.tools import curry

@curry(3)
def tag(tag: str, attr: dict[str, str], content: str):
    attributes = " ".join(f'{k}="{v}"' for k, v in attr.items())
    attrs = f" {attributes}" if attributes else ""
    return f"<{tag}{attrs}>{content}</{tag}>"

attributes = { 'class': 'list-group', 'style': 'list-group-item-separator' }
li_tag = tag('li', attributes, 'item 23')
print(li_tag)

bold_tag = tag("b", attributes)
italic_tag = tag("i", attributes)
bold_text = bold_tag("bold content")
italic_text = italic_tag("italic content")
print(bold_text)
print(italic_text)