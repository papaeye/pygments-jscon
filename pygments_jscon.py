import re

from pygments.lexer import Lexer, do_insertions
from pygments.lexers.agile import line_re
from pygments.lexers.web import JavascriptLexer
from pygments.token import Generic


class JavaScriptConsoleLexer(Lexer):
    """For JavaScript console."""

    name = 'JavaScriptConsole'
    aliases = ['jscon']

    _prompt_re = re.compile('>{1,3} ')

    def get_tokens_unprocessed(self, text):
        jslexer = JavascriptLexer(**self.options)

        curcode = ''
        insertions = []
        for match in line_re.finditer(text):
            line = match.group()
            m = self._prompt_re.match(line)
            if m is not None:
                end = m.end()
                insertions.append((len(curcode),
                                   [(0, Generic.Prompt, line[:end])]))
                curcode += line[end:]
            else:
                if curcode:
                    for item in do_insertions(
                        insertions, jslexer.get_tokens_unprocessed(curcode)):
                        yield item
                    curcode = ''
                    insertions = []
                yield match.start(), Generic.Output, line
        if curcode:
            for item in do_insertions(insertions,
                                      jslexer.get_tokens_unprocessed(curcode)):
                yield item
