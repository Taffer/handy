# Handy

Handy scripts and tools that aren't part of a project.

* `crush.sh` - Shell script that uses `pngcrush` to make sure your PNGs are as
  small as possible.
* `open` - Simulate macOS's `open` command using `xdg-open`, which is nearly
  the same thing.
* `rclone-sync-music.sh` - Use `rclone` to back up my music collection to B2.

The stuff in sub-directories is of limited use.

In `cygwin`:

* `pylint_cygwin` - Make it easier to use Cygwin pylint with Eclipse PyDev.
* `subl.sh` - Use Sublime Text 3 from Cygwin shells.

In `macosx`:

* `fortune_helper.rb` - Integrate  `fortune(6)` with
  [xscreensaver](https://www.jwz.org/xscreensaver/).

In `pidgin`:

* `pidgin_emoji.py` - Convert Taehoon Kim's "emoji" module into Pidgin's\
  dictionary format.

These are all MIT-licensed (see [LICENSE](LICENSE.md)) except for
`fortune_helper.rb`.

## crush.sh

Feed your PNG files to this script and they'll become as small as possible
(depends on `pngcrush` and expects `/bin/bash`). I think I saved about 30MB in
my wallpaper collection...

## find-broken-perms.h

Shell script to search for files that have had their permissions blown off.
This seems to happen under Windows Subsystem for Linux when I'm editing files
using the Windows version of SublimeText.

Yes, I know you're not supposed to touch WSL files with Windows apps.

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

## open

I use macOS at work, so I got very used to being able to `open` things;
`xdg-open` is basically the same command, but without my muscle memory, and
with chattier applications.

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

## rclone-sync-music.sh

Syncs my music collection to Backblaze's excellent B2 cloud storage using
`rclone`. Limits bandwidth usage during the day so I could still work from
home while doing the initial upload (which took a week or so). Also, so my
family doesn't kill me for hogging the limited up-stream bandwidth.

Sure be nice if Canada's Internet wasn't controlled by a colluding duopoly.
Maybe in another 20 years I'll be able to get fibre to my home.

## subl.sh

Short script to make it easier to use Sublime Text 3 from a Cygwin shell. It
preserves any arguments, then attempts to convert file paths to Windows
format.

## LICENSE

These are all [MIT-licensed](LICENSE.md) except for `fortune_helper.rb`. It's
not mine, so I have no idea what license it has.
