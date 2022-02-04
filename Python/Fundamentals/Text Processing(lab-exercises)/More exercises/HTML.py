articleTitle=input(); articleContent=input()
def TurnIntoHtml(Title,Content):
    htmlCode=f"<h1>\n    {Title}\n</h1>\n<article>\n    {Content}\n</article>"
    while True:
        comment=input()
        if comment!="end of comments":
            htmlCode+=f"\n<div>\n    {comment}\n</div>"
        else:
            break
    return htmlCode
print(TurnIntoHtml(articleTitle,articleContent))
