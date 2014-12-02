# handy

Handy scripts and tools that aren't part of a project.

* `pidgin_emoji.py` - Convert Taehoon Kim's "emoji" module into Pidgin's dictionary format.
* `pylint_cygwin` - Make it easier to use Cygwin pylint with Eclipse PyDev.

## pidgin_emoji

This doesn't actually seem to work in Pidgin 2.10 on Windows; some searching
suggests that the "Text Replacment" plugin isn't very flexible. I can't even
get it to work with canned replacements, such as "it' snot" -> "it's not".

## pylint_cygwin

This makes it easier to use Cygwin's python (and a nice fresh `pylint`
installed via `pip install pylint` rather than the out-of-date version in
Cygwin) with PyDev in Eclipse.

The problem is that Eclipse runs in the Windows version of Java, so it's
passing in `C:\blah\filename.py`; `pylint` running in Cygwin sees
this isn't an absolute path, so it tries adding `/cygdrive/c/blah`
at the start, giving you the useless path of
`/cygdrive/c/blah/C:\\blah\\filename.py`.

This version of the `pylint` script (which lives in `/usr/bin/pylint` on
Cygwin) converts the Windows path to a UNIXy Cygwin path and carries on.
