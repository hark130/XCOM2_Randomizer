# XCOM2_Randomizer
This is a python script to randomize XCOM2 character customizations for me

## TO DO
    [ ] Expand on Character Info
        [ ] Backstory function incorporates 'majority dead' in narrative
        [ ] Implement other racial first names (male and female)
        [ ] Implement other racial last names
        [ ] Implement other racial city lists
        [ ] Implement family into background, dead or alive
        [ ] Include a certain number of Jrs. and IIIds
        [ ] Format the biography to match default in-game creations
        [ ] Implement age
    [ ] Expand on Props
        [ ] Establish color selection for tattoos (implement color wheel?)
        [ ] Armor style ADVENT only gets long sleeve arms
        [ ] Refactor tattoo % based on data (don't forget to inflate):
            [ ] In America, the percentage of people with tattoos is 42% for adults.
            [ ] Percentage of people with tattoos in Canada: 38% of adults.
            [ ] Percentage of people with tattoos in Ireland: 36% of adults.
            [ ] Percentage of people with tattoos in UK: 29% of adults.
    [ ] Expand on Appearance
        [ ] Everyone from Norway has Blue eyes (or colored contacts) and fair skin
        [ ] Base eye color on race (or colored contacts)
    [ ] Rando_Color_Scheme
        [ ] Modify (see: uncomment) randomization algorithm once more Color Schemes are implemented in ColorPalette
        [ ] Investigate ADVENT armor appearance and tie that to "ADVENT" armor style
        [ ] Investigate Alien armor appearance and tie that to "Alien" armor style
        [ ] Chaotic should have an increased chance for Random Chaos color scheme
    [ ] Refactor dictionary into a class
        [ ] Utilize members instead of variables/parameters to influence randomizations
            [ ] Any 'Muton' armor gets 'Muton' mask or 'Muton' face paint
            [ ] Allows for easier themed creation
            [ ] Colors better matched based on established color scheme
            [ ] People with XCOM in their backstory have an increased chance for an XCOM tattoo
            [ ] Mentions of certain words (see: prison, torture) will generate a starting scar
    [ ] Refactor redundant (?) determine_wheel_color() elif chain so the redundancies aren't redundant
    [ ] Refacotr redundant (?) division of mono_primary(), mono_secondary(), etc into a single function
    [ ] Implement a method to verify the same color isn't chosen a second time (necessary?  Dupe colors between Primary and Secondary?)
    [ ] Implement a get_color() wrapper in Weapon Color Palette to sometimes, based on armor style, return normal colored weapons (see: Greyscale)  Function should vary percent chances for normal weapon color based on armor style
    [ ] WRT Main and Secondary Armor colors, Dark (or at least Medium) probably looks better with Light and vice versa... especially Greyscale
    [ ] Refactor Earthy color randomization... probably better served in an adaptation of count_colors but implement count_specific_colors(wheelColor, brightness) and then implement get_specific_color_index(wheelColor, brightness, index)
    [ ] Add Armor Style and Color Scheme notes to the Character Info Biography
    [ ] Urban color scheme should equal increased chance for camo patterns everywhere
    [ ] Urban color scheme should equal higher probability for urban camo patterns
    [ ] Emo color scheme should:
        [ ] Maximize piercings
        [ ] Maximize certain face paint (e.g., Pris, eye black, eyeliner)
        [ ] Maximize tattoos (black and red)
        [ ] Maximize emo hair styles (bows, pigtails?)
        [ ] Minimize facial hair (clean shaven, stubble, and 5 o'clock shadow)
        [ ] Hair color (black, violet, green, purple, red)
        [ ] Hats (bows, fedoras, skull caps, pigtails, etc)
        [ ] Lightest skin tone
    [X] Rename Emo color style to Goth
    [X] Extra input validation on get_color()... if colorToMatch == None and secondColorToMatch != None... error
    [X] Implemenet Color class
        [X] Members
            [X] Number
            [X] Hue
            [X] Saturation
            [X] Value
            [X] Type (see: Primary, Secondary, Tertiary)
            [X] Brightness (see: Light, Medium, Dark)
            [X] Wheel (see: Greyscale, Blue, Blue-Green, Green, Yellow-Green)
        [X] Methods
            [X] Determine Type
            [X] Determine Brightness
            [X] Determine Wheel
    [X] Implement Color Palette class
        [X] Members
            [x] Number of Colors in List [NOT IMPLEMENTED]
            [X] List of Colors
        [X] Methods
            [X] Count a color
            [X] Find a color based on scheme
                [X] Monochromatic
                    [X] Primary
                    [X] Secondary
                    [X] Tertiary
                [X] 2 Colors
                    [X] Analogous
                    [X] Complementary
                [X] 3 Colors
                    [X] Triad
                    [X] Split Complementary
                    [X] Secondary
                [X] Random
                [x] Earthy
                    [X] 2 Colors
                    [?] 3 Colors
                    [X] Random
                [X] Urban
                [X] Goth
                [X] Parallel
        [X] Inherit Child Color Palette Classes
            [X] Main Armor Color
            [X] Secondary Armor Color
            [X] Weapon Color


## NOTES/RESEARCH
### IMPLEMENTING NEW COLOR SCHEMES
Update:
    * xrando: rando_color_scheme()
    * Harklepalette: ColorPalette.implementedSchemes[]
    * Harklepalette: ColorPalette.get_color()
    * Harklepalette: Add new method (called by ColorPalette.get_color())
### [COLOR SCHEMES](http://www.hgtv.com/design/decorating/design-101/color-wheel-primer):
    * Monochromatic - Primary
    * Monochromatic - Secondary
    * Monochromatic - Tertiary
    * 2 Colors - Analogous
    * 2 Colors - Complementary
    * 3 Colors - Triad
    * 3 Colors - Split Complementary
    * 3 Colors - Secondary
    * Random
    * Earthy - 2 Colors
    * Earthy - Random
    * Urban
    * Goth
    * Parallel
### MISC
    * Helmet and upper face prop cannot be equipped together
    * Weapon patterns and armor patterns are identical
    * Left arm tattoo and right arm tattoo list are identical
