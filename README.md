# math_engine

Python engine for practicing simple math. Not really designed to be
used on its own, but rather to be used by other software such as chat
bots. It asks questions in string format, and expects answers as
strings.

## Purpose

I wrote this package because of a child who needs help practicing
math. My initial thought was to install a math practice app on the
child's phone, but I had difficulties finding one I liked that had the
following two key features:

1. Reporting progress to a parent / teacher, and
2. Not having, for example, only 10 seconds to answer each question.
   The child in question doesn't handle math well under stress, so I
   want something that keeps track of how long the drills take, but
   doesn't set a fixed time limit to them.
   
I was unable to find something like this. So I decided to make it
myself instead. I don't want to write it as an Android / Ios app
though, I'd rather have it be a chat bot that you can talk to on any
device. I already have a general purpose bot (EnforsBot), so I want to
add this functionality to it. But instead of coding the math engine
stuff directly in EnforsBot, I decided to separate it out to its own
package, which EnforsBot can use.
