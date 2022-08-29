# A GUID Generator for EDK II Programming

## What does it do?

This script generate a GUID and formats it in a way that's easy to be used within EDK II codes.

Below are the 3 formats it outputs:

```
d13d75ab-190d-48b9-9f7e-b819ad715aaa
D13D75AB-190D-48B9-9F7E-B819AD715AAA
{ 0xD13D75AB, 0x190D, 0x48B9, { 0x9F, 0x7E, 0xB8, 0x19, 0xAD, 0x71, 0x5A, 0xAA }}
```

## Why the script?

This is a script I wrote & used during my (really short period of) time working at Insyde.

During that time, I found that whenever I need a new GUID I have to go to a website like [this one](https://www.guidgenerator.com/) to make one and format it.

It gets old really quick when you have to make a bunch of them.

That's reason I wrote this script and keybinding it to `Ctrl+Alt+G` in VSCode.
