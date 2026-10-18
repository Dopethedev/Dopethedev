<p align="center">
  <img src="banner.svg" alt="itsdope: python on arch, mostly things that run locally" width="820">
</p>

**I build things that run on my own machine.** Mostly Python, on Arch with
Hyprland. If it can work without an account, without a subscription, and without
sending my data somewhere, that is the one I want to build.

## What I am working on

**[jarvis](https://github.com/Dopethedev/jarvis)** is a voice assistant that
hears and speaks locally, thinks through whichever model I point it at, and puts
a dashboard on screen that changes mood by voice.

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

These are cheap to say and expensive to keep, which is the point:

- **A test that cannot fail does not count.** Take the fix out, watch the test
  fail, put it back.
- **Numbers come from runs**, not from a datasheet or a guess.
- **Failure paths first.** The quiet failure is the one that matters.
- **Say what was not verified** rather than rounding up to "done".
- **Nothing personal in a tracked file.** Settings live in a file that is ignored.

## Where to look

- [jarvis](https://github.com/Dopethedev/jarvis), the assistant
- [FEATURES.md](https://github.com/Dopethedev/jarvis/blob/main/FEATURES.md),
  including the limits and what it deliberately does not do
- [CONTRIBUTING.md](https://github.com/Dopethedev/jarvis/blob/main/CONTRIBUTING.md),
  the rules the project actually follows
