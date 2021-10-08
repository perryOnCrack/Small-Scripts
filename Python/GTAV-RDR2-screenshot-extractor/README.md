 # Grand Theft Auto V & Red Dead Redemption 2 PC In-game Camera Photo Extractor

## Where to find the photos?

Any screenshot or in-game camera photos is saved in the directory:

```
%userprofile%\Documents\Rockstar Games\Red Dead Redemption 2\Profiles\[account id]
```

These photo are stored in the files with a prefix `PRDR` or `PGTA`.

## How to use this script?

Run the script with all the photos in the `Unprocessed` directory. It will pull the jpegs and photo taking dates out and put them in `Output` directory.

Processed file will be moved in the `Processed` directory.

## About the `PRDR` & `PGTA` file

These files contain jpeg and some other information, like dates and probably locations.

Dates are stored from 0E to 2F in some weird fashion.
