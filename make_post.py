import sys
from datetime import date, time
import argparse
import sys, tempfile, os
from subprocess import call
import git

EDITOR = os.environ.get('EDITOR','vim') #that easy!

def make(my_date=None, title=None):

    if my_date is None:
        my_date = input("Enter Date in MM/DD/YYYY:\t")

    if my_date in ["today", "Today", "TODAY", "T", ""]:
        prefix = date.today().strftime("%Y-%m-%d")
    else:
        flip = my_date.replace("/", "-").replace('.', '-')
        y, m, d = flip.split('-')
        prefix = '-'.join([y,m.zfill(2),d.zfill(2)])

    if title is None:
        title = "-".join(input("Title:\t").lower().split())
    else:
        title = "-".join(title.lower().split())

    fn = "_posts/{}-{}.md".format(prefix, title)
    with open(fn, "a") as f:
        f.write(
            '---\nlayout: post\ntitle: "{}"\n---\n'.format(
                title.replace("-", " ").title()
            )
        )
        f.flush()
        call([EDITOR, f.name])
        f.seek(0)

        g = git.cmd.Git('./')
        g.add(fn)
        g.commit(message="Adding post from {} about {}".format(prefix, title))
        g.push()
        # origin = g.remote(name='origin')
        # origin.push()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Some useful utilities for this project."
    )
    parser.add_argument("-d", "--date", default=None)
    parser.add_argument("--title", "-t", default=None)
    args = parser.parse_args()

    make(args.date, args.title)
