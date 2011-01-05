#!/usr/bin/env python
# Copyright 2011 Canonical Ltd.  Distributed under the terms of the GNU GPLv3 or later.
# Combines multiple SVG files into a single SVG in batch mode
# 2011-01-04 Mathieu Trudel-Lapierre <mathieu.trudel-lapierre@canonical.com>
# 2011-01-05 Paul Sladen <sladen@canonica.com>

import xml.dom.minidom
import sys
import optparse

def commandline():
    # Parse commandline
    parser = optparse.OptionParser(usage = '%prog [options] INPUT.svg [MOREINPUT.svg] -o OUTPUT.svg')
    parser.add_option("-n", "--dry-run", dest = "do_write",
                      default = True, action = "store_false",
                      help = "dry run: do not write output file, just test")
    parser.add_option("-o", "--output", dest = "output",
                      help = "full output path for processed SVG file")
    options, args = parser.parse_args()

    # Validate
    if len(args) < 1:
        parser.error("one or more input SVG files required")
    if options.do_write and not options.output:
        parser.error("SVG output filename required")

    return options, args

def main():
    options, args = commandline()

    # Open first SVG and then composite others on top as overlays
    base = xml.dom.minidom.parse(args[0])
    newline = lambda: base.createTextNode('\n')

    for overlay in args[1:]:
        comment = base.createComment(" imported from '%s' " % overlay)
        dom = xml.dom.minidom.parse(overlay)

        # Pull-in '<svg>' tag, clear attributes and rename to '<g>'
        g = base.importNode(dom.getElementsByTagName("svg")[0], deep = True)
        [g.removeAttribute(k) for k in g.attributes.keys() if k != 'id']
        g.tagName = 'g'

        # Insert into first SVG with comments and spacing
        for node in newline(), comment, newline(), g, newline():
            base.documentElement.appendChild(node)

    if options.do_write:
        base.writexml(open(options.output, "w"))

if __name__=='__main__':
    main()
