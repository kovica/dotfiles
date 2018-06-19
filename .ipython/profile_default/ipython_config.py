c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 50
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = [
    'import numpy as np',
    'import matplotlib',
    'import seaborn as sns',
    'import protein as pr',
    '%autoreload 2',
    '%matplotlib qt5'
]
c.InteractiveShell.autoindent = True
# c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = True
# c.InteractiveShell.deep_reload = True
c.InteractiveShell.editor = 'nvim'
c.InteractiveShell.xmode = 'Context'

from IPython.terminal.prompts import Prompts, Token
import os

class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [(Token, os.getcwd()),
                (Token.Prompt, ' >>> ')]

c.TerminalInteractiveShell.prompts_class = MyPrompt

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
 ('la', 'ls --color -al')
]