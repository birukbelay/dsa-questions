# functions
#  remove prefix
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix)]
    return text

def remove_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s