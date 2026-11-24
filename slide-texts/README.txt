HOW TO EDIT THE SLIDE TEXT

1. Open a slide file, for example 02-the-agency-finds-out-last.txt.
2. Change the text under any [number]. Keep the [number] lines as they are.
     *word*      = the pink italic accent word
     new line    = a line break on the slide
     <b> ... </b> or other <tags>: leave them around the words they style
3. Save, then rebuild the deck. In Terminal:
     cd "/Users/celinasawizki/sales-deck-culvay /slide-texts"
     python3 build.py
4. Refresh http://127.0.0.1:8766 to see the change.

Notes
- build.py overwrites ../index.html with the text from these files.
  Edit text here, not in index.html, or your index.html edits will be replaced.
- _template.html holds the layout. Do not edit it.
- Short numbers like [02.9] that contain "1" or "2" are the numbered circles in the diagrams.
