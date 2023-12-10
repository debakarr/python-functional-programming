from IPython.display import HTML, display
from IPython.core.magic import register_line_cell_magic
import urllib.parse


def tutor(line, cell):
    code = urllib.parse.urlencode({"code": cell})
    display(HTML(f"""
    <iframe width="800" height="500" frameborder="0"
            src="http://pythontutor.com/iframe-embed.html#{code}&py=311">
    </iframe>
    """))
    
def load_ipython_extension(ipython):
    ipython.register_magic_function(tutor, magic_kind="line_cell")