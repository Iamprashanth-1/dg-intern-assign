import urllib.request

def getvalues(ch, string, k):
    for i in range(len(string)):
        if ch == string[i]:
            k.append(i)
def get_spaces(n):
    str = ''
    for _ in range(0, n):
        str = str + ' '
    return str
def anti_html(link):

    opener = urllib.request.FancyURLopener({})
    f = opener.open(link)
    html = str(f.read())

    l1 = []
    l2 = []
    getvalues('<', html, l1)
    getvalues('>', html, l2)

    for i in range(0, len(l1)):
        html = html.replace(html[l1[i]:l2[i]+1],get_spaces(l2[i]-l1[i]+1), -1)
    return html


if __name__ == "__main__":
    print(anti_html('https://www.datagrokr.com/'))