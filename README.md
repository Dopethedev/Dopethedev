<p align="center">
  <img src="banner.svg?v=2" alt="itsdope: learning AI and ML, building in public" width="820">
</p>

**I am learning AI and ML, and building in public while I do it.** From Nepal. I
write passion projects, learning projects, and the occasional thing that solves a
real problem. Early stage, and saying so plainly is more useful than dressing it
up. Not tied to one language either: Python most days, and whatever the problem
wants otherwise.

## What I am learning

The stage matters, so here it is:

- **Machine learning fundamentals**, and how models actually behave outside a
  notebook.
- **Local inference**, which is where most of my learning happens: whisper for
  speech to text, kokoro for speech out, silero for voice activity, onnxruntime
  underneath all of it.
- **Making a model useful in a program** rather than in a demo. That turned out to
  be mostly failure handling, deadlines and measuring, not prompts.
- **The parts of a language that are not the language:** packaging, locking,
  cross-platform behaviour, and tests that can actually fail.

## What I have built

**[archy](https://github.com/Dopethedev/archy)** is a voice assistant that hears
and speaks locally, thinks through whichever model I point it at, and puts a
dashboard on screen that changes mood by voice.

The parts worth knowing about:

- **Speech never leaves the machine.** Silero for voice activity, faster-whisper
  for speech to text, kokoro for speech out. Only the text of the request goes to
  a model, and only because that is the question.
- **It knows the machine.** One request sweeps it: processes, listening sockets,
  SSH configuration, the hosts file, world writable paths, user services, browser
  extensions, launcher entries, pending updates, and a ClamAV scan of the usual
  drop points.
- **The local things stay local.** Reminders, timers and the theme are parsed on
  the machine and answered in about half a second, with no model in the loop.
- **Windows runs most of it,** and the one part that cannot says so instead of
  pretending it did something.

## How I build

Rules I set early because they are cheap to say and expensive to keep:

- **A test that cannot fail does not count.** Take the fix out, watch the test
  fail, put it back.
- **Numbers come from runs**, not from a datasheet or a guess.
- **Failure paths first.** The quiet failure is the one that matters.
- **Say what was not verified** rather than rounding up to "done".
- **Nothing personal in a tracked file.** Settings live in a file that is ignored.

## What is coming

More of both kinds: projects I start because I want to learn something, and
projects that fix a real annoyance. Different languages, different problems. Stay
tuned.

## Where to look

- [archy](https://github.com/Dopethedev/archy), the assistant
- [FEATURES.md](https://github.com/Dopethedev/archy/blob/main/FEATURES.md),
  including the limits and what it deliberately does not do
- [CONTRIBUTING.md](https://github.com/Dopethedev/archy/blob/main/CONTRIBUTING.md),
  the rules the project actually follows
