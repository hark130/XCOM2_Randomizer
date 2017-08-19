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
    [ ] Refactor dictionary into a class
    	[ ] Utilize members instead of variables/parameters to influence randomizations
    		[ ] Any 'Muton' armor gets 'Muton' mask or 'Muton' face paint
    		[ ] Allows for easier themed creation
    		[ ] Colors better matched based on established color scheme
    		[ ] People with XCOM in their backstory have an increased chance for an XCOM tattoo
    		[ ] Mentions of certain words (see: prison, torture) will generate a starting scar
    [ ] Implemenet Color class
      [ ] Members
        [ ] Number
        [ ] Hue
        [ ] Saturation
        [ ] Value
        [ ] Type (see: Primary, Secondary, Tertiary)
        [ ] Brightness (see: Light, Medium, Dark)
        [ ] Wheel (see: Greyscale, Blue, Blue-Green, Green, Yellow-Green)
      [ ] Methods
        [ ] Determine Type
        [ ] Determine Brightness
        [ ] Determine Wheel
    [ ] Implement Color Palette
      [ ] Members
        [ ] Number of Colors in Vector
        [ ] Vector of Colors
      [ ] Methods
        [ ] Find a complementary color
          [ ] Monochromatic
          [ ] 2 Colors
          [ ] 3 Colors
          [ ] Random
          [ ] Earthy
          [ ] Urban
          [ ] Emo

## NOTES/RESEARCH
[COLOR SCHEMES](http://www.hgtv.com/design/decorating/design-101/color-wheel-primer):
  * Monochromatic - Primary
  * Monochromatic - Secondary
  * Monochromatic - Tertiary
  * 2 Colors - Analogous
  * 2 Colors - Complementary
  * 3 Colors - Triad
  * 3 Colors - Split Complementary
  * 3 Colors - Secondary
  * Random Chaos
  * Earthy
  * Urban
  * Emo (Monochromatic Black)
NOTE:  Helmet and upper face prop cannot be equipped together
NOTE:  Weapon patterns and armor patterns are identical
NOTE:  Left arm tattoo and right arm tattoo list are identical
