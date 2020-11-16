# SipherGlyph
an "aesthetic" encryption. a universal language. only 0.1% chance to summon the ghost of unicodes past


![examplesipher](/glyph.mp4)


### how it works (for now)

Every unicode char corresponds to a number (no surprise there).

The "𐒱" char is the key. For now, it's randomly spliced into the output along with two 'key' numbers, like "[#]𐒱[#]". I think I'm going to make the key numbers correspond to row or column rotations -- each side of the "𐒱" char being its own graphable row or column. 

However, some unicode chars don't like to render or will render backwards, i.e., a line of chars "abc" will sometimes render "cba". It doesn't seem to be consistent. I've narrowed down my original charlist *massively*, and it still happens sometimes. Will come back to figure which ones at some point and finish.
