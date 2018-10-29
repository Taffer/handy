# handy

Handy scripts and tools that aren't part of a project.

* `fortune_helper.rb` - Integrate  `fortune(6)` with
  [xscreensaver](https://www.jwz.org/xscreensaver/).
* `pidgin_emoji.py` - Convert Taehoon Kim's "emoji" module into Pidgin's\
  dictionary format.
* `pylint_cygwin` - Make it easier to use Cygwin pylint with Eclipse PyDev.
* `subl.sh` - Use Sublime Text 3 from Cygwin shells.

These are all MIT-licensed (see [LICENSE](LICENSE)) except for
`fortune_helper.rb`.

## fortune_helper.rb

A simple-ish Ruby web server that calls `fortune(6)`, intended for running
locally as a endpoint for some of the
[xscreensaver](https://www.jwz.org/xscreensaver/) hacks that display text in
an interesting way.

I can't remember where I got this, and I don't program in Ruby; the original
author didn't include any info in the comments.

Note that it doesn't allow any input from the web, and it's limited to running
`fortune -s`, so it *shouldn't* present a security vulnerability.

Preserved here for posterity.

If you wrote `fortune_helper.rb` let me know and I'll replace it with a link
to your repo or web page or whatever.

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

## subl.sh

Short script to make it easier to use Sublime Text 3 from a Cygwin shell. It
preserves any arguments, then attempts to convert file paths to Windows
format.

# LICENSE

These are all [MIT-licensed](LICENSE) except for `fortune_helper.rb`. It's not
mine, so I have no idea what license it has.
