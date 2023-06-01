from html.parser import HTMLParser
class Parser(HTMLParser):
  # method to append the start tag to the list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    # method to append the end tag to the list end_tags.
  def handle_endtag(self, tag):
    global end_tags
    end_tags.append(tag)
  # method to append the data between the tags to the list text_data.
  def handle_data(self, data):
    global text_data
    text_data.append(data)
  # method to append the comment to the list comments.
  def handle_comment(self, data):
    global comments
    comments.append(data)
start_tags = []
end_tags = []
text_data = []
comments = []






# # # # EXAMPLE ON HOW TO USE ON OTHER FILES/NOTEBOOKS
#-----------------------------------------------------

# import html_parser as htmlParser
# sample = "<P>You could use any of the DLR languages, which provide a way to really easily host your own scripting platform. However, you don't have to use a scripting language for this. You could use C# and compile it with the C# code provider. As long as you load it in its own AppDomain, you can load and unload it to your heart's content.</P>"
# parser = htmlParser.Parser()
# parser.feed(sample)
# print("data:", htmlParser.text_data)
# print("start tags:", htmlParser.start_tags)
# print("end tags:", htmlParser.end_tags)
# print("comments", htmlParser.comments)

#-----------------------------------------------------


## SIDENOTE -> This parser doesn't extract links or images just raw text