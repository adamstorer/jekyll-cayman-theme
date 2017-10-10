import os
import re
files = [f for f in os.listdir("_topublish") if f.endswith('.markdown')]
for posts in files:
    print(posts)
    with open("_topublish/"+posts,"r") as post1:
        post = post1.read()
    defs = re.findall("<def>(.*?)</def>",post)
    replacement = "defs_used:\n"
    for definition in defs:
        replacement = replacement+"\n    "+definition

    newpost = post.replace("defs_used:\n",replacement)
    newname = posts.replace('.markdown','-defs.markdown')
    print newpost
    with open("_posts/"+newname,'w') as w:
        w.write(newpost)

taglist=[]
for posts in files:
    print(posts)
    with open("_topublish/"+posts,"r") as post1:
        post = post1.read()
    tags = re.findall("\[(.*?)\]",post)[0]
    tags = tags.replace("'","")
    tags = tags.split(",")
    for tag in tags:
        taglist.append(tag)
taglist = list(set(taglist))

for tag in taglist:
    with open("_category/template.md") as cat1:
        cat = cat1.read()
    cat = cat.replace("REPLACE1",tag)
    tag2 = tag.replace(" ","%20")
    cat = cat.replace("REPLACE2",tag2)
    with open("_category/"+tag+".markdown",'w') as w:
        w.write(cat)
