# 形 kata-dev

**This small repo provides information for developers of [kata](http://kata.geosci.ai/) challenges.**

The `kata` server itself is private, because it essentially contains the solutions to the challenges. But the [`demo`](demo) folder contains everything you need to provide for a challenge. This demo challenge is itself live at [kata.geosci.ai](http://kata.geosci.ai/challenge/demo) — check it out. Have a go at solving it, and you'll soon get the hang of what the challenges are like (although most of them are a bit harder than the demo!).


## Basic information

- Users are anonymous and the server does not track or log any information at all.
- There is no UI, and the server only responds to GET requests. Forming and submitting requests is part of the learning for new Pythonistas.
- Users can respond as many times as they like, but wrong answers are throttled (one minute for the first, then 2 minutes, then 3, etc). The time penalty pertains to a *key*, not a *user*, and resets each day.
- Users can get hints by giving the server a key and question number, but no answer.

## Guidelines for making challenges

- Challenges should be related to subsurface datasets or workflows, but can be quite abstract or toy-like.
- Your code must generate pseudorandom datasets of a reasonable size (usually 1000's of records), given a random seed.
- The generation should take less than about 250 ms; there is no caching on the server. (If you'd like to help implement this, please get in touch!).
- Challenges must have 3 or 4 questions.
- The responses to questions should be integers or strings. Floating point numbers are not ideal and would certainly need rounding.
- The first question should be very easy and really only check that the person has parsed the data correctly.
- The last question should be somewhat related to a real-world problem or challenge.
- Questions between the first and last should ideally build in some way towards the last.
- In general, the puzzles can be solved in any language, so we try to avoid Python-specific language or tools. But most people do them in Python so sometimes it seems humane to do it anyway.

Check out the two files in [the `demo` folder](demo) and see if you can cook something up. The best way to share your challenge with us is probably [by email at hello@scienxlab.org](mailto:hello@scienxlab.org) or via DM in [the Software Underground slack](https://swung.slack.com) (sign up at [softwareunderground.org](https://softwareunderground.org/slack). Remember not to share it publicly; it needs to stay secret.
