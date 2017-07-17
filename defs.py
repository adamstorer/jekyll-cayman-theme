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
